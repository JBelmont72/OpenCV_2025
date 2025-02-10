'''CV_21_Pyramid.py
the best tutorial for explaining Sorbel operators
https://automaticaddison.com/how-the-sobel-operator-works/
follow up link is:(this is a great depiction of calculus)
https://cse442-17f.github.io/Sobel-Laplacian-and-Canny-Edge-Detection-Algorithms/

THis site explains the laplacian of gaussian:' How the Laplacian of Gaussian Filter Works '
https://automaticaddison.com/how-the-laplacian-of-gaussian-filter-works/

To solve this problem, a Gaussian smoothing filter is commonly applied to an image to reduce noise before the Laplacian is applied. This method is called the Laplacian of Gaussian (LoG).

We also set a threshold value to distinguish noise from edges. If the second derivative magnitude at a pixel exceeds this threshold, the pixel is part of an edge.
this image is the formula for the Lap of Gaus formula:
https://automaticaddison.com/wp-content/uploads/2019/12/7-log.jpg
this is open cv tutorial on gfaussian with a program illustrating
https://docs.opencv.org/4.x/d5/db5/tutorial_laplace_operator.html


Source for photos to play with :  https://pixabay.com



the first link os very advanced, use the second two
https://python.hotexamples.com/examples/cv2/-/pyrDown/python-pyrdown-function-examples.html
has baout 60 different programs using pyramids/laplacain, gaussian


https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_pyramids/py_pyramids.html

https://www.projectpro.io/recipes/do-laplacian-pyramids-work-opencv
There is no pre-defined function for creating a Laplacian pyramid in OpenCV. Laplacian pyramids can be obtained by the difference between that layer and its lower layer (i.e., expanded layer) in the Gaussian pyramid. We already know that Laplacian is a high pass filter, and for this reason, we obtain the edges of the image as output in each layer.

Let us now create a gaussian pyramid, and in the next step, we shall calculate the difference between layers to obtain the Laplacian pyramid.

To begin with, let us create an array called gaussian in which we will store all the layers of the Gaussian pyramid and initialize a variable called gaussian_layer with a copy of the image that we have read using the copy() function.


gaussian = []  

gaussian_layer= image.copy() 


We can easily create a Gaussian pyramid using the cv2.pyrDown() function inside a loop.

for i in range(3):
    gaussian_layer = cv2.pyrDown(gaussian_layer)
    gaussian.append(gaussian_layer)
    cv2.imshow('Gaussian Layer -{}'.format(i),gaussian_layer)
cv2.waitKey(0)
cv2.destroyAllWindows()
In the above chunk of code, we perform two other functions inside the loop for every iteration. One is appending the gaussian layer that we obtained from the cv2.pyrdown() function to the list that we created earlier using the append() function. The other displays each layer of the Gaussian pyramid using the cv2.imshow() function

Step 3: Create a Laplacian Pyramid
Once we have the list of gaussian layers ready, we can proceed with creating the Laplacian pyramid. To do that, let us first initialize a list called Laplacian which will store all the layers of the Laplacian pyramid with the top image of the Gaussian pyramid. (i.e., the last element of the gaussian list).


    laplacian = [gaussian[-1]] 

Then by iterating through the gaussian list in reverse order, let us perform the following in each iteration.

Obtain the expanded layer of the current layer using the cv2.pyrup() function
Obtain the Laplacian layer by calculating the difference between the current gaussian layer and the expanded gaussian layer using the cv2.subtract() function.
Append each Laplacian layer to the laplacian list.
Display each Laplacian layer.
for i in range(2,0,-1):
    size = (gaussian[i - 1].shape[1], gaussian[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian[i], dstsize=size)
    laplacian_layer = cv2.subtract(gaussian[i-1], gaussian_expanded)
    laplacian.append(laplacian_layer)
    cv2.imshow('laplacian layer -{}'.format(i-1),laplacian_layer)
cv2.waitKey(0)
cv2.destroyAllWindows()
As is well known that the dimensions of the two images that we subtract must be of the same dimension, we calculate the size of the layer behind the current layer and pass that size as the output size to the dstsize parameter of the cv2.pyrUp() function. The dstsize parameter is an optional parameter of both cv2.pyrUp() and cv2.pyrDown() functions which returns the output image in the desired dimension.




https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_pyramids/py_pyramids.html
work with images of diffeent resolution, the face can be different from other portions of photo
 a type of multi scale signal representaton subjected to repeated scaling 
 level o  original image
 level 1  blur and subsample 1/2 resolution
 level 2  blur and subsample 1/4 resolution
 level 3  blur and subsample 1/8 resolution
 level 4  blur and subsample 1/16 resolution
 two types of image pyramids
 laplacian and gaussian
 Two types of gaussian:
 gaussian pyr down and pyr up  pyr for pyramid
https://www.projectpro.io/recipes/do-laplacian-pyramids-work-opencv

UCF CRCV lecture 7 
pyramids.  useful for representing images, pyramid is buiilt by using multiple copies of the image.
Each level is 1/4 of the size of tghe previous level.
THe lowest level if of the HIGHEST resolution.'
512 X 512 is level 10  to 8x8 level 4 to 4x4  level 3to 2x2 level 2; to 1x1 level 1
 Gaussian Pyramid to reduce 
 g = reduce(g-1)
 people can ecognize things of different scale. computers not good at this.
 We want to find things in image of different scale.
 
 We look for the same thing at different scales. Start with full resolution image and resize it smaller.
 
 gong down by half means you go down 4 (2x2) pixels at a time.
 Shannon Nyquist sampling theorem.
 it says theat sampling ragte must be at least twice the highest frequency. half of the sampling rate it called the Nyquiest rate or Nyquist Frequency.
 
 if we downsample, i e set the sampling frequency to half of ist current rate , then we need to ensure that there is niothng in our signal(in our case image)thjat is greater than 1/th.
 
 'aliasing' a plaid shirt  is example. 
 if film is 24 fps and sometin is moving fastr than half, then you can see wheels stopping or going backwards. tskes the form of MOIRE>
 
 we must do is use a low-pass filter the signal(the image) to remove the frequencies between the Nyquist rate and the old.
 Use Gaussian to remove what we need but not too mush.
 In a gaussian pyramid, the lowedst level (g0) is the original image I. the next level up is g1, is computed by a Gaussian(discrete approximatkion) weighted average of the values of g0.
 EACH LEVEL Gi  is computed by a Gaussian weighted avarage of the value s of Gi-1.Each level is computed by the weigthed values of the Gi-1 (or lower closer to the original Image)
 Smoothing and then downsizing.
 ____
 related to this is the idea of expanding an image from low-res to highre res.
 Why upsize after downsize.
 It is useful to smaooth out .
 It makes sure that each pixel is weighted equally.
 Laplacian is used for image compression.  . LImage = GImage 
 
 Gaussian  repeat sampling
  
 

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/butterfly.jpg')

pyr_d_1 = cv2.pyrDown(img)
pyr_d_2 = cv2.pyrDown(pyr_d_1)
hr =cv2.pyrUp(pyr_d_2)
# pyr_d = cv2.pyrDown(img)
# pyr_d = cv2.pyrDown(img)
# pyr_d = cv2.pyrDown(img)
cv2.imshow('pyrDown_1',pyr_d_1)
cv2.imshow('pyrDown_2',pyr_d_2)
cv2.imshow('Original Image',img)
cv2.imshow('pyrUp',hr)

cv2.waitKey(0)
cv2.destroyAllWindows()

