''' This works, basic Mouseclick to retreive Xpos and YPos
python -m venv .venv
source .venv/bin/activate

use the 3.9.6 ('venv':venv)  version in the interpreter!!
'''
import sys
import cv2
print(f'OpenCV version: {cv2.__version__}')
import numpy as np
print(f"This python is version {sys.version}")
print(f'Numpy version is: {np.__version__}')
def mouseClick(event,XPos,YPos,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Button Down: ',event)
        print('XPos: ',XPos,' YPos: ',YPos)

    if event == cv2.EVENT_LBUTTONUP:
        print('Left Button Up: ',event)
        print('XPos: ',XPos,' YPos: ',YPos)
   
width=640
height=360
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBCam')
cv2.setMouseCallback('my WEBCam', mouseClick)
while True:
    ignore,  frame = cam.read()
    
    cv2.imshow('my WEBCam',frame)
    cv2.moveWindow('my WEBCam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()