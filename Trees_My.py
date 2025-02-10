'''Create a tree forest - this is the 1st stage of my effort
object  oriented computing
https://www.youtube.com/watch?v=f0TrMH9s-VE&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=1

https://www.youtube.com/watch?v=-LsuiVGO-88&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=3

https://www.youtube.com/playlist?list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv
In this tutorial, we will practice the principles of Object-Oriented Programming and draw a forest of unique tree objects.
We will first create a Tree class and then we will replicate it in different locations, sizes and colours. We will also include a very large degree of randomness in our code, so that each time our program runs - a brand new forest with brand new trees is created
Object Oriented Programming


'''

import numpy as np
import cv2 
import random

# general parameters
width = 900
height = 600
n_trees = 30
ground_level = height-100
BrThickness =2
treeX =200  # the x position for the left tree trunk
variationYbot =20  #this is the variation added to the bottom of the tree trunks
variationYtop =120
treeWidth =50
treeBottom=(treeX,int(ground_level+variationYbot))
treeTopX=treeX+treeWidth
treeTopY = int(ground_level -variationYtop-200)
treeTop=(treeTopX,treeTopY)
# treeTop =(treeX+treeWidth,int(ground_level-200 -variationYtop))
brown=(0,76,153)    #bgr for brown

# colours
green, light_green, brown,red = (40,185,40),(25,220,0),(30,65,155),(0,0,255)

# blank image
bg = np.zeros((height, width, 3), dtype=np.uint8)

# draw background
cv2.rectangle(bg,(width,0), (0, ground_level), (255,255,95), -1)
cv2.rectangle(bg,(width, ground_level), (0, height), green, -1)
# leftTrunk = cv2.line(bg,treeBottom,treeTop,brown,BrThickness,4)
# rightTrunk = cv2.line(bg,treeBottom,treeTop,brown,BrThickness,4)
cv2.rectangle(bg,treeBottom,treeTop,brown,-1)
cv2.circle(bg,(int(treeX+treeWidth/2),(int(ground_level-200 -variationYtop))),treeWidth,green,-1)
#display image
cv2.imshow('forest of objects', bg) 

    
cv2.waitKey(0)
cv2.destroyAllWindows()

