'''ProgrammingKnowledge OpenCV Python video 5 Geometric Shapes
Similar to lesson 8 of PW AI for everyone
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

www.fourcc.org/codecs.php   video codes by fourcc, compressed formats  that you see displayed when you don't have the right CODEC installed to play a given AVI file
color picker    https://math.hws.edu/graphicsbook/demos/c2/rgb-hsv.html
https://colorpicker.me/#ca64b6
lena.jpg is 500 x 500
first is a numpy array and second is drawing on a webcam
'''
# import sys
# import cv2
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)

# width=640
# height=360
# thickness = 5
# fontH = 2
# fontThickness = 4
# image = np.zeros([512,512,3],np.uint8)
# # image = cv2.imread('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/lena.jpg',1)
# while True:     #if true then the first arguement (ret) is true and the frame is captured
    
#     imageBGR =cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
#     image1 = cv2.line(image,(0,0),(255,255),(255,0,0),thickness,4)
#     image2 = cv2.line(image,(300,255),(500,0),(182,100,202),thickness,4)
#     image3 = cv2.arrowedLine(image,(0,300),(200,300),(125,125,0),thickness,6)
#     image4 =cv2.rectangle(image,(255,255),(325,325),(0,0,255),7)
#     image5 =cv2.rectangle(image,(400,0),(510,500),(0,0,255),7)
#     image6 =cv2.circle(image,(250,250),25,(125,125,0),4)
#     image7 =cv2.putText(image,'This is fun!',(20,400),cv2.FONT_HERSHEY_TRIPLEX,fontH,(255,255,255),fontThickness,cv2.LINE_4)
#     cv2.imshow('image',image)
    
#     if cv2.waitKey(1) & 0xff ==ord('c'):
#         break

# cv2.destroyAllWindows()
# cap.set(3, 1280)
# cap.set(4, 720)
# print(cap.set(3,1280))
# print(cap.set(4,720))
# print(cap.get(3))
# print(cap.get(4))

import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
cam=cv2.VideoCapture(0)
width=1280
height=720
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
print(cam.get(3),' x ',cam.get(4))

thickness = 5
fontH = 2
fontThickness = 4
# imageBGR = np.zeros([512,512,3],np.uint8)
# image = cv2.imread('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/lena.jpg',1)
while True:     #if true then the first arguement (ret) is true and the frame is captured
    ret,image=cam.read()
    print(image.shape)
    # imageBGR[:,:]=(255,0,0)
    # imageBGR =cv2.cvtColor(imageBGR,cv2.COLOR_BGR2RGB)
    image1 = cv2.line(image,(0,0),(int(.5*width),int(0.25*height)),(255,0,0),thickness,4)
    image2 = cv2.line(image,(300,255),(500,0),(182,100,202),thickness,4)
    image3 = cv2.arrowedLine(image,(0,300),(200,300),(125,125,0),thickness,6)
    image4 =cv2.rectangle(image,(255,255),(325,325),(0,0,255),7)
    image5 =cv2.rectangle(image,(400,0),(510,500),(0,0,255),7)
    image6 =cv2.circle(image,(250,250),25,(125,125,0),4)
    image7 =cv2.putText(image,'This is fun!',(20,400),cv2.FONT_HERSHEY_TRIPLEX,fontH,(255,255,255),fontThickness,cv2.LINE_4)
    cv2.imshow('image',image)
    # cv2.imshow('BGR Image',imageBGR)
    if cv2.waitKey(1) & 0xff ==ord('c'):
        break
cam.release()
cv2.destroyAllWindows()
    
 