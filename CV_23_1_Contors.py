


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/shapes.jpg')
# img = cv2.imread('images/opencv-logo.png')
imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh =cv2.threshold(imgGray,100,255,0)
# contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print('Number of contours = '+str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,2,(0,255,0),3)
cv2.imshow('image',img)
cv2.imshow('imageGray',imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()