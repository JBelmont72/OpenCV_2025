'''CV_21_Pyramids, Gaussian
Gaussian
THe best turorial of all===
https://automaticaddison.com/how-the-sobel-operator-works/

no exclusive function for laplacain pyramid.
A level of Laplacian Pyramid is formed by the 
difference between that level in the Gaussian pyramid and the 
"expanded version of its UPPER LEVEL in Gaussian Pyramid"
we have appended the images to the list 'layer'
1 load 2 images
2 find gaussian pyramids
3 find laplacian pyrimids
4 join each half in the laplacian pyramids
5 reconstruct the original image

At bottom is procedure to resize.
? do the images have to have even size parameters (  not odd width, height)?
Why I've got error in the 
laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
Somebody please help
Reply
1 reply
 @derkertherblack6177
@derkertherblack6177
3 years ago
It is probably because of the size of the image you use, I had the same problem and I changed the image to a 512x512 image
if you pyrUp an image which was of odd shape earlier, you loose some pixels and operation ends with error. 

For example if you have a (3, 3) image and scale it down, it'll be (1, 1), but if you'll scale it up again it will be of shape (2, 2

try these, 
  gaussian_extended = cv2.pyrUp(gp[i],dstsize = (gp[i - 1].shape[1], gp[i - 1].shape[0])),
I guess the issue is in mismatch size of images, I hope this solves out the error


-----
The two arrays passed to np.hstack have to be in a Tuple. So instead of img1[:, :128], img2[:, 128:] it has to be (img1[:, :128], img2[:, 128:])
------
cv2.error: OpenCV(4.3.0) C:\projects\opencv-python\opencv\modules\core\src\arithm.cpp:669: error: (-209:Sizes of input arguments do not match) The operation is neither 'array op array' (where arrays have the same size and the same number of channels), nor 'array op scalar', nor 'scalar op array' in function 'cv::arithm_op'   -- WTF is this error
 


Reply


2 replies
 @abdielribeiro2955
@abdielribeiro2955
3 years ago
use some online tool to resize the image (iloveimg.com) and place both images in 512 x 512 resolution, it worked for me



'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


apple = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/apple.jpg',cv2.IMREAD_UNCHANGED)
orange = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/orange.jpg',cv2.IMREAD_UNCHANGED)

# print(apple.shape)
# print(orange.shape)

# apple_orange = np.hstack((apple[: , :256] ,orange[: , 256:]))



# Gaussian pyramid for apple image
apple_copy = apple.copy()

gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# Gaussian pyramid for Orange image
orange_copy = orange.copy()

gp_orange = [orange_copy]

for i in range(5):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)





# Generate Laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
# same a lp_apple[gp_apple[5]]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_extended)
    lp_apple.append(laplacian)


# Generate Laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(laplacian)
    
    



# Now add left and right halvas of images in each level.
apple_orange_pyramid = []
n = 0
for apple_lap , orange_lap in zip(lp_apple, lp_orange):
    n += 1
    rows , cols , ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[: , 0:int(cols/2)] ,orange_lap[: , int(cols/2):]))
    apple_orange_pyramid.append(laplacian)





# Now Reconsturct the image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i] , apple_orange_reconstruct)

cv2.imshow('orange0',lp_orange[0])
cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('apple_orange_reconstruct',apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
# print(apple.shape)
# print(orange.shape)
# apple_orange =np.hstack((apple[:,:256],orange[:,256:]))
# cv2.imshow('apple_orange',apple_orange)
# FIND GAUSSIAN IMAGE
# apple_copy = apple.copy()
# gp_apple =[apple_copy]

# orange_copy = orange.copy()
# gp_orange =[orange_copy]
# # gaussian pyramid for apple 
# for i in range(6):
#     apple_copy=cv2.pyrDown(apple_copy)
#     gp_apple.append(apple_copy)
#     # cv2.imshow(str(i),apple_copy)
# # gaussian pyramid for orange
# for i in range(6):
#     orange_copy=cv2.pyrDown(orange_copy)
#     gp_orange.append(orange_copy)
#     # cv2.imshow(str(i),orange_copy)
# # laplacian pyramid for apple
# layer_apple = gp_apple[5] # we're getting the last (or pinnacle 0layer/level of the apple gaussian pyramid)
# cv2.imshow('upper level of gaussian pyramid', layer_apple)
# # now create the Laplacain pyramnid
# lp = [layer_apple]  # note the len of layer is 4, 
# # print('len of layer:',len(layer_apple))
# # print('gp is : ',len(gp_apple))  # note the len of gp is 7
# for i in range(6,0,-1):  # extended level of upper version of upper level
#     size = (gp_apple[i - 1].shape[1], gp_apple[i - 1].shape[0])
#     gaussian_expanded = cv2.pyrUp(gp_apple[i], dstsize=size)
#     laplacian =cv2.subtract(gp_apple[i-1],gaussian_expanded)
#     lp.append(laplacian)
#     cv2.imshow(str(i),laplacian) 
# # laplacian pyramid for orange 


 

 




# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print('Original Dimensions : ',img2.shape)
# width = 930         #columns
# height = 862        #rows
# dim =(width,height)
# halfWidth=int(width/2)


# scale_percent = 60 # percent of original size
# width = int(img2.shape[1] * scale_percent / 100)
# height = int(img2.shape[0] * scale_percent / 100)
# dim = (width, height) 
# resize image
# resized = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

# print('Resized Dimensions : ',resized.shape)
# apple_orange = np.hstack((img1[ :, :halfWidth:],resized[:,halfWidth:]))
# cv2.imshow("apple_orange", apple_orange)                         
# cv2.imshow("Resized image", resized)