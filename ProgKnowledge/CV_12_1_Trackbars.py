'''CV_12_1_trackbars
Always check for .dsStore before COMMITTING
ANd delete any movies 

'''
# import cv2
# import numpy as np
# def nothing(x):
#     print(x)
    
# # create a black frame and apply b g r colors
# img = np.zeros((300,512,3),np.uint8)
# cv2.namedWindow('img')
# cv2.createTrackbar('B','img',0,255,nothing) # the 5th arduemtn is the callback function
# cv2.createTrackbar('G','img',0,255,nothing) # the 5th arduemtn is the callback function
# cv2.createTrackbar('R','img',0,255,nothing) # the 5th arduemtn is the callback function


# while True:
#      # if the 'cv2.imshow('img',img) is same as the cv2.namedWindow then we have a combined window if the treackbar with the FRAME 'img'
#     # this is nice becasue the trackbar is not hidden!! and is already stretched out full length
#     cv2.imshow('img',img)
#     cv2.moveWindow('img',0,150)
#     b= cv2.getTrackbarPos('B', 'img')
#     g= cv2.getTrackbarPos('G', 'img')
#     r= cv2.getTrackbarPos('R', 'img')
#     img[:]=[b,g,r]
#     k = cv2.waitKey(1)& 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()
########## create a switch  SWITCH  when zero nothing
# import cv2
# import numpy as np
# def nothing(x):
#     print(x)
    
# # create a black winodoe/frame
# img = np.zeros((300,512,3),np.uint8)
# cv2.namedWindow('img')
# cv2.createTrackbar('B','img',0,255,nothing) # the 5th arduemtn is the callback function
# cv2.createTrackbar('G','img',0,255,nothing) # the 5th arduemtn is the callback function
# cv2.createTrackbar('R','img',0,255,nothing) # the 5th arduemtn is the callback function
# switch = '0 : OFF  1 : ON' 
# cv2.createTrackbar(switch,'img',0,2,nothing)

# while True:
#      # if the 'cv2.imshow('img',img) is same as the cv2.namedWindow then we have a combined window if the treackbar with the FRAME 'img'
#     # this is nice becasue the trackbar is not hidden!! and is already stretched out full length
#     cv2.imshow('img',img)
#     cv2.moveWindow('img',0,150)
#     b= cv2.getTrackbarPos('B', 'img')
#     g= cv2.getTrackbarPos('G', 'img')
#     r= cv2.getTrackbarPos('R', 'img')
#     s= cv2.getTrackbarPos(switch, 'img')
#     if s == 0:
#         img[:]= 0     # or simply 0
#     else:
#         img[:]=[b,g,r]
        
    
#     # img[:]=[b,g,r]
#     k = cv2.waitKey(1)& 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()


########  third modifiction  to print values on the image using the trackbar
##  and use a switch to go from grayscale to color
##  have to put the imshow AFTER the if pass else cvw.cvtcolor conditions!!
import cv2
import numpy as np
def nothing(x):
    print(x)
    
# create a black window/frame
# img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('img')  # need this even for just reading an image 
cv2.createTrackbar('CurPos','img',10,400,nothing) # the 5th arduemtn is the callback function
switch = '0 : BGR  1 : GRAY' 
cv2.createTrackbar(switch,'img',0,2,nothing)

while True:
    img = cv2.imread('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/lena.jpg')
     # if the 'cv2.imshow('img',img) is same as the cv2.namedWindow then we have a combined window if the treackbar with the FRAME 'img'
    # this is nice becasue the trackbar is not hidden!! and is already stretched out full length
    # img = cv2.imshow('img',img)
    # cv2.moveWindow('img',0,0)
    pos= cv2.getTrackbarPos('CurPos', 'img') # chekc against how McWhorter gets the vlaues into the while loop
    font =cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,6,(0,0,0),10)

    s= cv2.getTrackbarPos(switch, 'img')
    if s == 0:
        pass
    if s>= 1:
        
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
    img = cv2.imshow('img',img)
    k = cv2.waitKey(1)& 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()



'''
 ## below is thefirst part with the trackbar creation , frame('img') any selected combo of b g r 
# import cv2
# import numpy as np
# def nothing(x):
#     print(x)
    
# # create a black winodoe/frame
# img = np.zeros((300,512,3),np.uint8)
# cv2.namedWindow('img')
# cv2.createTrackbar('B','img',0,255,nothing) # the 5th arduemtn is the callback function
# cv2.createTrackbar('G','img',0,255,nothing) # the 5th arduemtn is the callback function
# cv2.createTrackbar('R','img',0,255,nothing) # the 5th arduemtn is the callback function


# while True:
#      # if the 'cv2.imshow('img',img) is same as the cv2.namedWindow then we have a combined window if the treackbar with the FRAME 'img'
#     # this is nice becasue the trackbar is not hidden!! and is already stretched out full length
#     cv2.imshow('img',img)
#     cv2.moveWindow('img',0,150)
#     b= cv2.getTrackbarPos('B', 'img')
#     g= cv2.getTrackbarPos('G', 'img')
#     r= cv2.getTrackbarPos('R', 'img')
#     img[:]=[b,g,r]
#     k = cv2.waitKey(1)& 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()


# played with splicing gthe rfframe into quarters with different parameters
'''


'''
import cv2
import numpy as np
## the callback function
def nothing(x):
    print(x)
    
# create a black winodoe/frame
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('img')
cv2.createTrackbar('B','img',0,255,nothing) # the 5th arduemtn is the callback function
cv2.createTrackbar('G','img',0,255,nothing) # the 5th arduemtn is the callback function
cv2.createTrackbar('R','img',0,255,nothing) # the 5th arduemtn is the callback function


while True:
     # if the 'cv2.imshow('img',img) is same as the cv2.namedWindow then we have a combined window if the treackbar with the FRAME 'img'
    # this is nice becasue the trackbar is not hidden!! and is already stretched out full length
    
    cv2.imshow('img',img)
    cv2.moveWindow('img',0,150)
    
    k = cv2.waitKey(1)& 0xFF
    if k == 27:
        break
    b= cv2.getTrackbarPos('B', 'img')
    g= cv2.getTrackbarPos('G', 'img')
    r= cv2.getTrackbarPos('R', 'img')
    
    # np rows collumns 300 512
    img[0:150,0:256]=[b,g,r]
    # top left
    if b+100>= 255:
        
        img[0:150,0:256]=[int(255),g,r]
    # bottom left
    if g<155:
        img[0:150,256:512]=[b,g,r]
    # bottom right 
    if g+100>=255:
        img[150:300,256:512]=[b,255,r]
    if g<155:
        img[150:300,256:512] = [b,g,r]
    # top right    
    if b< 255:        
        img[150:300,0:256]=[int(b),g,r]
cv2.destroyAllWindows()
'''
