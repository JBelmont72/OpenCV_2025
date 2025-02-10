'''CV_9_2_Mouse.py
ProgrammingKnowledge OpenCV Python video 8 MouseClick
THIS PROGRAM USES THE MOUSECLICK TO DREATE A NEW IMAGE THAT IS ALL THE COLOR OF THE VALUES x,y[]
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

www.fourcc.org/codecs.php   video codes by fourcc, compressed formats  that you see displayed when you don't have the right CODEC installed to play a given AVI file
color picker    https://math.hws.edu/graphicsbook/demos/c2/rgb-hsv.html
https://colorpicker.me/#ca64b6
lena.jpg is 500 x 500
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
# cap =cv2.VideoCapture(0)
# note we are accessing a LIST so used []
# this lists all the events available in CV2
# dir is an in-built method  to show the 'events' methods(or any other keyWord) for mouse, 'EVENT' is the keyword

# events = [ i for i in dir(cv2)if 'EVENT' in i]
# print(events)
# callback function 'listens' for mouseclick and the setMouseCLick method 'calls' the callback function!!
def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue  = img[x,y,0]
        green = img[x,y,1]
        red   = img[x,y,2]
        text ='Blue: '+str(blue)+' Green: '+str(green)+' Red: '+str(red)
        cv2.circle(img,(x,y),10,(255,255,0),3,cv2.LINE_AA)
        myColorImage = np.zeros((256,256,3),np.uint8)
        myColorImage[:,:]=[blue,green,red] # this gives the color of where the click was
        cv2.imshow('myColorImage',myColorImage)
        cv2.moveWindow('myColorImage',0,500)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255),2)
        cv2.imshow('image',img) # in this poistion connects all the points
   
img = cv2.imread('images/lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event) 
cv2.waitKey(0)
cv2.destroyAllWindows()      
    
