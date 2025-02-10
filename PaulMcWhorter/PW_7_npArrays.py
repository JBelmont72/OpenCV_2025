'''
PW lesson 7 understanding pictures and images
note that i need 'if elif' or 'if and else' and not 'if if' which just canged me back to dark for the whole board  
'''
import cv2
import numpy as np
boardSize= int(input('How big do you want the boarad?'))
squares=int(input('How many squares do you want across?'))
# board =np.zeros([boardSize,boardSize,3],dtype=np.uint8)
sqSize=int(boardSize/squares)
# Square=np.zeros([int(sqSize),int(sqSize),3],dtype=np.uint8)
darkColor=(255,0,0)
lightColor=(0,0,100)
nowColor=darkColor
while True:
    Square=np.zeros([boardSize,boardSize,3],dtype=np.uint8)
    for rows in range(0,squares):
        for col in range(0,squares):
            Square[int(sqSize*rows):int(sqSize*(rows+1)),int(sqSize*col):int(sqSize*(col+1))]=nowColor
            if nowColor==darkColor:
                nowColor=lightColor
            elif nowColor==lightColor:
                nowColor=darkColor
        if nowColor==darkColor:
            nowColor=lightColor
        elif nowColor==lightColor:
            nowColor=darkColor    
    cv2.imshow('frame',Square)
    
    if cv2.waitKey(0) & 0xFF==ord('q'):
      break
cv2.destroyAllWindows()

