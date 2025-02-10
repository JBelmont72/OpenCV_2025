'''CV_9_1MouseAdvanced
ProgrammingKnowledge OpenCV Python video 8 MouseClick
THIS PROGRAM USES THE MOUSECLICK TO PLACE TWO SMALL POINTS AND CONNECT THE CIRCLES.
CREATES A LINE DRAWING-
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
# print(np.__version__)
# cap =cv2.VideoCapture(0)
# note we are accessing a LIST so used []
# this lists all the events available in CV2
# dir is an in-built method  to show the 'events' methods(or any other keyWord) for mouse, 'EVENT' is the keyword

# events = [ i for i in dir(cv2)if 'EVENT' in i]
# print(events)
# callback function 'listens' for mouseclick and the setMouseCLick method 'calls' the callback function!!
def click_event(event,x,y,flags,params):
    # cv2.circle(img,(x,y),10,(255,255,255),-1)  ##in this positon circles are drawn along the entire route of the cursor/mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,255,255),-1)        
        points.append((x,y)) # (need a tuple, otherwise+++) TypeError: list.append() takes exactly one argument (2 given)
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(255,0,0),3)
        cv2.imshow('image',img) # in this poistion connects all the points
    #cv2.imshow('image',img)    
img = cv2.imread('images/lena.jpg',1)
cv2.imshow('image',img)
points =[]
cv2.setMouseCallback('image',click_event) 
cv2.waitKey(0)
cv2.destroyAllWindows()      
    






# create a mouseclick callback function
# arguements are 1. the event, x pos, y pos, flags, params
# font = cv2.FONT_HERSHEY_SIMPLEX
# def click_event1(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         print(x,' , ',y)
#         text = str(x)+' , '+str(y)
#         cv2.putText(frame,text,(x,y),font,1,(255,255,0),2)
#         cv2.imshow('image',frame)
#     if event  == cv2.EVENT_RBUTTONUP:
#         blue  =  frame[y,x,0]       #the bgr channel printout, note the []
#         green =  frame[y,x,1]
#         red   =  frame[y,x,2]
#         font  =  cv2.FONT_HERSHEY_SIMPLEX
#         strBGR=  str(blue)+ ' , '+str(green)+ ' , '+str(red)
#         cv2.putText(frame,strBGR,(x,y-30),font,1,(0,255,255),1)
#         cv2.imshow('image',frame)
          
        
        
# def click_event2(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONUP:
#         print('LButtonUP: x- ',x,'y- ',y)
#         text2= str(x)+' ,' +str(y)
#         cv2.putText(frame,text2,(x,y),font,1,(0,0,255),2)       
#         cv2.imshow('image',frame)
# while True:
# frame = np.zeros((512,512,3),np.uint8 )
# img = cv2.imread('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/lena.jpg',1)
# cv2.imshow('image',img)
# points =[]
# cv2.setMouseCallback('image',click_event) 
# cv2.waitKey(0)
# cv2.destroyAllWindows()      







# while(cap.isOpened()):
#     ret,frame =cap.read()
#     if ret == True:
        
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('myWebCam',gray)
        
    # if cv2.waitKey(0) & 0xFF == ord('c'): # if waitkey (1)just flashes on
    #     cap.release()
    #     cv2.destroyAllWindows #press any key with cursor on photo
    # else:
    #     break       