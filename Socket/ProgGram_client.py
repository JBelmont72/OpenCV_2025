'''CLIENT
programming knowledge 'Python Socket Programming Tutorial'
90% of sockets are family=AF_INET
type=SOCK_STREAM for TCP socket
used www.python.org  port 80
to connect to a server process using a TCP client program

the server process has to carry out extra work, has to bind and also listen for clients
'''
# import socket
# import sys
# try:
#     sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# except socket.error as err:
#     print('Failed to create a socket')
#     print('Reason: ',str(err))
# print('socket created')
# target_host=input('Enter the target_host name to connect')
# target_port=input("enter the target port")
# try:
#     sock.connect(((target_host, int(target_port))))
#     print('Socket connected to:  '+ target_host +target_port)
#     sock.shutdown(2)
# except socket.error as err:
#     print('Failed to connect %s on port %s' %(target_host,target_port))
#     print('Reason: ',str(err))
#     sys.exit()
##~~~~~~~~~~~~~minute 42 programming Knowledge 
# import socket

# client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# target_host='127.0.0.1'
# target_port=9999
# client_socket.connect(('127.0.0.1', 9999))
# print('Socket connected to:  '+ target_host +target_port)
# payload = 'Hey Server'
# try:
#     while True:
#         client_socket.send(payload.encode('utf-8'))
#         data=client_socket.recv(1024)
#         print('data: ',str(data))
#         more = input('want to send more data to the server?')
#         if more.lower()=='y':
#             payload=input('Enter Payload')
#         else:
#             break
# except KeyboardInterrupt:
#     print('Exited by user')
# client_socket.close()

###~~~~
import socket
import sys
try:
    client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print('Failed to create a socket')
    print('Reason: ',str(err))
print('socket created')
target_host='127.0.0.1'
target_port=12345
# target_host='192.168.1.11'
# target_port=9999
# target_host=input('Enter the target_host name to connect')
# target_port=input("enter the target port")
payload = 'Hey Server'
try:
    client_socket.connect(((target_host, int(target_port))))
    print('Socket connected to:  '+ target_host +target_port)
    client_socket.shutdown(2)
    while True:
        client_socket.send(payload.encode('utf-8'))
        data=client_socket.recv(1024)
        print('data: ',str(data))
        more = input('want to send more data to the server?')
        if more.lower()=='y':
            payload=input('Enter Payload')
        else:
            break
except socket.error as err:
    print('Failed to connect %s on port %s' %(target_host,target_port))
    print('Reason: ',str(err))
    sys.exit()