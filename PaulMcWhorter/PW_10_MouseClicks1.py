'''
PW lesson 10 mouse clicks and events
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
# print(cv2.getBuildInformation())
width=640       ##1280 x 640  
height=360
# global evt , pnt
evt=0
xPos =0
yPos =0

def mouseClick(event,xPos,yPos,flags,params):
    global evt, pnt1
    global pnt2
    
    if event== cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event with Left But Down was: ',event)
        print('at position: ',xPos,yPos)
        pnt1=(xPos,yPos)
        evt=event
    if event== cv2.EVENT_LBUTTONUP:
        print('Mouse Event with Left But UP was: ',event)
        print('at position: ',xPos,yPos)
        pnt2=(xPos,yPos)
        evt=event
    if event== cv2.EVENT_RBUTTONUP:
        print('Mouse Event with RIGHT But UP was: ',event)
        print('at position: ',xPos,yPos)
        pnt3=(xPos,yPos)
        evt=event
  
  
cam = cv2.VideoCapture(0)
# cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow('my WebCam') ## need to create this window so the setMouseCLick function will not fault due to not being created yet
cv2.setMouseCallback('my WebCam',mouseClick)

points=[]
while True:
    ignore,  frame = cam.read()
    if  evt ==4:
        cv2.circle(frame,pnt1,15,(0,0,255),3)
        cv2.putText(frame,str(evt),((pnt1[0]+40),pnt1[1]),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0),3)
        cv2.rectangle(frame,pnt1,pnt2,(255,255,0),2)
        ROI=frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
        cv2.imshow('ROI',ROI)
        cv2.moveWindow('ROI',width,0)
    if evt ==5:
        cv2.destroyWindow('ROI')
        evt=0   
    # print(evt, 'EVT')
    cv2.imshow('my WebCam', frame)
    cv2.moveWindow('my WebCam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


# import sys
# import cv2
# print(f'OpenCV version: {cv2.__version__}')
# import numpy as np
# print(f"This python is version {sys.version}")
# print(f'Numpy version is: {np.__version__}')
# evt =0
# xPos =0
# yPos =0
# Thickness = 2
# CircleSize =25
# Color =[0,0,255]

# def mouseClick(event,xPos,yPos,flags,params):
#     global evt
#     global pnt
#     if event == cv2.EVENT_LBUTTONDOWN:        
#         print('Left Mouse Down was: ',event)
#         print('at Postion',xPos,' x  ',yPos, ' y')
#         evt = event
#         pnt = (xPos,yPos)
#     if event == cv2.EVENT_LBUTTONUP:
         
        
#         print('Left Mouse Up was: ',event)
#         print('at Postion',xPos,' x  ',yPos, ' y')
#         evt = event
#     if event  == cv2.EVENT_RBUTTONUP:
#         print('Right Mouse Up was: ',event)
#         print('at Postion',xPos,' x  ',yPos, ' y')
#         evt = event         #evt will be set to 5 and will not put the circle on the frame. thus the circle wil disappear
          
    
# # want to put a circle when the button is clicked.  Have to put it in the while loop because the cicle would be present only for One frame if it was up here.    
# width=640
# height=360
# cam = cv2.VideoCapture(0)
# # cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# cv2.namedWindow('my WEBcam')
# cv2.setMouseCallback('my WEBcam', mouseClick)
# while True:
#     ignore,  frame = cam.read()
#     if evt == 1 or evt == 4:
#         cv2.circle(frame,pnt,CircleSize,Color,Thickness)       
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
    
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()


######## i can draw lines with the below function. could be useful but conflicts when I was creating an ROI 
## might work with 'and ' bollean conditions added. just for fun simetime.