'''  
https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
contour principles interesting reading
'''
'''
Lesson 14 this is same as CV_14 but with notes
Find the contour on the mask, not on the frame
python -m venv .venv
source .venv/bin/activate

use the 3.9.6 ('venv':venv)  version in the interpreter!!
https://www.pythonpool.com/cv2-boundingrect/
CV2 Boundingrect returns 4 numeric values when the contour is passed as an argument. These 4 values correspond to x, y, w, h 
'''
# import sys
# import cv2
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)

#  #  640  380  <> 960 540
# width=640 #960
# height=480 #540
# hueLow=90
# hueHigh=100
 
# hueLow2=90
# hueHigh2=100
 
# satLow=20
# satHigh=200
# valLow=20
# valHigh=200
# def onTrack1(val):
#     global hueLow
#     hueLow=val
#     print('Low Hue: ',val)
# def onTrack2(val):
#     global hueHigh
#     hueHigh=val
#     print('High Hue: ',val)
# def onTrack3(val):
#     global satLow
#     satLow=val
#     print('Low Sat: ',val)
# def onTrack4(val):
#     global satHigh
#     satHigh=val
#     print('High Sat: ',val)
# def onTrack5(val):
#     global valLow
#     valLow=val
#     print('Low Val: ',val)
# def onTrack6(val):
#     global valHigh
#     valHigh=val
#     print('High Val: ',val)
 
 
# def onTrack7(val):
#     global hueLow2
#     hueLow2=val
#     print('Low Hue2: ',val)
# def onTrack8(val):
#     global hueHigh2
#     hueHigh2=val
#     print('High Hue2: ',val)
 
# cam=cv2.VideoCapture(1)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) 
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# cv2.namedWindow('myTracker')
# cv2.moveWindow('myTracker',width,0)
# cv2.resizeWindow('myTracker',400,500)
# cv2.createTrackbar('Hue Low','myTracker',15,180,onTrack1)
# cv2.createTrackbar('Hue High','myTracker',30,180,onTrack2)
 
# cv2.createTrackbar('Hue Low2','myTracker',50,180,onTrack7)
# cv2.createTrackbar('Hue High2','myTracker',60,180,onTrack8)
 
# cv2.createTrackbar('Sat Low','myTracker',10,255,onTrack3)
# cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
# cv2.createTrackbar('Val Low','myTracker',10,255,onTrack5)
# cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)
 
 
# while True:
#     ignore,  frame = cam.read()
#     frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
 
#     lowerBound=np.array([hueLow,satLow,valLow])
#     upperBound=np.array([hueHigh,satHigh,valHigh])
 
#     lowerBound2=np.array([hueLow2,satLow,valLow])
#     upperBound2=np.array([hueHigh2,satHigh,valHigh])
 
#     myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
#     myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
#  # myMask is the amalgam of myMask and MyMask2
#     myMask=myMask | myMask2 #the vertical bar means 'OR'
#     # myMask=cv2.add(myMask,myMask2)
#     # myMask=np.logical_or(myMask,myMask2)
#     contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     #cv2.drawContours(frame,contours,-1,(255,0,0),3)
#     ### the drawcontours wants the whole array
#     for contour in contours:
#         area=cv2.contourArea(contour)
#         if area>=200:
#             #cv2.drawContours(frame,[contour],0,(255,0,0),3)
#             ## the drawcontours command expects an array of contours but we are just passing a single array. so need to put it inside an array
#             ## could do it with myContour=[contour] OR just put contour in [contour] as shown above
#             x,y,w,h=cv2.boundingRect(contour)
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
# ## https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html cool oblique box:
#             rect = cv2.minAreaRect(contour)
#             box = cv2.boxPoints(rect)
#             box = np.int0(box)
#             cv2.drawContours(frame,[box],0,(0,0,255),print(frame.shape))
            
#     #myMask=cv2.bitwise_not(myMask)
#     myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
#     mySelection=cv2.bitwise_and(frame,frame, mask=myMask)
#     mySelection=cv2.resize(mySelection,(int(width/2),int(height/2)))
#     cv2.imshow('My Selection', mySelection)
#     cv2.moveWindow('My Selection',int(width),int(height/2))
 
#     cv2.imshow('My Mask', myMaskSmall)
#     cv2.moveWindow('My Mask',int(width),int(height))
#     cv2.imshow('my WEBcam',frame)
#     cv2.moveWindow('my WEBcam',0,int(height/2))
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()
# cv2.destroyAllWindows()

