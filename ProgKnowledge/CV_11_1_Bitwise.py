'''CV_11_1.Bitwise.py


'''
import cv2
import numpy as np

img1= np.zeros((250,500,3),np.uint8)    #rows, columns
img2=cv2.rectangle(img1,(250,0),(500,250),(255,255,255),-1)# (x1,y1)  (x2,y2)
frame =np.zeros((250,500,3),np.uint8)
img3=cv2.rectangle(frame,(200,0),(300,125),(255,255,255),-1)

# bitAnd = cv2.bitwise_and(img2,img3)
# cv2.imshow('bitAnd',bitAnd)
# cv2.moveWindow('bitAnd',500,0)

# bitOr = cv2.bitwise_or(img2,img3)
# cv2.imshow('bitOr',bitOr)
# cv2.moveWindow('bitOr',500,0)

# bitXor = cv2.bitwise_xor(img2,img3)
# cv2.imshow('bitXor',bitXor)
# cv2.moveWindow('bitXor',500,0)


bitNot2 = cv2.bitwise_not(img2)
bitNot3 = cv2.bitwise_not(img3)
cv2.imshow('bitNot2',bitNot2)
cv2.moveWindow('bitNot2',500,0)
cv2.imshow('bitNot3',bitNot3)
cv2.moveWindow('bitNot3',500,250)




# cv2.imshow('Image',img2)
# cv2.moveWindow('Image',0,0)
# cv2.imshow('Image3',img3)
# cv2.moveWindow('Image3',0,300)
cv2.waitKey(0)
cv2.destroyAllWindows