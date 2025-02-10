'''Zuni
https://www.youtube.com/watch?v=7gek0eCnbHs
Zuni client socket
1- basic server TCP with fixed paylload size
2- basic server UDP with fixed paylload size
3- !!server TCP with adjusted payload and two-way chat 1-1:23 hr
in udp server, if i make a small payload size in recvfrom(), only a little gets received by the server.
in TCP client, if I make a small payload size. it all gets sent but just in separate payloads
ipconfig getifaddr en0
'''
## program #1  up to minute 51

# import errno
# import sys
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
# ## put socket into listening mode 
# server_socket.listen()
# ## Listen forever to accept ANY connections, accept () returns/ stores the cllient socket and client address

# while True:
#     client_socket,client_address=server_socket.accept()
#     print(client_address)
#     print(type(client_address))
#     print(client_socket)
#     print(type(client_socket))
#     print(f'connected to {client_address}.\n')    
#     ## send a message tothe client who has just connected
#     client_socket.send('You are connected!'.encode(FORMAT))
#     ## close the socket
#     server_socket.close()
#     break
################### program #2 UDP below Server  Zuni  THIS is UDP minute 51-1hr

# import socket
# import threading ## allows multiple actions/ messaging at same time. Non blocking
# HEADER =64  # tells us how big the first message will be always at least 64 and willl have 64 bytes
#         ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
# FORMAT='utf-8'
# DISCONNECT_MESSAGE='Disconnected'
# PORT=5050       ## 80 is used over the internet
# ## CREATE a UDP server side socket IPV4(AF_NET) and UDP (SOCK_DGRAM)
# server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host_name  = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print('HOST IP:',host_ip)
# socket_address = (host_ip,PORT)
# ## bind  the new socket to a tuple(IP address, port address)
# server_socket.bind(socket_address)
# ## will not put socket into listening mode  like we did in TCP. just wait around but not listening
# ### server_socket.listen()
# ## Listen forever to accept ANY connections, accept () returns/ stores the cllient socket and client address

# message,address=server_socket.recvfrom(1024)
# print(message.decode(FORMAT))
# print(address)

####~~~~~PROG 3 TCP CHAT~~1:01 hr TCP server with adjusted buffer
# if send a buffer size larger than specified, it will get there but in subsequent messages
### Chat Server Side
import errno
import sys
import socket
import threading ## allows multiple actions/ messaging at same time. Non blocking
import time
HEADER =64  # tells us how big the first message will be always at least 64 and willl have 64 bytes
        ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
FORMAT='utf-8'
DISCONNECT_MESSAGE='Disconnected'
BYTESIZE=1024
PORT=5050       ## 80 is used over the internet
## 1 create the server socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
# host_ip = str('192.168.1.12')
print('HOST IP:',host_ip)
socket_address = (host_ip,PORT)
### 2    bind the socket to the ipaddress and port, it is a tuple
server_socket.bind(socket_address)
##  3 put socket into listening mode 
server_socket.listen()
## Listen forever to accept ANY connections, accept () returns/ stores the cllient socket and client address
print('Server is running...')    
client_socket,client_address=server_socket.accept()
print(f'connected to {client_address}.\n')    
## send a message tothe client who has just connected
client_socket.send('You are connected!'.encode(FORMAT))
## Send/Receive messages from the client for chat
while True:
        ## Receive info from the client
        message=client_socket.recv(BYTESIZE).decode(FORMAT)
        
        ## Quit if client wants or else continue
        if message == 'quit':
                client_socket.send('quit'.encode(FORMAT))
                print('\nEnding chat... goodbye')
                break
        else:
                print(f'\n{message}')
                message=input('New Message?..')
                client_socket.send(message.encode(FORMAT))
server_socket.close()      