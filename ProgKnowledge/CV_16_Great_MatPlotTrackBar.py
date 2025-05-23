'''
tutorial from Opencv for using a trackbar on a image (not a video or webcam
this is the blenicng of an apple and orarnge)
https://docs.opencv.org/3.4/da/d6a/tutorial_trackbar.html

Argparse tutorials: 
https://www.digitalocean.com/community/tutorials/how-to-use-argparse-to-write-command-line-programs-in-python
https://docs.python.org/3/library/argparse.html#adding-arguments
https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/?ref=ml_lbp
'''



# from __future__ import print_function
# from __future__ import division
import cv2 as cv
import argparse
alpha_slider_max = 100
title_window = 'Linear Blend'
def on_trackbar(val):
 alpha = val / alpha_slider_max
 beta = ( 1.0 - alpha )
 dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
 cv.imshow(title_window, dst)
parser = argparse.ArgumentParser(description='Code for Adding a Trackbar to our applications tutorial.')
parser.add_argument('--input1', help='Path to the first input image.', default='images/apple.jpg')
parser.add_argument('--input2', help='Path to the second input image.', default='images/orange.jpg')
args = parser.parse_args()
src1 = cv.imread(cv.samples.findFile(args.input1))
src2 = cv.imread(cv.samples.findFile(args.input2))
if src1 is None:
 print('Could not open or find the image: ', args.input1)
 exit(0)
if src2 is None:
 print('Could not open or find the image: ', args.input2)
 exit(0)
cv.namedWindow(title_window)
trackbar_name = 'Alpha x %d' % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
# Show some stuff
on_trackbar(0)
# Wait until user press some key
cv.waitKey()