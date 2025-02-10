'''Tech with tim  client
https://www.youtube.com/watch?v=3QiPPX-KeSc


-modem has one public IP address.
-in LAN  has local IP address also called the IPV4 address
- if run a server on the public IP address, accessible worldwide
https://www.geeksforgeeks.org/broken-pipe-error-in-python/
this corrected the broken pipe error i had
The Emergence of Broken Pipe Error
A broken Pipe Error is generally an Input/Output Error, which is occurred at the Linux System level. The error has occurred during the reading and writing of the files and it mainly occurs during the operations of the files. The same error that occurred in the Linux system is EPIPE, but every library function which returns its error code also generates a signal called SIGPIPE, this signal is used to terminate the program if it is not handled or blocked. Thus a program will never be able to see the EPIPE error unless it has handled or blocked SIGPIPE.

Python interpreter is not capable enough to ignore SIGPIPE by default, instead, it converts this signal into an exception and raises an error which is known as IOError(INPUT/OUTPUT error) also know as ‘Error 32’ or Broken Pipe Error.
how to host a server on line!!! linode , ubuntu  and putty used
https://www.youtube.com/watch?v=KQasIwElg3w

'''

import socket

HEADER =64  # tells us how big the first message will be always at least 64 and willl have 64 bytes
        ## will have a message that is padded to be 64  bytes long, can be a problem is message is too short
FORMAT='utf-8'
DISCONNECT_MESSAGE='Disconnected'
PORT=5050       ## 80 is used over the internet
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ADDR=(host_ip,PORT)
print('HOST IP:',host_ip)
socket_address = (host_ip,PORT)

client_socket.connect(socket_address)

## the above connects to the server.  below we will create the message/payload
def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message) ## next we have to make sure the message is 64 bytes long
    send_length=str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER-len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)
    
    print(client_socket.recv(2048).decode(FORMAT))
    # print(client_socket.recv(2048))
# send(f'\nquit')   
# send(f'\nHello Server!!!WOW') 
  
send(f'\nHello WOrld from ME')
input()
send(f'\nHi Jannie')
input()
send(f'\nDisconnected')
input()

