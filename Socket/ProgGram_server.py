'''
this is the server program of a TCP protocol. has to do extra work because has to lock on a socket and listen for clients

'''
import socket
import sys

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
###bind
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)   ## the output here is HOST IP: 127.0.0.1
port = 9999

socket_address = (host_ip,port)
server_socket.bind(socket_address)
# Socket Listen
server_socket.listen(5) ## keeps it waiting if a 6th socket rries to connect, it is refused
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
    print("server waiting for connection")
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    while True:
        data = client_socket.recv(1024)
        if not data or data.decode('utf_8')=='END':
            break
        print('received from client: %s' %data.decode('utf-8'))
        try:
            client_socket.send(bytes('Hey Client','utf-8'))
        except:
            print('Exited by the user.')
    client_socket.close()
server_socket.close()    
        
