'''
setting camera properties
First is the basic and seocnd is the modification
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!
'''
import cv2
cap = cv2.VideoCapture(1)
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
'''output:  1920.0
    1080.0
    True
    True
    1280.0
    720.0
    Note that if i do not have a webcam hooked up, it takes a single image from the mac webcam
    Note if you enter a wrong value for width and height, it will self adjust to some corrent combination
'''
while(cap.isOpened()):
    ret,frame =cap.read()
    # if ret == True:
        
    #     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('myWebCam',gray)
        
    # if cv2.waitKey(1) & 0xFF == ord('c'): # if waitkey (1)just flashes on
    #     cap.release()
    #     cv2.destroyAllWindows #press any key with cursor on photo
    # else:
    #     break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('myWebCam',gray)
    if cv2.waitKey(1) & 0xFF == ord('c'): # if waitkey (1)just flashes on
        break
cap.release()
cv2.destroyAllWindows #press any key with cursor on photo