'''
if you don’t use a floating point data type when computing the gradient magnitude image, you will miss edges, specifically the white-to-black transitions.
In order to ensure you catch all edges, use a floating point data type, then take the absolute value of the gradient im- age and convert it back to an 8-bit unsigned integer, 
PyImage/Py10.1_Edge_Sobel.py
images/smarties.png
'''
import numpy as np
import argparse
import cv2
# 
image=cv2.imread('images/smarties.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)

cv2.imshow("Laplacian", lap)
cv2.waitKey(0)