'''THis is an amalgamation of CV_10_3 where a ROI is found with mouseclicks and then used to move the ROI into the photo

AI for everyone Lesson 11 and Lesson 11 Homework is a nice review 
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

www.fourcc.org/codecs.php   video codes by fourcc, compressed formats  that you see displayed when you don't have the right CODEC installed to play a given AVI file
https://gist.github.com/takuma7/44f9ecb028ff00e2132e this deals with fourcc codes for mac
also read about "HAP codec"

'''

# import sys
# import cv2
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)

'''
width=640
height=360
evt =0
Radius =10
Thickness = 2
Color = [255,255,0]
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt1
    global pnt2
    if event ==cv2.EVENT_LBUTTONDOWN:
        print('Event Left Down = ',event)
        print('xPos: ',xPos,' yPos ',yPos)
        pnt1=(xPos,yPos)
        evt = event
    if event ==cv2.EVENT_LBUTTONUP:
        print('Event Left Up = ',event)
        print('xPos: ',xPos,' yPos ',yPos)
        pnt2=(xPos,yPos)
        evt = event
    if event ==cv2.EVENT_RBUTTONUP:
        print('Event Right Up = ',event)
        print('xPos: ',xPos,' yPos ',yPos)
        
        evt = event
        
cam =cv2.VideoCapture(0)    # to access webcam
# cam = cv2.VideoCapture('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/myQuicktime_1.mov')
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.MOV',fourcc,20.0, (640,480))
print(cam.isOpened())
print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cam.get(cv2.CAP_PROP_FPS))
print(cam.get(cv2.CAP_PROP_POS_FRAMES))
cv2.namedWindow('my Webcam')
cv2.setMouseCallback('my Webcam',mouseClick)
while(cam.isOpened()):
# while True:     #if true then the first arguement (ret) is true and the frame is captured
    ret,frame =cam.read()
    # out.write(frame)
    if evt ==  4:
        cv2.rectangle(frame,pnt1,pnt2,(255,0,255),Thickness)
        cv2.circle(frame,pnt1,Radius,Color,Thickness,cv2.LINE_AA)
        ROI =frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
        try:
            cv2.imshow('ROI',ROI)
            cv2.moveWindow('ROI',int(width*1.2),0)
        except:
            pass
    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if evt == 5:
        cv2.destroyWindow('ROI')
        evt = 0    
    
    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('c'):
        break
cam.release()
# out.release()
cv2.destroyAllWindows()
    
'''
# import sys
# import cv2
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)
# img=cv2.imread('images/lena.jpg')
# assert img is not None, "file could not be read, check with os.path.exists()"
# b,g,r =cv2.split(img)
# zeros=np.zeros(b.shape,dtype=np.uint8)
# print(zeros.shape)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# BlueImg=cv2.merge([b,zeros,zeros])
# cv2.imshow('Blueimg' , BlueImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# GreenImg=cv2.merge([zeros,g,zeros])
# cv2.imshow('Greenimg' , GreenImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# RedImg=cv2.merge([zeros,zeros,r])
# cv2.imshow('Redimg' , RedImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
image=cv2.imread('images/lena.jpg',cv2.IMREAD_COLOR)
while True:
    print(image.shape)
    cv2.imshow('image',image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    x=np.zeros([image.shape[0],image.shape[1],1],dtype=np.uint8)
    print(x.shape)
    # cv2.imshow('x',x)
    # cv2.waitKey(0)
    b,g,r=cv2.split(image)
    imageB=cv2.merge([b,g,x])
    cv2.imshow('imageB',imageB)
    # cv2.waitKey(0)
    cv2.imshow('x',x)
    cv2.moveWindow('x',500,0)


    if cv2.waitKey(1)& 0xff==ord('c'):
        break

cv2.destroyAllWindows()