''''
neuralnine for connecting over internet WAN
https://www.youtube.com/watch?v=CC58_XY8yLQ
'''
import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR=('127.0.0.1',5050)
### No bind or listen as in the server
print('client socket address: ',ADDR)
client_socket.connect(ADDR)
while True:
    print(client_socket.recv(1024).decode('utf-8'))
    msg=("client received message ")
    client_socket.send(msg.encode('utf-8'))
