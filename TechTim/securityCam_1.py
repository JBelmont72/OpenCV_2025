'''
tech with Tim
aim is to take this security cam on my computer and combine it using socket and struct modules to put on LAN
pass face and bodies to face detection /body haar cascades
cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_fron...')
'''
import time
import cv2
import datetime
import os
cap=cv2.VideoCapture(1)
cap.set(4,720)
cap.set(3,1080)
cap.set(cv2.CAP_PROP_FPS,30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

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
    'avi': cv2.VideoWriter_fourcc(*'avc1'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    # 'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      print(ext)
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))





print(datetime.date(2025,1,8))
face_cascade=cv2.CascadeClassifier("haar/haarcascade_frontalface_default.xml")
face_cascade2=cv2.CascadeClassifier("haar/haarcascade_profileface.xml")
# face_cascade2=cv2.CascadeClassifier("haar/haarcascade_frontalface_alt.xml")
body_cascade=cv2.CascadeClassifier("haar/haarcascade_fullbody.xml")
recording =True
# ## frameSize of recording has to be same size of the cam frame
# frame_size =(int(cap.get(3)),int(cap.get(4)))
# ## to save in mpg4
# fourcc=cv2.VideoWriter_fourcc(*'mpv4')
# # fourcc=cv2.VideoWriter_fourcc(*'MJPG')
# out= cv2.VideoWriter('video.mpv4',fourcc,20,frameSize=frame_size)

while True:
    ret,frame = cap.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiScale(frameGray,1.1,5)## 1 - 1.5 for accuracy make closer to 1, 5 is minimum number of neighbors How many number of overlapping boxes to be convinced its a face( make lower to pick up more faces, higher if picking up too many fake faces)
    # print(frame.shape)
    faces2=face_cascade2.detectMultiScale(frameGray,1.5,5)
    bodies=body_cascade.detectMultiScale(frameGray,1.5,5)
    # if len(faces)!=0:
    #     for face in faces:
    #         x,y,width,height=face
    #         # for (x,y,width,height) in faces:
    #         cv2.rectangle(frame,(x,y),(int(x+width),int(y+height)),(255,0,0),3)
    # # if len(faces)==0:
    # for face in faces2:
    #     x,y,width,height=face
    #     # for (x,y,width,height) in faces:
    #     cv2.rectangle(frame,(x,y),(int(x+width),int(y+height)),(255,0,0),3)
    
    if len(faces) + len(faces2) +len(bodies)> 0:
        recording =True
        
    
        out.write(frame)
    cv2.imshow('Camera',frame)
    if cv2.waitKey(1)== 27:
        break 
out.release()
cap.release()
cv2.destroyAllWindows()
