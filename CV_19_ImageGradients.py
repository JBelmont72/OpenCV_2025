'''CV_19  Images Gradients
in image processing, a kernel , convolution matrix, or mask is a small matrix. It is used for blurring, embossing, sharpening,edge detection, and more.
can use numpy to create a kernal  kernal = 1/(k x k )

an image gradient is a directional chnge in the intensity or color of an image
several Methods  use different mathematical methods. the functions for finding the gfradients which we will use to analyze
the Laplacian method SHOWS the EDGES


'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
from matplotlib import pyplot as plt

# img = cv2.imread('images/smarties.png')

# very IMPRESSIVE DIFFERENCES WHEN I VIEW THE BUTTERFLY.JPG
img = cv2.imread('images/butterfly.jpg',cv2.IMREAD_GRAYSCALE)
# lap =cv2.Laplacian(img,cv2.CV_64F)
lap =cv2.Laplacian(img,cv2.CV_64F,ksize=1) # can use different values
# lap =cv2.Laplacian(img,cv2.CV_64F)
# using a 64 bit data type which supports negative numbers
# will now convert back to 8 bit
lap =np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img,cv2.CV_64F, 1, 0)    # can apply a kernal size as a 5th arguement if desired
sobely = cv2.Sobel(img,cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobely = np.uint8(np.absolute(sobely))
canny = cv2.Canny(img, 100,200)
#  1st threshold value   = 100,  2 d threshold  = 200 (later add TRACKBARS to adjust threshold
#       

titles = ['img','Laplacian','sobelX','sobelY','canny']
images =[img,lap,sobelX,sobely,canny]
for i in range(len(titles)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
# note!! do not use the cv2.waitkey when just reading and making plt images
# cv2.waitKey(0)
# cv2.destroyAllWindow