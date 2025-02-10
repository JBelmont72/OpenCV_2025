''''
neuralnine for connecting over internet WAN
https://www.youtube.com/watch?v=CC58_XY8yLQ
'''
import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR=('127.0.0.1',5050)
server_socket.bind(ADDR)
print('server socket address: ',ADDR)
server_socket.listen()
print("Socket is listening.")
while True:
    client,addr=server_socket.accept()
    print(('client address:  ',client))
    msg='Hello World'
    client.send(msg.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))