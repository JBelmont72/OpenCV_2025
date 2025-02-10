'''

'''
import cv2
import numpy as np

# img = cv2.imread("images/Cat.jpeg")
# img = cv2.imread("images/road.jpg")
img = cv2.imread("images/detect_blob.png")
# filter2D
# build a filter to blur image
blur_filter = np.ones(([3,3]),np.uint8)
# blur_filter = np.array([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
blur_filter = blur_filter / 9 ## 9 is the size of the filter 3X3 and makes img just a little fuzzy
#ddepth is dimension depth , can change to 16,32 float
blur_img = cv2.filter2D(img, ddepth=-1, 
        kernel=blur_filter)

# NO FILTER // BRIGHTNESS
# the only pixel that is being adjusted is the cnetral one.
# if central is 1 then no change.can brighten of dim by changing
no_filter = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
no_filter = no_filter    ## can divide or multiply   here or in array central value
bright_img = cv2.filter2D(img, ddepth=-1, 
        kernel=no_filter)

# BLUR The larger the ksize , the blurrier, HAS to BE ODD NUMBER
# previously used a ksize of 3X3
blur_img = cv2.blur(img, ksize=(11, 11))

# GAUSSIAN BLUR sigma is how spread out the standard deviations
gaus_img = cv2.GaussianBlur(img, ksize=(11, 11),
            sigmaX=30, sigmaY=300)

# SHARPEN  make bigger difference between the central value and its neighbors
# central pixel must be greater than (-4)  Note 5 works best
sharpen_filter = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
# sharpen_filter=sharpen_filter*2  #my addition
sharp_img = cv2.filter2D(img, ddepth=-1, 
        kernel=sharpen_filter)

# EDGE DETECTION // LAPLACIAN
# interesting, with the blob, I get greeat edges with a (1,1) array!
# 3X3 gives the whiskers only with the cat
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.GaussianBlur(img, ksize=(3, 3),
            sigmaX=1, sigmaY=1)
# gray_img = cv2.GaussianBlur(img, ksize=(1, 1),
#             sigmaX=1, sigmaY=1)
edges = cv2.Laplacian(gray_img, ddepth=-1)

cv2.imshow("Cat!", img)
# cv2.imshow("Cat!!", blur_img)
# cv2.imshow("Cat_bright_image", bright_img)
cv2.imshow("Cat_gaus_image", gaus_img)
cv2.imshow("Cat_sharp_image", sharp_img)
cv2.imshow("Cat_edges_image", edges)
# cv2.imshow("Cat!", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
