'''
setting date and time on frame
First is the basic and seocnd is the modification
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!
'''
import cv2
import datetime #new library

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cv2's code number fort width is 3 and height is 4
# Can use those code numbers in lieu of print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))such as in cap.set() method
# cap.set(3, 1280)
# cap.set(4, 720)
# print(cap.set(3,1280))
# print(cap.set(4,720))
# print(cap.get(3))
# print(cap.get(4))
'''output:  1920.0
    1080.0
    True
    True
    1280.0
    720.0
    Note that if i do not have a webcam hooked up, it takes a single image from the mac webcam
    Note if you enter a wrong value for width and height, it will self adjust to some corrent combination
'''
font =cv2.FONT_HERSHEY_SIMPLEX
fontScale = .5
thickness = 1
lineType = cv2.LINE_AA
while(cap.isOpened()):
    ret,frame =cap.read()
    if ret == True:
        text = 'Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        
        rectangle = cv2.rectangle(frame,(5,10),(550,55),(255,255,255),-1)
        dateTime = str(datetime.datetime.now()) # forgot the ()
        frame = cv2.putText(frame,dateTime + text,(10,50),font,fontScale,(255,0,0),thickness,lineType)
        
        cv2.imshow('myWebCam',frame)
        
    # if cv2.waitKey(0) & 0xFF == ord('c'): # if waitkey (1)just flashes on
    #     cap.release()
    #     cv2.destroyAllWindows #press any key with cursor on photo
    # else:
    #     break
    if cv2.waitKey(1)&0xFF==ord('c'):
        break
cap.release()
cv2.destroyAllWindows()