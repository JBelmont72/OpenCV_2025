'''

'''
# import sys
# import cv2
# import time
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)
# cam=cv2.VideoCapture(1)
# width=1280
# height=720
# cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS,30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# print(cam.get(3),' x ',cam.get(4))
# boxY=40
# boxX=80
# Bx=int(width/2)
# By=int(height/2)

# while True:
#     _,frame=cam.read()
#     frameROI=frame[int(.5*height -boxY):int(.5*height+boxY),int(.5*width -boxX):int(.5*width+boxX)]
#     grayROI=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
#     grayToBGRroi=cv2.cvtColor(grayROI,cv2.COLOR_GRAY2BGR)
#     frame[int(.5*height -boxY):int(.5*height+boxY),int(.5*width -boxX):int(.5*width+boxX)]=grayToBGRroi
#     cv2.imshow('my Gray ROI',grayROI)
#     cv2.moveWindow('my Gray ROI',width,int(.20*height))
#     cv2.imshow('my ROI', frameROI)
#     cv2.moveWindow('my ROI',width,0)
#     cv2.imshow('my WEBcam',frame)
#     cv2.moveWindow('myWEBcam',0,0)

#     if cv2.waitKey(1)& 0xFF==ord('q'):
#         break
# cam.release()
# cv2.destroyAllWindows()

###~~~~~~~~~~~~~~bouncing ROI

import sys
import cv2
import time
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
cam=cv2.VideoCapture(1)
width=1280
height=720
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
print(cam.get(3),' x ',cam.get(4))
boxY=100
boxX=180
Bx=int(width/2)
By=int(height/2)
x=Bx
y=By
deltaX=10
deltaY=10
while True:
    _,frame=cam.read()
    frameROI=frame[int(.5*height -boxY):int(.5*height+boxY),int(.5*width -boxX):int(.5*width+boxX)]
    print('frameROI shape: ',frameROI.shape)
    grayROI=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    grayToBGRroi=cv2.cvtColor(grayROI,cv2.COLOR_GRAY2BGR)
    x=x+deltaX
    print('X ',x)
    if int(x+boxX+7) >=width or int(x-boxX-7)<=0:
    # if x>=int(width-boxX) or x <=int(boxX):
        deltaX=(-1)*deltaX
    y=y+deltaY
    
    print(y)
    if int(y+boxY+7)>=height or int(y-boxY-7)<=0:
    # if y>=int(height-boxY) or y<= int(boxY):
        deltaY = (-1)*deltaY
    # if x>=int(width-boxX) or x <=int(boxX):
    #     deltaX=(-1)*deltaX
    # y=y+deltaY
    # print(y)
    # if y>=int(height-boxY) or y<= int(boxY):
    #     deltaY = (-1)*deltaY
        
        
       
    # frame[int(y -boxY):int(y+boxY),int(x -boxX):int(x+boxX)]=grayToBGRroi
    frame[int(y -boxY):int(y+boxY),int(x -boxX):int(x+boxX)]=grayToBGRroi
    print('ROI shape ',grayToBGRroi.shape)
    cv2.imshow('my Gray ROI',grayROI)
    cv2.moveWindow('my Gray ROI',width,int(.20*height))
    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI',width,0)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('myWEBcam',0,0)

    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()