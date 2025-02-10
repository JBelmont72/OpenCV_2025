'''Morphological operations are a set of operations that process images based on shapes. They apply a structuring element to an input image and generate an output image. 
The most basic morphological operations are two: Erosion and Dilation 
 In ghis program I tried erosion, dilation and a combination. Erosion 'diminishes' the features of the objects.
 As stated below, a pixel is only considered 1 if all the pisxels in the kerenl are i. You might think that the dark balls woud be smaller but the background is white and this the background is smaller and the balls look larger.  So when the background is white, the background shrinks/ erodes and the foreground dark object s becomd bigger.
 
 when I then apply dilation, the result is pretty good.

Basics of Erosion: 

Erodes away the boundaries of the foreground object
Used to diminish the features of an image.
Working of erosion: 

A kernel(a matrix of odd size(3,5,7) is convolved with the image.
A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel are 1, otherwise, it is eroded (made to zero).
Thus all the pixels near the boundary will be discarded depending upon the size of the kernel.
So the thickness or size of the foreground object decreases or simply the white region decreases in the image.
Basics of dilation: 

Increases the object area
Used to accentuate features

Uses of Erosion and Dilation: 

Erosion: 
It is useful for removing small white noises.
Used to detach two connected objects etc.
Dilation:
In cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
It is also useful in joining broken parts of an object.



'''
# Python program to demonstrate erosion and 
# dilation of images. 
import cv2 
import numpy as np 

# Reading the input image 
img = cv2.imread('images/Cat.jpeg', 0) # this is interesting as is the smarties balls
# img = cv2.imread('images/smarties.png', 0) 

# Taking a matrix of size 5 as the kernel 
kernel = np.ones((5, 5), np.uint8) # dramanmtic when I made it 11,11

# The first parameter is the original image, 
# kernel is the matrix with which image is 
# convolved and third parameter is the number 
# of iterations, which will determine how much 
# you want to erode/dilate a given image. 
img_erosion = cv2.erode(img, kernel, iterations=2) 
img_dilation = cv2.dilate(img, kernel, iterations=2) 
img_dilate_erode =cv2.erode(img_dilation,kernel,iterations=2)
img_erode_dilate = cv2.dilate(img_erosion,kernel, iterations=2)
img_erodeTwiceDilateOne=cv2.erode(img_erode_dilate,kernel,iterations=1)
cv2.imshow('ErodeTwice Dilate once',img_erodeTwiceDilateOne)
cv2.imshow('Input', img) 
cv2.imshow('Erosion', img_erosion) 
cv2.imshow('Dilation', img_dilation) 
cv2.imshow("dilateThenErode",img_dilate_erode)
cv2.imshow('erodeThenDilate',img_erode_dilate)

cv2.waitKey(0) 
