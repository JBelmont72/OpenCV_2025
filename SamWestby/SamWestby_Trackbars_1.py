'''
Add trackbars



'''
import cv2
import numpy as np

# img = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/Cat.jpeg',cv2.IMREAD_UNCHANGED)
xPos =30
yPos =60

# Step 2
def MyCallback1(xPos):
    pass
def MyCallback2(yPos):
    pass

# def MyCallback1(val):
#     global xPos
#     print('x = ',val)
#     xPos= val
# def MyCallback2(val):
#     global yPos
#     print('y = ',val)
#     yPos= val
    
#STEP 1 1st Str is the value name,2d Str is the Name of location of the trackbar, the last is the CALLBACK function
cv2.namedWindow('My Trackbars')
cv2.resizeWindow('My Trackbars',400,100)
cv2.moveWindow('My Trackbars',400,10)
cv2.createTrackbar('xPos','My Trackbars',xPos,300,MyCallback1)
cv2.createTrackbar('yPos','My Trackbars',yPos,300,MyCallback2)
while True:
    
    img = cv2.imread('/Users/judsonbelmont/Documents/Python/OpenCV_3/images/Cat.jpeg')
    print('Shape y; = ',img.shape[0])
    print('Shape x; = ',img.shape[1])
    print('dimension: ',img.dtype)
    print(img.shape)
    xPos = cv2.getTrackbarPos('MyCallback1','My Trackbars')
    print('xPos in loop:  ',xPos)
    # img = cv2.resize(img,(int(img.shape[1]/2),img.shape[0]))
    # img = cv2.resize(img,(img.shape[1],img.shape[0]))
    
    
    cv2.circle(img,(xPos,yPos),25,(255,0,0),2)
    
    
    cv2.imshow('imag',img)
        
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('myWebCam',gray)
        
    if cv2.waitKey(0) & 0xFF == ord('c'): # if waitkey (1)just flashes on
        cv2.destroyAllWindows #press any key with cursor on photo
    else:
        break
    
#         img = cv2.imshow('img',img)
#     k = cv2.waitKey(1)& 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()
'''
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

