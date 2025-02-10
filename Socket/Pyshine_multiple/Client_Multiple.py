'''
https://www.pyshine.com/Socket-Programming-with-multiple-clients/
Transfer video over sockets from multiple clients
the pyshine Library:(has good examples to review)
https://pypi.org/project/pyshine/       to install
pip install pyshine
https://www.pyshine.com/Faster-video-transfer-over-wifi/


how to host a server on line!!! linode , ubuntu  and putty used
https://www.youtube.com/watch?v=KQasIwElg3w
'''
# Welcome to PyShine
# lets make the client code
# In this code client is sending video to server
import socket,cv2, pickle,struct
import pyshine as ps # pip install pyshine
import imutils # pip install imutils
camera = True
if camera == True:
	vid = cv2.VideoCapture(0)
else:
	vid = cv2.VideoCapture('videos/mario.mp4')
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.1.11' # Here according to your server ip write the address

port = 9999
client_socket.connect((host_ip,port))

if client_socket: 
	while (vid.isOpened()):
		try:
			img, frame = vid.read()
			frame = imutils.resize(frame,width=380)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			cv2.imshow(f"TO: {host_ip}",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				client_socket.close()
		except:
			print('VIDEO FINISHED!')
			break