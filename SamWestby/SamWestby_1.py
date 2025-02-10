'''
Sam Westby Tech
here  also made a copy of the gray image. note the realative path in the imWrite('path', gray_cat)
'''
import cv2
import numpy as np


img = cv2.imread('images/Cat.jpeg',cv2.IMREAD_UNCHANGED)
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
print(img.size)
print(img.dtype)
print(img[0,0])
# img = img*2
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img[i,j]= max(254,img[i,j]*2.4)
cv2.imshow('Cat',img)
cv2.imshow('Gray Cat',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite('images/GrayCat.jpeg',gray_img)
# cap = cv2.VideoCapture(0)

# if cap.isOpened
