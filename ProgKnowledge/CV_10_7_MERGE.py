'''CV_10_7_Merge.py
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

www.fourcc.org/codecs.php   video codes by fourcc, compressed formats  that you see displayed when you don't have the right CODEC installed to play a given AVI file
https://gist.github.com/takuma7/44f9ecb028ff00e2132e this deals with fourcc codes for mac
also read about "HAP codec"
cv2.add(img,img2)
cv2.addWeighted(input array1, weight,img2, weight,gamma scalar value, distination, data type)
scalar is added to the image
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
width=640
height=360

# cam =cv2.VideoCapture(0)    # to access webcam
# # cam = cv2.VideoCapture('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/myQuicktime_1.mov')
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.MOV',fourcc,20.0, (640,480))
# print(cam.isOpened())
# print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(cam.get(cv2.CAP_PROP_FPS))
# print(cam.get(cv2.CAP_PROP_POS_FRAMES))


img = cv2.imread('images/starry_night.jpg')
img2 = cv2.imread('images/home.jpg')
print(img.shape)    #returns a tuple of number of rows, columns, and channels
print(img.size)     # returns Total number of pixels accessed
print(img.dtype)    # returns image dataType
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))        #Note the double brackets
# resize the images  use a Tuple

img = cv2.resize(img,(512,512))
img2 =cv2.resize(img2,(512,512))
# dist =cv2.addWeighted(img,.3,img2,.7, 0)
dist =cv2.addWeighted(img,.3,img2,.7, 0)
# dist =cv2.add(img,img2)
cv2.imshow('image',dist)
cv2.waitKey(0)
cv2.destroyAllWindows()