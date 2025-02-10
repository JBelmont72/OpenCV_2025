'''CV_18 Smoothing Images
in image processing, a kernel , convolution matrix, or mask is a small matrix. It is used for blurring, embossing, sharpening,edge detection, and more.
can use numpy to create a kernal  kernal = 1/(k x k )
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
from matplotlib import pyplot as plt

# img = cv2.imread('images/smarties.png')
img = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/opencv-logo.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5),np.float32)/25
dst =cv2.filter2D(img,-1,kernal)
# define destiantion, a filter  1sr arguemnt is image, 2d arguement is desired depth of the destiantion image, and 3d arguemtn is the kernal
titles = ['img','2Dfilter']
images =[img,dst]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
# note!! do not use the cv2.waitkey when just reading and making plt images
# cv2.waitKey(0)
# cv2.destroyAllWindow