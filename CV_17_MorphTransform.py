'''CV_17 Morphological Transformations
simple operatons based on shape.
a Kernel tells you how to change the value of a pixel by combininig it with the 
value of adjacent pixels


'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
from matplotlib import pyplot as plt

img = cv2.imread('images/smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
# the mask has 1st- the image, 2d arguemt is threshole, 3d is max, 4th is type of threshold
kernal = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernal,iterations =2)

erosion = cv2.erode(mask,kernal,iterations =1)

opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)


#  opening is first erosion followed by  dilation
titles = ['image','mask','dilation','erosion','opening']
images = [img,mask,dilation,erosion,opening]
'''
to get rid of the black dots, will use the dilation transformation. write dilation and use the c2 method(dilation). uses the source which is mask and then uses a kernal which is a shape we want to apply. 
Get an error until we define a kernel which we will define as a 2 by 2 square shape which we apply wherever the black dots are

'''




for i in range(5):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
# note!! do not use the cv2.waitkey when just reading and making plt images
# cv2.waitKey(0)
# cv2.destroyAllWindows    

    