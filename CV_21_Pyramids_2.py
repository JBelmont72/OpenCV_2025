'''
the best tutorial explaining kernels  and the Sorbel Operator
https://automaticaddison.com/how-the-sobel-operator-works/
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('images/butterfly.jpg')
layer = img.copy()
gp = [layer] # create gaussian pyramid array

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

# pyr_d_1 = cv2.pyrDown(img)
# pyr_d_2 = cv2.pyrDown(pyr_d_1)
# hr =cv2.pyrUp(pyr_d_2)
# pyr_d = cv2.pyrDown(img)
# pyr_d = cv2.pyrDown(img)
# pyr_d = cv2.pyrDown(img)
# cv2.imshow('pyrDown_1',pyr_d_1)
# cv2.imshow('pyrDown_2',pyr_d_2)
cv2.imshow('Original Image',img)
# cv2.imshow('pyrUp',hr)

cv2.waitKey(0)
cv2.destroyAllWindows()