import matplotlib.pyplot as plt
import numpy as np
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
from matplotlib import pyplot as plt
lowerVal =150
val=20

# img = cv2.imread('images/smarties.png',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/smarties.png',cv2.IMREAD_COLOR)
cv2.namedWindow('mask')
# mask = cv2.threshold(img,lowerVal,255,cv2.THRESH_BINARY_INV)
def myCallBack1(val):
    print('lowerVal',val)
    _,mask  =cv2.threshold(img,val,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('Mask',mask)
    kernal = np.ones((2,2),np.uint8)
    dilation = cv2.dilate(mask,kernal,iterations =2)
    cv2.imshow('Dilation',dilation)
    erosion = cv2.erode(mask,kernal,iterations =1)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
    mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
    tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)


#     titles = ['image','mask','dilation','erosion','opening','closing']
#     images = [img,mask,dilation,erosion,opening,closing]
# # img = cv2.imread('images/smarties.png',cv2.IMREAD_GRAYSCALE)
#     # cv2.imshow('Mask',mask)
#     for i in range(6):
#         plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
#         plt.title(titles[i])
#         plt.xticks([]),plt.yticks([])
cv2.namedWindow('My Trackbars')
cv2.createTrackbar('lowerVal','My Trackbars',30,255,myCallBack1)



# _,mask = cv2.threshold(img,lowerVal,255,cv2.THRESH_BINARY_INV)
# the mask has 1st- the image, 2d arguemt is threshole, 3d is max, 4th is type of threshold
# kernal = np.ones((2,2),np.uint8)
# dilation = cv2.dilate(mask,kernal,iterations =2)

# erosion = cv2.erode(mask,kernal,iterations =1)

# opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
# closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
# mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
# tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)


# # opening is first erosion followed by  dilation
# titles = ['image','mask','dilation','erosion','opening']
# images = [img,mask,dilation,erosion,opening]
'''
to get rid of the black dots, will use the dilation transformation. write dilation and use the c2 method(dilation). uses the source which is mask and then uses a kernal which is a shape we want to apply. 
Get an error until we define a kernel which we will define as a 2 by 2 square shape which we apply wherever the black dots are

'''



# cv2.imshow('Mask',mask)
# for i in range(5):
#     plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# cv2.imshow('Image',img)    
plt.show()
myCallBack1(val)
# note!! do not use the cv2.waitkey when just reading and making plt images
cv2.waitKey(0)
cv2.destroyAllWindows  


## https://stackoverflow.com/questions/69826191/python-opencv-parse-progress-bar
'''

import cv2
import numpy as np


def parse_hp(hp_area):
    width = int(hp_area.shape[1] * 5)
    height = int(hp_area.shape[0] * 5)
    dim = (width, height)

    # resize image
    resized = cv2.resize(hp_area, dim, interpolation=cv2.INTER_AREA)
    # Color segmentation
    hsv = cv2.cvtColor(resized, cv2.COLOR_RGB2HSV)
    lower_red = np.array([120, 170, 0])
    upper_red = np.array([245, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(resized, resized, mask=mask)

    # Contour exctraction
    imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(imgray, (5, 5), 0)
    ret, thresholded = cv2.threshold(blurred, 50, 255, 0)
    contours, h = cv2.findContours(thresholded, 1, 2)

    if contours:
        cnt = contours[0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if cv2.contourArea(cnt) > 25:  # to discard noise from the color segmentation
            contour_poly = cv2.approxPolyDP(cnt, 3, True)
            center, radius = cv2.minEnclosingCircle(contour_poly)

            cv2.circle(resized, (int(center[0]), int(center[1])), int(radius), (0, 255, 0), 2)
            cv2.imshow("Found limits", resized)
            cv2.waitKey(0)

            resized_width = int(resized.shape[1])
            hp_width = radius * 2

            return int(hp_width * 100 / resized_width)
    else:
        return -1


if __name__ == "__main__":
    hp_area = cv2.imread("Cv2NotWorking.png")
    result = parse_hp(hp_area)
    print(result)


'''  
