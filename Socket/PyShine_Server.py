'''pyShine  video socket
https://www.youtube.com/watch?v=7-O7yeO3hNQ
Socket programming to send and receive webcam video

'''
# Welcome to PyShine
##my public IP address New Hampshire 75.68.100.114
# This code is for the server 
# Lets import the libraries
import socket, cv2, pickle,struct,imutils

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
# host_ip = "75.68.100.114"
# host_ip='192.168.1.12'
# host_ip='192.168.1.117'		## florida
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
	client_socket,addr = server_socket.accept()
	print('GOT CONNECTION FROM:',addr)
	if client_socket:
		vid = cv2.VideoCapture(1)
		
		while(vid.isOpened()):
			img,frame = vid.read()
			frame = imutils.resize(frame,width=320)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			print(struct.calcsize("Q"))
			print(len(a))
			# print(a)
			# print(message)
			client_socket.sendall(message)
			
			cv2.imshow('TRANSMITTING VIDEO',frame)
			key = cv2.waitKey(1) & 0xFF
			if key ==ord('q'):
				client_socket.close()