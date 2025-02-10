'''CV_24Part 1    tracking persons with rectangle and show staus as 'movement'
optioms to conver .mov to .avi

https://www.movavi.com/support/how-to/how-to-convert-mov-to-avi.html#
Hitfilm Express (free or 300$ for Pro), DaVinci Resolve (free or 300$ for studio), openshot (free), shotcut (free), Olive (free), vsdc (free), lightworks (free), Blender (free ... and yes it can be used to edit video).

How can I convert MOV to AVI on a Mac?
Just follow these simple steps.
Install the distribution file of Movavi Video Converter for Mac and run the app.
Download Movavi Video Converter for Mac
Drag and drop your MOV files into the program window.
Select the Video tab below and choose AVI as the output format.
Click the Convert button and wait for the conversion process to end. That’s all there is to it!
You can also convert MOV to AVI online using any web media conversion service. Please note that some services have file size restrictions, so take that into account when choosing an online converter for large files.
Can I convert MOV to AVI for free with VLC?
Yes, you can use the VLC media player as MOV-to-AVI converter freeware. To convert MOV to AVI with that app, do as follows.
Install and run VLC.
Download VLC
Click Media and then choose Convert / Save.
Click Add and open the MOV file you want to convert.
Select Convert / Save below.
In the new dialog box, click the Wrench icon, select AVI in the Encapsulation tab and click Save.
Click Browse and enter a name for the resulting AVI file. Make sure the name contains the .avi extension.
Hit Start to start the conversion.

Read more: https://www.movavi.com/support/how-to/how-to-convert-mov-to-avi.html# © Movavi.com

'''

import cv2
import numpy as np 
cap = cv2.VideoCapture('images/vtest.avi')
ret,frame1 =cap.read()
ret,frame2 =cap.read()
while cap.isOpened():
    # ret,frame1 =cap.read()
    # ret,frame2 =cap.read()
    ## cv2.absdiff  is the absolute difference between the 1st and 2d frame
    ## then convert into grayscale because it is easier to find the contours in grayscale
    ## instead of the bgr mode
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    # 2d paramter is ksize or  kernal size(5,5), 3d parameter is sigmax =0
    blur =cv2.GaussianBlur(gray,(5,5),0)
    ## the  _mis a varialbe we are not using,   the threshold 2d value os the min threhold and the 3d is the max.
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)  # type is thresh binary
    ## dilate the thresh image to fill all the holes
    ## the 2d threhold is kernal size = None, and the iterations =3
    dilated = cv2.dilate(thresh, None, iterations=3)
    ##  below mat, mode, method for find contours
    contours,_ =cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1,contours, -1, (0,255,0),2)
     
    cv2.imshow('video',frame1)
    
    # interesting if I delete the next two lines
    frame1 = frame2
    ret,frame2 =cap.read()
    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()

