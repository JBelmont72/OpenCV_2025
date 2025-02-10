'''
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

www.fourcc.org/codecs.php   video codes by fourcc, compressed formats  that you see displayed when you don't have the right CODEC installed to play a given AVI file
https://gist.github.com/takuma7/44f9ecb028ff00e2132e this deals with fourcc codes for mac
also read about "HAP codec"

'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
width=640
height=360
cam =cv2.VideoCapture(1)    # to access webcam
# cam = cv2.VideoCapture('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/myQuicktime_1.mov')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.MOV',fourcc,20.0, (640,480))
print(cam.isOpened())
print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cam.get(cv2.CAP_PROP_FPS))
print(cam.get(cv2.CAP_PROP_POS_FRAMES))
while(cam.isOpened()):
# while True:     #if true then the first arguement (ret) is true and the frame is captured
    ret,frame =cam.read()
    # out.write(frame)
   
    
    
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frameGray)
    
    if cv2.waitKey(1) & 0xff ==ord('c'):
        break
cam.release()
# out.release()
cv2.destroyAllWindows()
    
    