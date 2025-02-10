'''
oad our image, convert it to graysc- ale, and blur it using the Gaussian blurring method. By ap- plying a blur prior to edge detection, we will help remove
“noisy” edges in the image that are not of interest to us. Our goal here is to find only the outlines of the coins.
Canny involves blurring the image to remove noise, computing Sobel gradi- ent images in the x and y direction, suppressing edges, and finally a hysteresis thresholding stage that determines if a pixel is “edge-like” or not.
'''
import numpy as np
import argparse
import cv2
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True,
# help = "Path to the image")
# args = vars(ap.parse_args())
# image = cv2.imread(args["image"])
image= cv2.imread('images/smarties.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
