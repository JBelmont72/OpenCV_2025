'''Create a tree forest this is the 2d stage of my effort
object  oriented computing
https://www.youtube.com/watch?v=f0TrMH9s-VE&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=1

https://www.youtube.com/watch?v=-LsuiVGO-88&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=3

https://www.youtube.com/playlist?list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv
 Principles of Object-Oriented Programming and draw a forest of unique tree objects.
First create a Tree class and then  replicate it in different locations, sizes and colours. We will also include a very large degree of randomness in our code, so that each time our program runs - a brand new forest with brand new trees is created
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
rad = 100
brown=(0,76,153)    #bgr for brown
green, light_green, brown,red = (40,185,40),(25,220,0),(30,65,155),(0,0,255)

# blank image
bg = np.zeros((height, width, 3), dtype=np.uint8)
class Tree():
    def __init__(self,image,location,rad): # the location is the x value, pass a constant but later make it vary randomly
        self.img =image
        self.loc =location
        self.ht = 300
        self.radius =100
    def draw(self):
        #trunk
        # cv2.line(self.img,(self.loc,ground_level),(self.loc,self.ht),brown,20)
        cv2.line(self.img,(self.loc,ground_level),(self.loc,ground_level-self.ht),brown,35)
        #brancheswant them to end in the leaf circles
        cv2.line(self.img,(self.loc,int(ground_level)-self.ht +150 ),(self.loc-90,ground_level-self.ht+self.radius-40 ),brown,10)
        cv2.line(self.img,(self.loc,int(ground_level)-self.ht +150 ),(self.loc+90,ground_level-self.ht+self.radius-40 ),brown,10)
        
        #leafs
        # 1st self.img is bg(the background),next is the x,y for the top of the tree, then readius, color,-1
        cv2.circle(self.img,(self.loc,ground_level-self.ht),self.radius,green,-1)
        # cv2.circle(self.img,(self.loc-90,ground_level-self.ht+40 ),self.radius-40,green,-1)
        # cv2.circle(self.img,(self.loc+90,ground_level-self.ht+40),self.radius-40,green,-1)
        cv2.circle(self.img,(self.loc-90,ground_level-self.ht+self.radius-40 ),self.radius-40,green,-1)
        cv2.circle(self.img,(self.loc+90,ground_level-self.ht+self.radius -40),self.radius-40,green,-1)
        return self.img
# We are making a line that is 20 pixels wide- so it will look like a rectangle    
# initally passisng in ground_level as a fixed value,



# draw background
cv2.rectangle(bg,(width,0), (0, ground_level), (255,255,95), -1)
cv2.rectangle(bg,(width, ground_level), (0, height), green, -1)

#display image
# Create an objext of the Class 'Tree" and pass if bg which is the 'image' attribute and 450 which is the x coordiante 'location' attribute
# note that the 'draw'method is to draw a LINE
img = Tree(bg,450,rad).draw()
cv2.imshow('forest of objects', bg) 

    
cv2.waitKey(0)
cv2.destroyAllWindows()