###~~~~~~~create a rainbow 8 Jan 2025
###  create window with hue col going from zero to 179 and saturation from 0 to 255 in rows
# import cv2
# import numpy as np
# print(cv2.__version__)
# import sys
# print(sys.version_info)
# x=np.zeros([255,180*4,3],dtype=np.uint8)
# # x=np.zeros([255,180,3],dtype=np.uint8)
# for row in range(0,255,1):
#     for col in range(0,720,1):
#         x[row,col]=[int(col/4),row,255]##here the value is pinned at 255
# # for row in range(0,255,1):
# #     for col in range(0,180,1):
# #         x[row,col]=[col,row,255]##here the value is pinned at 255
# ## make hue go to 0-180 and value 0-255 and sat constant at 255
# y =np.zeros([255,4*180,3],dtype=np.uint8)
# for col in range(0,720,1):
#     for row in range(0,255,1):
#         y[row,col]=[int(col/4),255,row]

# while True:
#     xBGR=cv2.cvtColor(x,cv2.COLOR_HSV2BGR)
#     yBGR=cv2.cvtColor(y,cv2.COLOR_HSV2BGR)
#     cv2.imshow('yBGR',yBGR)
#     cv2.imshow('img',xBGR)
#     if cv2.waitKey(0)&0xff==27:
#         break
# cv2.destroyAllWindows()

###~~~~~~~~~~~ In this program the object of interest moves the whole screen
import numpy as np
import cv2
print(cv2.__version__)
hueLow=90
hueHigh=100
 
hueLow2=90
hueHigh2=100
 
satLow=20
satHigh=200
valLow=20
valHigh=200
def onTrack1(val):
    global hueLow
    hueLow=val
    print('Low Hue: ',val)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('High Hue: ',val)
def onTrack3(val):
    global satLow
    satLow=val
    print('Low Sat: ',val)
def onTrack4(val):
    global satHigh
    satHigh=val
    print('High Sat: ',val)
def onTrack5(val):
    global valLow
    valLow=val
    print('Low Val: ',val)
def onTrack6(val):
    global valHigh
    valHigh=val
    print('High Val: ',val)
 
 
def onTrack7(val):
    global hueLow2
    hueLow2=val
    print('Low Hue2: ',val)
def onTrack8(val):
    global hueHigh2
    hueHigh2=val
    print('High Hue2: ',val)
 
width =640
height=480
xPos=200
yPos=250
# width=960 ##640
# height=540    ##480
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cv2.namedWindow('myTracker')
cv2.moveWindow('myTracker',width,0)
cv2.resizeWindow('myTracker',400,500)
cv2.createTrackbar('Hue Low','myTracker',15,180,onTrack1)
cv2.createTrackbar('Hue High','myTracker',30,180,onTrack2)
 
cv2.createTrackbar('Hue Low2','myTracker',50,180,onTrack7)
cv2.createTrackbar('Hue High2','myTracker',60,180,onTrack8)
 
cv2.createTrackbar('Sat Low','myTracker',79,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',110,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',80,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',129,255,onTrack6)
 
 
while True:
    ignore,  frame = cam.read()
    # frame=cv2.resize(frame,(0,0),fx=.7,fy=0.7)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    print(frame.shape)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
 
    lowerBound2=np.array([hueLow2,satLow,valLow])
    upperBound2=np.array([hueHigh2,satHigh,valHigh])
 
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
 
    myMask=myMask | myMask2
    #myMask=cv2.add(myMask,myMask2)
    #myMask=np.logical_or(myMask,myMask2)
    contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(255,0,0),3)
    
    for contour in contours:
        area=cv2.contourArea(contour)
        if area>=200:
            #cv2.drawContours(frame,[contour],0,(255,0,0),3)
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

            xPos =x
            yPos=y
            xPos=int(xPos/width*1920)
            yPos=int(yPos/height*1080)
            # xPos=int(xPos/frame.shape[1])
            # yPos=int(yPos/frame.shape[0])
            print(xPos,yPos)
        
        
        
    #myMask=cv2.bitwise_not(myMask)
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    mySelection=cv2.bitwise_and(frame,frame, mask=myMask)
    mySelection=cv2.resize(mySelection,(int(width/2),int(height/2)))
    cv2.imshow('My Selection', mySelection)
    cv2.moveWindow('My Selection',width,int(height*.6))
 
    cv2.imshow('My Mask', myMaskSmall)
    cv2.moveWindow('My Mask',width,0)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,240)
    cv2.moveWindow('my WEBcam',xPos,yPos)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

######~~~~~~~~
# import cv2
# image = cv2.imread("images/smarties.png")

# while True:
#     cv2.imshow("image",image)
#     gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Changed",gray)
#     ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#     # contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#     contours,hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     print("Number of contours:" + str(len(contours)))
#     for contour in contours:
#         area=cv2.contourArea(contour)
#         if area>200:
#             x,y,w,h = cv2.boundingRect(contours[0])
#             cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
#             cv2.imshow("result",image)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         cv2.destroyAllWindows()