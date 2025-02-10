'''CV_21_Pyramids, Gaussian
Gaussian
THe best turorial of all===
https://automaticaddison.com/how-the-sobel-operator-works/

no exclusive function for laplacain pyramid.
A level of Laplacian Pyramid is formed by the 
difference between that level in the Gaussian pyramid and the 
"expanded version of its UPPER LEVEL in Gaussian Pyramid"
we have appended the images to the list 'layer'


'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('images/HappyFish.jpg')
layer = img.copy()
gp = [layer] 
# gp = [layer] # create gaussian pyramid LIST and the 1st element is the copy of the image!
# Interesting:len layer = 3 for range 2, if change ot 4, len is 13. For range =6  the len of layer is 4.
for i in range(6):#   for 5 it is len=7, for range 1, len is 97 !!!
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)  ## comment out so I can see the one gp[5] layer below    


# upper level of the gaussian pyramid
layer = gp[5]
cv2.imshow('upper level of gaussian pyramid', layer)
# now create the Laplacain pyramnid
lp = [layer]  # note the len of layer is 4, 
print('len of layer:',len(layer))
print('gp is : ',len(gp))  # note the len of gp is 7
for i in range(6,0,-1):  # extended level of upper version of upper level
    size = (gp[i - 1].shape[1], gp[i - 1].shape[0])
    gaussian_extended = cv2.pyrUp(gp[i], dstsize=size)
    
    
    # gaussian_extended = cv2.pyrUp(gp[i],dstsize = (gp[i - 1].shape[1], gp[i - 1].shape[0]))
    # gaussian_extended = cv2.pyrUp(gp[i])
    
    print(i)
    laplacian =cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian) 
# for i in range(5,0,-1):  # extended level of upper version of upper level
#     gaussian_extended = cv2.pyrUp(gp[i])
#     print(i)
#     laplacian =cv2.subtract(gp[i-1],gaussian_extended)
#     cv2.imshow(str(i),laplacian) 
    




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