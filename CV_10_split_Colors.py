import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
img=cv2.imread('images/lena.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
img[:,:,2]=0## this sets all the red pixels to 0 or any vlaue deired
img[:,:,0]=0## i left only green in the image
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##  https://www.tutorialspoint.com/how-to-split-an-image-into-different-color-channels-in-opencv-python
# import required libraries
import cv2
import numpy as np

# read the input color image
img = cv2.imread('images/lena.jpg',cv2.IMREAD_UNCHANGED)

# split the Blue, Green and Red color channels
blue,green,red = cv2.split(img)

# define channel having all zeros
zeros = np.zeros(blue.shape, np.uint8)

# merge zeros to make BGR image
blueBGR = cv2.merge([blue,zeros,zeros])
greenBGR = cv2.merge([zeros,green,zeros])
redBGR = cv2.merge([zeros,zeros,red])

# display the three Blue, Green, and Red channels as BGR image
cv2.imshow('Blue Channel', blueBGR)
cv2.waitKey(0)
cv2.imshow('Green Channel', greenBGR)
cv2.waitKey(0)
cv2.imshow('Red Channel', redBGR)
cv2.waitKey(0)
cv2.destroyAllWindows()