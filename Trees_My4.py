'''Create a tree forest this is the 2d stage of my effort
object  oriented computing
https://www.youtube.com/watch?v=f0TrMH9s-VE&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=1

https://www.youtube.com/watch?v=-LsuiVGO-88&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=3

https://www.youtube.com/playlist?list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv
 Principles of Object-Oriented Programming and draw a forest of unique tree objects.
First create a Tree class and then  replicate it in different locations, sizes and colours. We will also include a very large degree of randomness in our code, so that each time our program runs - a brand new forest with brand new trees is created
Object Oriented Programming
THis is the tutorial
https://www.youtube.com/watch?v=-LsuiVGO-88&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=3

Below is link to all her tutorials
https://www.youtube.com/watch?v=PtvN8ad9N3g&list=RDCMUCKQdc0-Targ4nDIAUrlfKiA&start_radio=1&rv=PtvN8ad9N3g&t=4
'''

import numpy as np
import cv2 
import random

# general parameters
width = 900
height = 600
n_trees = 8
ground_level = height-100
rad = 100
brown=(0,76,153)    #bgr for brown
green, light_green, brown,red = (40,185,40),(25,220,0),(30,65,155),(0,0,255)

# blank image
bg = np.zeros((height, width, 3), dtype=np.uint8)
class Tree():
    # def __init__(self,image,location,rad): # the location is the x value, pass a constant but later make it vary randomly
    def __init__(self,image): # the location is the x value, pass a constant but later make it vary randomly
        self.img =image
        # change location to make it random
        # self.loc =location
        self.loc =int(np.random.choice(range(900),1))
        self.ht =int(np.random.choice(range(200,350),1))
        # self.ht = 300
        self.radius =100
        # self.scale =2
        # creates a float number which we have to address below.
        self.scale =np.random.choice(np.linspace(0.5,2.5,num =8),1)
    def draw(self):
        smallRadius =int((self.radius-40)*(self.scale)/2)
        #trunk
        # # cv2.line(self.img,(self.loc,ground_level),(self.loc,self.ht),brown,20)
        # cv2.line(self.img,(self.loc,ground_level),(self.loc,ground_level-self.ht),brown,int(17*self.scale))
        # #brancheswant them to end in the leaf circles
        # cv2.line(self.img,(self.loc,int(ground_level)-self.ht +100*self.scale ),int((self.loc-45 *self.scale),ground_level-self.ht+self.radius-40 ),brown,int(5*self.scale))
        # cv2.line(self.img,(self.loc,int(ground_level)-self.ht +100* self.scale ),int((self.loc+45 *self.scale),ground_level-self.ht+self.radius-40 ),brown,int(5*self.scale))
        #Hers below
        # trunk
        cv2.line(self.img, (self.loc,ground_level),(self.loc,ground_level-self.ht), brown, int(20*self.scale))
        cv2.line(self.img, (self.loc,ground_level-self.ht+int(75*self.scale)),(self.loc+int(45*self.scale),ground_level-self.ht+smallRadius), brown, int(5*self.scale))
        cv2.line(self.img, (self.loc,ground_level-self.ht+int(75*self.scale)),(self.loc-int(45*self.scale),ground_level-self.ht+smallRadius), brown, int(5*self.scale))
        
        
        #leafs
        # 1st self.img is bg(the background),next is the x,y for the top of the tree, then readius, color,-1
        # cv2.circle(self.img,(self.loc,ground_level-self.ht),int((10+self.radius)*self.scale/2),light_green,-1)
        # # cv2.circle(self.img,(self.loc-90,ground_level-self.ht+40 ),self.radius-40,green,-1)
        # # cv2.circle(self.img,(self.loc+90,ground_level-self.ht+40),self.radius-40,green,-1)
        # #Next steps in the small leaf clusters is to scale the radius of the clusteres(created 'smallRadius' and put it in the draw method)
        # # cv2.circle(self.img,(self.loc-90,ground_level-self.ht+self.radius-40 ),int((self.radius-40)*(self.scale/2)),green,-1)
        # cv2.circle(self.img,(int(self.loc-45* self.scale),ground_level-self.ht+self.radius-40 ),10+smallRadius,light_green,-1)
        # cv2.circle(self.img,(int(self.loc+45 * self.scale),ground_level-self.ht+self.radius -40),10+smallRadius,light_green,-1)
        # # mine
        # cv2.circle(self.img,(self.loc,ground_level-self.ht),int((self.radius*self.scale/2)),green,-1)
        # cv2.circle(self.img,(self.loc-45* self.scale,ground_level-self.ht+self.radius-40 ),int(smallRadius),green,-1)
        # cv2.circle(self.img,(self.loc+45 * self.scale,ground_level-self.ht+self.radius -40),int(smallRadius),green,-1)
        # # Hers
         # leafs - shadows
        cv2.circle(self.img, (self.loc,ground_level-self.ht), int(self.radius*self.scale), green, -1)
        cv2.circle(self.img, (self.loc-int(45*self.scale),ground_level-self.ht+smallRadius), smallRadius , green, -1)
        cv2.circle(self.img, (self.loc+int(45*self.scale),ground_level-self.ht+smallRadius), smallRadius, green, -1)    
        
        
        
        cv2.circle(self.img, (self.loc,ground_level-self.ht), int(self.radius*self.scale-10*self.scale), light_green, -1)
        cv2.circle(self.img, (self.loc-int(45*self.scale),ground_level-self.ht+smallRadius), smallRadius-int(10*self.scale) , light_green, -1)
        cv2.circle(self.img, (self.loc+int(45*self.scale),ground_level-self.ht+smallRadius), smallRadius-int(10*self.scale), light_green, -1)    
        
        
        return self.img
# We are making a line that is 20 pixels wide- so it will look like a rectangle    
# initally passisng in ground_level as a fixed value,



# draw background
cv2.rectangle(bg,(width,0), (0, ground_level), (255,255,95), -1)
cv2.rectangle(bg,(width, ground_level), (0, height), green, -1)

#display image
# Create an objext of the Class 'Tree" and pass if bg which is the 'image' attribute and 450 which is the x coordiante 'location' attribute
# note that the 'draw'method is to draw a LINE
for i in range(1,n_trees,1):
    # img = Tree(bg,10+i*100,rad).draw()
    img = Tree(bg).draw()

# img = Tree(bg,450,rad).draw()
cv2.imshow('forest of objects', img) 

    
cv2.waitKey(0)
cv2.destroyAllWindows()

