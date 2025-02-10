'''PW 13 Homework
can track two different colored objects at the same time in OpenCV. 
'''
# import numpy as np
# import cv2
# print(cv2.__version__)
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
 
 
# width=960
# height=540
# cam=cv2.VideoCapture(0)
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
 
#     myMask=myMask | myMask2
#     #myMask=cv2.add(myMask,myMask2)
#     #myMask=np.logical_or(myMask,myMask2)
 
#     #myMask=cv2.bitwise_not(myMask)
#     myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
#     mySelection=cv2.bitwise_and(frame,frame, mask=myMask)
#     mySelection=cv2.resize(mySelection,(int(width/2),int(height/2)))
#     cv2.imshow('My Selection', mySelection)
#     cv2.moveWindow('My Selection',int(width/2),height)
 
#     cv2.imshow('My Mask', myMaskSmall)
#     cv2.moveWindow('My Mask',0,height)
#     cv2.imshow('my WEBcam',frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()
'''
possibility below is that with a green screen you make a mask of the foreground, ME, and then use the cv2.bitwise_not() to be equal to the background photo, Then use cv2.add()to combine them
'''

########~~~~~7 Jan 2025 create a mask with trackbars selecitng color
import cv2
import numpy as np

width=640
height=480
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
print(cam.get(3),' x ',cam.get(4))
def LH(val):
    global l_h
    print('lower Hue ',val)
    l_h=val    
def LS(val):
    global l_s
    l_s =val
    print('lower Sat ',l_s)
def LV(val):
    global l_v
    l_v=val
    print('lower Val ',l_v)
def UH(val):
    global u_h
    print('upper Hue ',val)
    u_h=val    
def US(val):
    global u_s
    u_s =val
    print('upper Sat ',u_s)
def UV(val):
    global u_v
    u_v=val
    print('upper Val ',u_v)

def LH_2(val):
    global l_h2
    print('lower Hue_2 ',val)
    l_h2=val    
def UH_2(val):
    global u_h2
    print('upper Hue_2 ',val)
    u_h2=val 

cv2.namedWindow('myTrackbars')
cv2.createTrackbar('Lower Hue','myTrackbars',30,180,LH)
cv2.createTrackbar('Upper Hue','myTrackbars',30,180,UH)
cv2.createTrackbar('Lower Sat','myTrackbars',20,255,LS)
cv2.createTrackbar('Upper Sat','myTrackbars',20,255,US)
cv2.createTrackbar('Lower Val','myTrackbars',30,255,LV)
cv2.createTrackbar('Upper Val','myTrackbars',30,255,UV)
cv2.createTrackbar('Lower Hue_2','myTrackbars',30,180,LH_2)
cv2.createTrackbar('Upper Hue_2','myTrackbars',30,180,UH_2)

while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_b=np.array((l_h,l_s,l_v),dtype=np.uint8)
    u_b=np.array([u_h,u_s,u_v],dtype=np.uint8)
    Mask=cv2.inRange(frameHSV,l_b,u_b)
    l_b2=np.array((l_h2,l_s,l_v),dtype=np.uint8)
    u_b2=np.array([u_h2,u_s,u_v],dtype=np.uint8)
    # mask=cv2.bitwise_not(mask)
    
    MyMask2=cv2.inRange(frameHSV,l_b2,u_b2)
    # comboMask=MyMask2 |Mask
    comboMask=cv2.add(MyMask2,Mask)
    mySelection=cv2.bitwise_and(frame,frame,mask=comboMask)
    cv2.imshow('myMask2',MyMask2)
    cv2.moveWindow('myMask2',int(width/2),int(height/2+50))
    cv2.imshow('Mask',Mask)
    cv2.moveWindow('Mask',int(width/2),50)
    cv2.imshow('mySelection',mySelection)
    cv2.imshow('Frame',frame)
    cv2.moveWindow('Frame',0,50)
    cv2.imshow('Combo',comboMask)
    cv2.moveWindow('Combo',int(width/2),int(height+50))
    if cv2.waitKey(1) & 0xff==27:
        break
cam.release()
cv2.destroyAllWindows()