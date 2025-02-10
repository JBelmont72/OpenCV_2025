'''CV_15_1 Adaptive Thresholding
 threshold method takes values:1st source (img)
        threshold value 2d min(the threshold)  127, 3d  max 255, 4th threshold type which here is cv2.threshold_BINARY)
https://www.pngegg.com/en/search?q=gradient
source of many gradients

in simple thresholding we are setting global thresholds.
Adoptinve thresholding is where the threshold is calculated for amaller regions. thus different values for different regions
Necessary where the lighting conditions are different in portions of picture/image. Gives better results for images with different illumination
Explanation with examples: good
https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html

'''
import cv2 
import numpy as np


img = cv2.imread('images/sudoku.png',0)
_,th1 = cv2.threshold(img, 150,255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#####   or
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow("Image", img)
cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()










# # img = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/sudoku.png',0)
# # the _ is the ret value , whatever is returned

# Jannie,threshold1 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
# Jannie,threshold2 = cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
# Jannie,threshold3 = cv2.threshold(img,125,255,cv2.THRESH_TRUNC)
# Jannie,threshold4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
# Jannie,threshold5 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)
# # # when  pixel value is less than the threshold, value is zero

# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
# # ##imag, max value, adaptive method (here is is adaptive thresh_mean_c  gives the mean of the blocksize times blocksize
# # ## fourth is the threshold type, and then a blocksize(11)(and try changing), c type
# # ##  the c value is 2 not sure why
# # ##the second available treshold  cv2.adapative_threshold_gaussian_c
 
# cv2.imshow('Image',img)
# cv2.imshow('th2',th2)
# cv2.moveWindow('th2',400,0)

# cv2.imshow('th3',th3)
# cv2.moveWindow('th2',800,0)
# cv2.imshow('Threshold1',threshold1)
# cv2.imshow('Threshold2',threshold2)
# cv2.imshow('Truncated',threshold3)
# cv2.imshow('ThreshToZero',threshold4)
# cv2.moveWindow('Image',0,0)
# cv2.moveWindow('Threshold1',400,0)
# cv2.moveWindow('Threshold2',800,0)
# cv2.moveWindow('Truncated',0,500)
# cv2.moveWindow('ThreshToZero',400,500)
# cv2.waitKey(0) 

# cv2.destroyAllWindows
