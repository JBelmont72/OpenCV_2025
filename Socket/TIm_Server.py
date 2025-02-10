'''Tech with tim   Server https://www.youtube.com/watch?v=3QiPPX-KeSc
ipconfig getifaddr en0  to get ip address  192.168.1.12
M is UDP
how to host a server on line!!! linode , ubuntu  and putty used
https://www.youtube.com/watch?v=KQasIwElg3w

judsonbelmont@MacBook-Pro ~ % ipconfig getifaddr en0
192.168.1.117
'''
# import socket
# import threading ## allows multiple actions/ messaging at same time. Non blocking
# import time
# HEADER =64  # tells us how big the first message will be always at least 64 and willl have 64 bytes
#         ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
# FORMAT='utf-8'
# DISCONNECT_MESSAGE='Disconnected'
# PORT=5050       ## 80 is used over the internet
# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host_name  = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print('HOST IP:',host_ip)
# socket_address = (host_ip,PORT)

# server_socket.bind(socket_address)

# def handle_client(conn,socket_address):
#     print(f"[NEW CONNECTION]{socket_address} connected.")
#     connected=True
#     while connected:
#         msg_length=conn.recv(HEADER).decode(FORMAT)
#         if msg_length:            
#             msg_length=int(msg_length)
#             msg=conn.recv(msg_length).decode(FORMAT)
#             print(f'[{socket_address}]{msg}')
#             if msg==DISCONNECT_MESSAGE:
#                 connected=False
#         ## now can send a message back to the client
#         print(f'[{socket_address}] {msg}') 
#         conn.send('Msg received from client '.encode(FORMAT))      
              
#     conn.close()
# def start():
#     server_socket.listen()
#     print(f'[LISTENING] server is listening on {host_ip}')
#     while True:
#         conn,socket_address=server_socket.accept()
#         thread=threading.Thread(target=handle_client,args=(conn,socket_address))
#         thread.start()
#         print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')
    
# print(('[STARTING] server is starting...'))
# start()

####~~~~~~~~~~~
import errno
import sys
import socket
import threading ## allows multiple actions/ messaging at same time. Non blocking
import time
HEADER =64  # tells us how big the first message will be always at least 64 bytes and will have 64 bytes
        ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
FORMAT='utf-8'
DISCONNECT_MESSAGE='Disconnected'
PORT=5050       ## 80 is used over the internet
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)## #1 creates a socketobject of IPV4,and to stream data through socket,  'family' and 'type'
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ADDR=(host_ip,PORT)## for some reason this worked better here
print('HOST IP:',host_ip)
socket_address = (host_ip,PORT) 

server_socket.bind(ADDR)    ###  # 2 binds thge socket object to the ADDRESS, anything that comes to this ADDR is designated for this cocket
## will run for each client and run concurrently
def handle_client(conn,addr):   ## # 5 this kicks in to take the individual client object and address and deal with it, runs concurrently for each clinet
    print(f"[NEW CONNECTION]{addr} connected.")
    connected=True
    try:
        while connected: ### # 6 after connected with a client, triggered by thread function
            msg_length=conn.recv(HEADER).decode(FORMAT)##three steps - step 1, we will receive a message of x lenght and want it to be 64 bytes as notified and sent by the client.  We will pad the message to make it 64 bytes
            if msg_length:            
                msg_length=int(msg_length)
                msg=conn.recv(msg_length).decode(FORMAT)### conn is a socket object to allow us to communicate back to the client,  this second time we get the acutual message, first time just the length
                print(f'[{addr}]{msg}')
                print(f' msg_length:  {msg_length}')
                if msg==DISCONNECT_MESSAGE:
                    connected=False
            ## now can send a message back to the client
            print(f'[{addr}] {msg}') 
            conn.send('Msg received from client '.encode(FORMAT))      
                
        conn.close()
    
    except IOError as e: 
        if e.errno == errno.EPIPE:
            print("error") 
            pass
        # Handling of the error
        
def start():        ### #3 this is the code that sets the socket object to LISTEN() , 
    server_socket.listen()
    print(f'[LISTENING] server is listening on {host_ip}')
    while True:     ### #4 will store the new connection. conn stores the ip address and addr
        conn,addr=server_socket.accept()## waits for a new connection of a client
        ###the conn is the client_socket
        print('Server is running...')    
        # client_socket,client_address=server_socket.accept()
        print(f'connected to {conn}.\n')    
        ## send a message tothe client who has just connected
        conn.send('You are connected!'.encode(FORMAT))
## Send/Receive messages from the client for chat
        
        thread=threading.Thread(target=handle_client,args=(conn,addr))## the handle_client will handle the communiction to the client
        # thread=threading.Thread(target=handle_client,args=(conn,socket_address))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')## make it minus one because we have our own thread connection
    
print(('[STARTING] server is starting...'))
start()