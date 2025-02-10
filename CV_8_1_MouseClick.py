'''ProgrammingKnowledge OpenCV Python video 8 MouseClick
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

www.fourcc.org/codecs.php   video codes by fourcc, compressed formats  that you see displayed when you don't have the right CODEC installed to play a given AVI file
color picker    https://math.hws.edu/graphicsbook/demos/c2/rgb-hsv.html
https://colorpicker.me/#ca64b6
lena.jpg is 500 x 500
macOS does not have a built-in middle click option for the Magic Mouse, but you can use the Command-left click shortcut to simulate a middle-click action
'''
# import sys
import cv2
# import math
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)

# note we are accessing a LIST so used []
# this lists all the events available in CV2
# dir is an in-built method  to show the 'events' methods(or any other keyWord) for mouse, 'EVENT' is the keyword
### practiced list comprehension below 
## x=[expression  for item in iterable if condition]
# iter=[1,2,3,4,5,6,7,8,9,10]
# x=[item*4**2 for item in (iter) if item%2==0]
# print(x)
events = [ i for i in dir(cv2)if 'EVENT' in i]
print(events)
# font =[i for i in dir(cv2)if 'COLOR' in i]
# for j in font:
#     print(j)
# myList=['11',22,'33',44]
# my=[int(i)**2 for i in list(myList) if i in myList]
# print(my)
# mySqrt=[math.sqrt(int(i))for i in myList if i in myList]
# print(mySqrt)

# myset=[11,'33',44,'55']
# mynewSqrt=[(math.sqrt(int(i))*math.sqrt(int(i))+1)<40 for i in (myset) if i in myset]
# print(mynewSqrt)
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
# def click_event2(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONUP:
#         print('LButtonUP: x- ',x,'y- ',y)
#         text2= str(x)+' ,' +str(y)
#         cv2.putText(frame,text2,(x,y),font,1,(0,0,255),2)       
#         cv2.imshow('image',frame)

# frame = np.zeros((512,512,3),np.uint8 )
# cv2.imshow('image',frame)
# cv2.setMouseCallback('image',click_event1) 
# cv2.setMouseCallback('image',click_event2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()  
 

#########~~~~~3 Jan 2025 I have made progress with making a drawing program!! 
import sys
import cv2
import math
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
mode=True

cap =cv2.VideoCapture(0) 
evt=0 
font = cv2.FONT_HERSHEY_SIMPLEX
def click_event1(event,x,y,flags,param):
    global evt
    global pnt1
    global pnt2
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        print(f'LButtonDOWN:x- {x} y- {y}')
        text = str(x)+' , '+str(y)
        # cv2.putText(frame,text,(x,y),font,1,(255,255,0),2)
        # cv2.imshow('image',frame)
        pnt1=(x,y)
        evt =event
    if event == cv2.EVENT_LBUTTONUP:
        print('LButtonUP: x- ',x,'y- ',y)
        text2= str(x)+' ,' +str(y)
        # cv2.putText(frame,text2,(x,y),font,1,(0,0,255),2)       
        # cv2.imshow('image',frame)
        pnt2=(x,y)
        evt=event
    if event==cv2.EVENT_RBUTTONUP:       
        evt=event
        print(f'event is RightButUP = : {evt}')
# frame = np.zeros((512,512,3),np.uint8 )
# cv2.imshow('image',frame)
cv2.namedWindow('image')
cv2.setMouseCallback('image',click_event1)   
while(cap.isOpened()):
    ret,frame =cap.read()
    if  evt==4  and mode == True:
        cv2.rectangle(frame,(int(pnt1[0]+20),pnt1[1]),pnt2,(255,0,0),2,cv2.LINE_4)
        cv2.imshow('image',frame) 
    if evt==4 and mode == False :
        cv2.circle(frame,pnt2,15,(0,0,255),2)
        cv2.rectangle(frame,pnt1,pnt2,(0,0,255),2,cv2.LINE_4)
        cv2.imshow('image',frame)
    if  evt==1 and mode==False:
        cv2.circle(frame,pnt1,25,(0,255,0),3)
        blue=frame[pnt1[1],pnt1[0],0]
        green=frame[pnt1[1],pnt1[0],1]
        red=frame[pnt1[1],pnt1[0],2]
        COLOR=str(blue)+' '+str(green)+'  '+str(red)
        print(blue)
        cv2.putText(frame,COLOR,pnt1,cv2.FONT_HERSHEY_DUPLEX,1,(255,255,0),2,cv2.LINE_AA)
        cv2.imshow('image',frame)
    if evt==5:
        evt=0
    cv2.imshow('image',frame)
      
    # if cv2.waitKey(1) & 0xFF == ord('c'): # if waitkey (1)just flashes on
    #     break
    k=cv2.waitKey(1) & 0xFF  # if waitkey (1)just flashes on
    if k==ord('c'):
        break   
    # elif k==ord('q'):
    #     print('ord is q')
    #     mode ==True
    #     print(mode)
    elif k==ord('f'):
        print('ord is FFFFFFFFF')
        mode = not mode
        print(mode)
cap.release()
cv2.destroyAllWindows      