'''
img.shape[0] is height! Remember that img.shape is not a cv2.function
CV2.fx    columns ( the x) is first
when prints in terminal order is Rows(y), Columns(x), value 1 or 3 array(tuple)
img.shape gives rows and columns, so img.shape(0 is the height(rows) and img(shape(1 is width the x)))
'''

import cv2
import numpy as np

img = cv2.imread("images/Cat.jpeg", cv2.IMREAD_COLOR)
print(img.shape)
print(img.size)
print(img.dtype)
print(img[0,0])

# RESIZE
## in resize the first # is the x width, 2d is the height, When you print the array is is rows, then columns
# img = cv2.resize(img, (50, 250))# 1st is columns(x) the width and 2nd  is height(y) the rowss
#  # (250, 50, 3)  the img[0]is width,columns but prints out the array value as width,height,pixel numberof values



img = cv2.resize(img,(400,400))
# img = cv2.resize(img, (0, 0), fx=1.5, fy=1)
#  output (924, 1244, 3)
# 3448368
# uint8
# [43 53 41]
# img = cv2.resize(img,(int(img.shape[0]/2),img.shape[0]))# xvalue then y(N.B. y is height is img.shape[0])
# img = cv2.resize(img,(100,1000))# xvalue then y
# img = cv2.resize(img,(1000,250))
print(img.shape)
print('shape[0] : ',img.shape[0])
print(img.size)
print(img.dtype)
print('😅')
# img2 = img[0:250,:]
# cv2.imshow('image 2',img2)
# # CROP
# height, width = img.shape[0], img.shape[1]
height, width = img.shape[0], img.shape[1]
# the next trwo are the same upper left corner of img
# img1 = img[ : int(height/2),int(width/2):]
# img2 = img[  :int(img.shape[0]/2),int(img.shape[1]/2):]

# img1 = img[ int(height/2): , 50 : ] # gives bottom left quadrant
# img = img[int(height/3) : , 50 : -50]

# # ROTATE
# height, width = img.shape[0], img.shape[1]
# img = cv2.rotate(img, cv2.ROTATE_180)
# 

M = cv2.getRotationMatrix2D(center=(width/2, height/2), 
                            angle=150, scale=1)
img = cv2.warpAffine(img, M, (width, height))

# TRANSLATE
tx = width / 5
ty = height /5
# translation matrix
M = np.array([
    [1, 0, tx],
    [0, 1, ty]
])
img = cv2.warpAffine(img, M, (width, height))

cv2.imshow("Cat!", img)
# cv2.imshow("Cat_mod!", img1)
# cv2.imshow("Cat_mod!!", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("/images/man_Cat.jpeg", img)