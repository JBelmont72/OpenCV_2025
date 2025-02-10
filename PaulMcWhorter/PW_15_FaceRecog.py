'''PW_15
simple method to detect faces in a WEB cam frame using  openCV and Haar Cascades. 
'''
import cv2
print(cv2.__version__)
width=640
height=480
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
## faceCascade is the OBJECT
faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
# faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalcatface_extended.xml')
# faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalcatface.xml')
 
while True:
    ignore,  frame = cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ## faces is the attribute returne by the .method applied to the OBJECT
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('my WEBcam', frame)
    print(frame.shape)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()