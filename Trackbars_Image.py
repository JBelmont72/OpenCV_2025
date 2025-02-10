'''Trackbars on image for image, goo demo
Akshit Madan
https://www.youtube.com/watch?v=xVyvw5chbUU
'''
import cv2
import numpy as np
print(cv2.getBuildInformation())
img = np.zeros((512,512,3),np.uint8)
img1 = cv2.imread(' image path  ')
img1 =cv2.resize(img1,(512,512))
img = img1[0:, :]
img = img1[0:256, :]
# img = img1[0:256, :]
def passfunction():
    pass
cv2.namedWindow('trackbar')
cv2.createTrackbar('B','trackbar',0,255, passfunction)
cv2.createTrackbar('G','trackbar',0,255, passfunction)
cv2.createTrackbar('R','trackbar',0,255, passfunction)
cv2.createTrackbar('xPos','trackbar',256,512, passfunction)
cv2.createTrackbar('yPos','trackbar',256,512, passfunction)
# cv2.createTrackbar('B','trackbar',0,255, passfunction)

while True:
    cv2.imshow('image',img)
    cv2.imshow('img_1',img1)
    button = cv2.waitKey(1) & 0xff
    if button == ord('q'):
        break
    b = cv2.getTrackbarPos('B','trackbar')
    g = cv2.getTrackbarPos('G','trackbar')
    r = cv2.getTrackbarPos('R','trackbar')
    xPos = cv2.getTrackbarPos('xPos','trackbar')
    yPos = cv2.getTrackbarPos('yPos','trackbar')
    
    img[:] = [b,g,r]
    cv2.circle(img,(xPos,yPos),25,(127,127,0),3)
cv2.destroyAllWindows()