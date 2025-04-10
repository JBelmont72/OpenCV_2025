'''
curiious   I start the video recording with++   'avi': cv2.VideoWriter_fourcc(*'XVID'),
and retrun the video recrdong as   ++   return VIDEO_TYPE['avi']

but the suffix in the recorded file is .mp4


'''
# import cv2
# cap = cv2.VideoCapture(1)
# # fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (w,h))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         out.write(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# to record a video in opencv

''' CV_4_MP4_2.py 'coding for entrepreneurs'

THIS WORKS 
https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python/
'''

import numpy as np
import os
import cv2
# from blog Kaira 
filename = '10fpsvideo.mp4'
framespersecond = 10.0
res = '480p'
# his from top of blog
# filename = 'video.avi'
# frames_per_second = 24.0
# res = '720p'

# Set resolution for the video capture
# Function adapted from https://kirr.co/0l6qmh
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),     ## 8 Feb 2025 *'XVID'  and 'AVC1 '  both work fine choose either
    'avi': cv2.VideoWriter_fourcc(*'AVC1'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    # 'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']



cap = cv2.VideoCapture(1)
out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
