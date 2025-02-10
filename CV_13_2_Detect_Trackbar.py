'''CV_13 Object detection
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!
cv2.createTrackbar('CurPos','img',10,400,nothing) # the 5th arduemtn is the callback function
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cv2's code number fort width is 3 and height is 4
# Can use those code numbers in lieu of print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))such as in cap.set() method
cap.set(3, 1280)
cap.set(4, 720)
print(cap.set(3,1280))
print(cap.set(4,720))
print(cap.get(3))
print(cap.get(4))
I added a canny conversion to this
'''
import cv2 
import numpy as np
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 360)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


def nothing(x):
    pass

cv2.namedWindow('ColorTrack')
cv2.createTrackbar('LowerHue','ColorTrack',50,255,nothing)
cv2.createTrackbar('UpperHue','ColorTrack',50,255,nothing)
cv2.createTrackbar('LowerSat','ColorTrack',50,255,nothing)
cv2.createTrackbar('UpperSat','ColorTrack',50,255,nothing)
cv2.createTrackbar('LowerVal','ColorTrack',50,255,nothing)
cv2.createTrackbar('UpperVal','ColorTrack',50,255,nothing)

while True:
    # frame = cv2.imread('images/smarties.png')
    _,frame = cap.read()
    hsv   = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # trackbars are used to create lower and upper bounds
    l_h =cv2.getTrackbarPos('LowerHue','ColorTrack')
    u_h =cv2.getTrackbarPos('UpperHue','ColorTrack')
    l_s =cv2.getTrackbarPos('LowerSat','ColorTrack')
    u_s =cv2.getTrackbarPos('UpperSat','ColorTrack')
    l_v =cv2.getTrackbarPos('LowerVal','ColorTrack')
    u_v =cv2.getTrackbarPos('UpperVal','ColorTrack')
    
    
    l_b = np.array([l_h,l_s,l_v])
    u_b =np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask = mask) 
    myCanny=cv2.Canny(res,100,200)  
    cv2.imshow('frame',frame)
    cv2.moveWindow('frame',0,20)
    cv2.imshow('mask',mask)
    cv2.moveWindow('mask',640,20)
    cv2.imshow('res',res)
    cv2.moveWindow('res',0,380)
    cv2.imshow('myCanny',myCanny)
    cv2.moveWindow('myCanny',640,380)
    key = cv2.waitKey(1)
    if key == 27:
        break
    cv2.destroyAllWindows


cap.release()