'''
Zuni client socket
1- basic client TCP with fixed paylload size
2- basic client UDP with fixed paylload size
3- !! TCP CHAT client TCP with adjusted payload and two-chat 1-1:23 hr

'''
###  program #1  Zuni   Server  SOcket
# import socket
# HEADER =64  # tells us how big the first message will be always at least 64 and willl have 64 bytes
#         ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
# FORMAT='utf-8'
# DISCONNECT_MESSAGE='Disconnected'
# PORT=5050       ## 80 is used over the internet
# ## create a client side IPV4 socket and TCP(sock_stream)
# client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ## obtain the IP dynamically
# host_name  = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print('HOST IP:',host_ip)
# socket_address = (host_ip,PORT)
# ## Connect the socket to a server
# client_socket.connect(socket_address)
# ## Receive a message from the server_must specify the max number of bytes to receive
# message= client_socket.recv(1024)
# print(message.decode(FORMAT))
# # print(message,type(message))
# ## close the client socker
# client_socket.close()
########  program #2 UDP Zuni Server start minute 51  to 1 hour This is UDP!!
# import socket
# HEADER =64  # tells us how big the first message will be always at least 64 and willl have 64 bytes
#         ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
# FORMAT='utf-8'
# DISCONNECT_MESSAGE='Disconnected'
# PORT=5050       ## 80 is used over the internet
# ## create a client side IPV4 socket and UDP(socket_DGRAM)
# client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# ## obtain the IP dynamically
# host_name  = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print('HOST IP:',host_ip)
# socket_address = (host_ip,PORT)
# ## send some info via a connectionless protocol to the server
# client_socket.sendto('Hello Server! How are you?'.encode(FORMAT),socket_address)
####~~~ 1:01 TCP CHAT Client with adjusting the buffer size

import socket
HEADER =64  # tells us how big the first message will be always at least 64 and willl have 64 bytes
        ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
FORMAT='utf-8'
BYTESIZE=1024
DISCONNECT_MESSAGE='Disconnected'
PORT=5050       ## 80 is used over the internet
## create a client side IPV4 socket and TCP(sock_stream)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
## obtain the IP d
# dynamically
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name) ## this is local for only the same computer
print('HOST IP:',host_ip)
socket_address = (host_ip,PORT)
## Connect the socket to a server
client_socket.connect(socket_address)
## Receive a message from the server_must specify the max number of bytes to receive
##      for demonstration decrease buffer size from 1024 to 10BYTES! and duplicate
while True:     ## send and receeive messages
        message= client_socket.recv(BYTESIZE).decode(FORMAT)## receive and decode in one line
        
        ## quit if connected server wants to quit,
        if message=='quit':
                client_socket.send('quit'.encode(FORMAT))
                print("\nEnding the chat...Goodbye")
                break
        else:
                print(f'\n{message}')
                message= input("Message:  ")
                client_socket.send(message.encode(FORMAT))
        # print(message.decode(FORMAT))
        # print(message,type(message))
        ## close the client socker
client_socket.close()
