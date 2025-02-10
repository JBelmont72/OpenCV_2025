'''CV_20_CannyEdgeDetector.py

edge detection that uses a multi-stage algorithim to detect a wide range of images. 
Developed by John F. Canny 1986
1 noise reduction
2 gradient calculation
3.non -maximum suppression
4 double threshold
5 edge tracking by hysteresi

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/butterfly.jpg',0)
# img = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/butterfly.jpg',cv2.IMREAD_GRAYSCALE)
canny = cv2.Canny(img, 100,200)
#  1st threshold value   = 100,  2 d threshold  = 200 (later add TRACKBARS to adjust threshold
#       

titles= ['Image','Canny']
images = [img,canny]

for i in range(len(titles)):
    plt.subplot(1,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
                 
                
plt.show()

# note!! do not use the cv2.waitkey when just reading and making plt images
# cv2.waitKey(0)
# cv2.destroyAllWindow

