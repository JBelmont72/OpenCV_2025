'''cv_14.py Thresholding
 threshold method takes values:1st source (img)
        threshold value 2d min(the threshold)  127, 3d  max 255, 4th threshold type which here is cv2.threshold_BINARY)
https://www.pngegg.com/en/search?q=gradient
source of many gradients
'''
import cv2 
import numpy as np

img = cv2.imread('images/Judson.jpg',1)
# the _ is the ret value , whatever is returned
Jannie,threshold1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
Jannie,threshold2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
Jannie,threshold3 = cv2.threshold(img,125,255,cv2.THRESH_TRUNC)
Jannie,threshold4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
# when  pixel value is less than the threshold, value is zero
cv2.imshow('Image',img)
cv2.imshow('Threshold1',threshold1)
cv2.imshow('Threshold2',threshold2)
cv2.imshow('Truncated',threshold3)
cv2.imshow('ThreshToZero',threshold4)
cv2.moveWindow('Image',0,0)
cv2.moveWindow('Threshold1',400,0)
cv2.moveWindow('Threshold2',800,0)
cv2.moveWindow('Truncated',0,500)
cv2.moveWindow('ThreshToZero',400,500)
cv2.waitKey(0)
cv2.destroyAllWindows
