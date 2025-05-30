'''

'''
'''
python -m venv .venv
source .venv/bin/activate

use the 3.9.6 ('venv':venv)  version in the interpreter!!
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
myRadius =20
width=640
height=360
xPos = int(width/2)
yPos =int(height/2)
myBlue=40
myColor= [myBlue,0,255]
myC=50
def myCallBack1(val):
    global xPos
    print('xPos: ',val)
    xPos =val
def myCallBack2(val):
    global yPos
    print('yPos: ',val)
    yPos = val
def myCallBack3(val):
    global myRadius
    print('myRadius: ',val)
    myRadius = val
def myCallBack4(val):
    global myBlue
    print('my Blue', val)
    myBlue =val
def myCallBack5(val):
    global myC
    myC=val
cam = cv2.VideoCapture(1)
# cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my Trackbars')
cv2.resizeWindow('my Trackbars',500,300)
cv2.moveWindow('my Trackbars',width,height)
cv2.createTrackbar('xPos','my Trackbars',xPos,width,myCallBack1)
cv2.createTrackbar('yPos','my Trackbars',yPos,height,myCallBack2)
cv2.createTrackbar('my Radius','my Trackbars',myRadius,int(height/2),myCallBack3)
cv2.createTrackbar('my Blue','my Trackbars',myBlue,255,myCallBack4)
cv2.createTrackbar('myCanny','my Trackbars',myC,255,myCallBack5)
cv2.createTrackbar('myCanny','my Trackbars',myC,255,myCallBack5)
while True:
    ignore,  frame = cam.read()
    cv2.circle(frame,(xPos,yPos),myRadius,myColor,2)
    print(myColor)
    myColor =[myBlue,0,255]
    if myC>100:
        myCanny=cv2.Canny(frame,100,200)
        cv2.imshow('canny',myCanny)
        cv2.moveWindow('canny',width,100)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,100)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()