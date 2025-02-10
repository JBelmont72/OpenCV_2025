'''CV_13 Object detection
Initial use of upper and lower bounds
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!
no trackbars,  using fixed values for upper and lower boundaries
'''
import cv2 
import numpy as np

while True:
    frame = cv2.imread('images/smarties.png')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # trackbars are used to create lower and upper bounds
    
    l_b = np.array([100,45,55])
    u_b =np.array([130,255,255])
    mask = cv2.inRange(hsv,l_b,u_b)
    # now show mask on  the original image below
    res = cv2.bitwise_and(frame,frame,mask = mask)
    
    
    cv2.imshow('frame',frame)
    cv2.moveWindow('frame',0,0)
    cv2.imshow('mask',mask)
    cv2.moveWindow('mask',400,0)
    cv2.imshow('res',res)
    cv2.moveWindow('res',0,400)
    
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    cv2.destroyAllWindows