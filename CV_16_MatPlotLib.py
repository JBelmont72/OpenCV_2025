'''
matplotlib.org

'''
import mediapipe
print(mediapipe.__version__)
import matplotlib
print(matplotlib.__version__)
import cv2
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
# img =cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/lena.jpg',-1)
# RBGimg =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow('Orig',img)
# cv2.moveWindow('Orig',0,400)

# cv2.imshow('image',RBGimg)
# plt.imshow(RBGimg)
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows

i =0
img = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/HikingSam.jpeg',cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image',img)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# cv2.moveWindow('image',0,400)

Jannie,threshold1 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
Jannie,threshold2 = cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
Jannie,threshold3 = cv2.threshold(img,125,255,cv2.THRESH_TRUNC)
Jannie,threshold4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
Jannie,threshold5 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)
# when  pixel value is less than the threshold, value is zero
titles = ['Original Image','BINARY','BINARY INVERSE','TRUNC','TO_ZERO','TO_ZERO_INV']
images =[img,threshold1,threshold2,threshold3,threshold4,threshold5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])




# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
# imag, max value, adaptive method (here is is adaptive thresh_mean_c  gives the mean of the blocksize times blocksize
#  fourth is the threshold type, and then a blocksize(11)(and try changing), c type
#   the c value is 2 not sure why
# the second available treshold  cv2.adapative_threshold_gaussian_c 
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




# plt.xticks([]),plt.xticks([])
# plt.yticks([]),plt.yticks([])
# cv2.imshow('image',RBGimg)
# plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows
