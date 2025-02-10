'''SamWestby_5_EDGE/corner detection
'''
import cv2
import numpy as np

img = cv2.imread("images/messi5.jpg")
# img = cv2.imread("images/road.jpg")
# img = cv2.imread("images/HappyFish.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SHI-TOMASI METHOD_ look for all the corners by having a sliding box window.when sees a line entering the box at acertaind angle and predicts where it should exit if 'STRAIGHT."
# if there is a large difference between the entrance and exit , then decides there is a corner there."
# the quality lefel and the distance between the corners are arguemtns
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                qualityLevel=.15, minDistance=50)
corners = np.intp(corners)
# corners = np.int0(corners) ## this is deprecated
# the np.into np array
for c in corners:
    x, y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=20, 
                    color=(0, 0, 255), thickness=-1)

##HARRIS CORNER DETECTION
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                qualityLevel=0.01, minDistance=50,
                useHarrisDetector=True, k=.15)
# higher k means less corners
corners = np.intp(corners)
# corners = np.int0(corners)

for c in corners:
    x, y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=10, 
                    color=(0, 254, 0), thickness=-1)

cv2.imshow("Shape", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("assets/5_shape_w_corners.png", img)