'''Thresholding/ PyProgramming
https://pythonprogramming.net/thresholding-image-analysis-python-opencv-tutorial/

HOW to get frame size of image
https://note.nkmk.me/en/python-opencv-pillow-image-size/
class numpy.ndarray
(342,548,3)
width = 548
height = 342
channel = 3

h, w = img_gray.shape
print('width: ', w)
print('height:', h)
# width:  400
# height: 225

print('width: ', img_gray.shape[1])
print('height:', img_gray.shape[0])
# width:  400
# height: 225




'''
import cv2
import numpy as np



x=0
def myCallback1(x):
    global thresh
    print(x)
    thresh = x
def myCallback2(x):
    global gausThresh
    print(x)
    if x%2 ==0:
        x=x+1
    gausThresh = x
def myCallback3(x):
    global OtsuThresh
    print(x)
    if x%2 ==0:
        x=x+1
    OtsuThresh = x
   

cv2.namedWindow('Trackbars')
cv2.createTrackbar('threshold','Trackbars',50,254,myCallback1)
cv2.createTrackbar('gausThresh','Trackbars',51,254,myCallback2)
cv2.createTrackbar('OtsuThreshold','Trackbars',51,254,myCallback3)
# img = cv2.imread('images/gradient.png',cv2.IMREAD_UNCHANGED)
# img = cv2.imread('images/messi5.jpg',cv2.IMREAD_UNCHANGED)
img = cv2.imread('images/messi5.jpg',cv2.IMREAD_UNCHANGED)
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
print(type(img.shape))
# (225, 400, 3)
# <class 'tuple'>
# print("Frame width: ",width,
#       '\n\t Frame height',height)

while True:
    print(type(img))
# <class 'numpy.ndarray'>

    print(img.shape)
    print(type(img.shape))
# (225, 400, 3)
    h, w, c = img.shape
    print('width:  ', w)
    print('height: ', h)
    print('channel:', c)
# width:   400
# height:  225
# channel: 3
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(grayscaled, thresh, 255, cv2.THRESH_BINARY)  
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, gausThresh, 1)
    retval2,threshold2 = cv2.threshold(grayscaled,OtsuThresh,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    cv2.imshow('OtsuThreshold',threshold2)
    
    
    print('x: ',thresh)
    cv2.imshow('original',img)
    cv2.imshow('threshold',threshold)
    cv2.imshow('thresh_adapive_Gaus', th)
        
    if cv2.waitKey(1) & 0xff ==ord('c'):
        break

cv2.destroyAllWindows()
    

