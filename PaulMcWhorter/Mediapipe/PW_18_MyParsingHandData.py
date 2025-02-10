'''20 Jan 2025 Works
this has all three versions of mediapipe lesson 18 for hands=
1. straght program
2. with functtion
3 library mpHands  (i started including a logging module functionality)

Mandatory reading https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/hands.md

https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python
https://developers.google.com/mediapipe/solutions/guide
 Study this video  https://www.youtube.com/watch?v=qAw5tuYgVec
from 'code with price'

about using it on Python https://github.com/google/mediapipe/issues/2765

Plan_ watch videos by 'coding with Prince'
the https://developers.google.com/mediapipe/framework/getting_started/install
mdiapipe homepage is specific about using pythone 3.6 if want to use tensorflow.
Create a new Project with pythone 3.6 following the instructions in the Mediapipe homepage.

this is my version of parsing hand data
python -m venv .venv
source .venv/bin/activate

use the 3.9.6 ('venv':venv)  version in the interpreter!!
important note.  if I just activate the virtual environment , it goes to venv on python interpreteor
If I want to stay in the pyenv  then I MUST use the python -m venv .venv as the first command when I activate the virtual environment with source venv/bin/activate

Thank you. I am also working on a MAC (3.9.6 python_Mediapipe says python is  supported  up to 3.10). Running into a MAC related problem.  My webcam launches but the data is being directed to STDER which is apparently a MAC thing. Thus, the data points are not shown either by print() or on the webCam. The specific message is 'WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1707495418.390307 '  found a GitHub link https://github.com/abseil/abseil-py/issues/141 that addresses it but not in a way I can understand. Hoping you have crossed that hurdle. Any insights appreciated.

THis video is about python logging modules  https://www.youtube.com/watch?v=pxuXaaT1u3k
this was critical and not covered in PW tutorial:::
'hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
    min_tracking_confidence=0.5)'
'''
# import mediapipe as mp
# import sys
# import cv2
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)
# width= 1280  #640
# height= 720  #360
# cam = cv2.VideoCapture(1)
# # cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#     min_tracking_confidence=0.5)
# '''
# hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#     min_tracking_confidence=0.5)
#     the hands after mp.solutions references very specific methods.
#      THe .Hands is another method inside of mp.slolutons.hands.
     
    




# The problem with your code lies in line 11-12:
# self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
# The class Hands() takes in 5 arguments, but it seems like you have missed the "complexity" parameter.

# https://stackoverflow.com/questions/73409691/how-to-fix-an-opencv-ai-hands-critical-code-error-in-python
# here we are taking the data from the hands object (created by mp.solutions)
# and passing it over to the myDraw object (created by mp.solutions.drawing_utils)

# '''


# # hands =mp.solutions.hands.Hands(False,2,1,1)  # the false tells the method that the image is NOT static, but will move
# # he said that there are 'solutions' with lower case hands and uppercase Hands
# # the 2 is the number of hands   the .5 and .5 is level of confidence
# # to draw the hands follows:
# mpDraw = mp.solutions.drawing_utils     # this is to annotate the frame with the data, if want to analyze the frame TO DRAW HANDS  use the mp.solutions.hands.Hands(   , , )

# while True:
#     ignore,  frame = cam.read()
#     frame = cv2.resize(frame,(width,height))
#     frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     # the arrays of hand data come back in results.multi_hand_landmarks.  if = NOne +Go look for more hands.If not nothing then look further
#     results = hands.process(frameRGB)       # call the HANDS object and process it in RGB. reuslts is the object with lots of arrays
#     if results.multi_hand_landmarks != None:## the data in the multi_hand_landmarks are the arrays of handmarks in the results object, (actually for two hands in our case) 
#         for handLandMarks in results.multi_hand_landmarks:
#             # mpDraw.draw_landmarks(frame,handLandMarks)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
#             mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
#             print(handLandMarks)    ## above the mpDraw draws the landmarks on the frame(in RGB)
    
    
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('c'):
#         break
# cam.release()
######~~~~~~~~~tkae two- will try to parse the data structure
# import mediapipe as mp
# import sys
# import cv2
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)
# width= 1280  #640
# height= 720  #360
# cam = cv2.VideoCapture(1)
# # cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#     min_tracking_confidence=0.5)
'''
hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
    min_tracking_confidence=0.5)
    the hands after mp.solutions references very specific methods.
     THe .Hands is another method inside of mp.slolutons.hands.
     
    




The problem with your code lies in line 11-12:
self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
The class Hands() takes in 5 arguments, but it seems like you have missed the "complexity" parameter.

https://stackoverflow.com/questions/73409691/how-to-fix-an-opencv-ai-hands-critical-code-error-in-python
here we are taking the data from the hands object (created by mp.solutions)
and passing it over to the myDraw object (created by mp.solutions.drawing_utils)

'''


#  not correct== hands =mp.solutions.hands.Hands(False,2,1,1)  # the false tells the method that the image is NOT static, but will move
# he said that there are 'solutions' with lower case hands and uppercase Hands
# the 2 is the number of hands   the .5 and .5 is level of confidence
# to draw the hands follows:
# mpDraw = mp.solutions.drawing_utils     # this is to annotate the frame with the data, if want to analyze the frame TO DRAW HANDS  use the mp.solutions.hands.Hands(   , , )
# while True:
#     myHands=[]
#     ignore,  frame = cam.read()
#     frame = cv2.resize(frame,(width,height))
#     frame=cv2.flip(frame,1)
#     frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     # the arrays of hand data come back in results.multi_hand_landmarks.  if = NOne +Go look for more hands.If not nothing then look further
#     results = hands.process(frameRGB)       # call the HANDS object and process it in RGB. reuslts is the object with lots of arrays
#     if results.multi_hand_landmarks != None:## the data in the multi_hand_landmarks are the arrays of handmarks in the results object, (actually for two hands in our case) 
#         for handLandMarks in results.multi_hand_landmarks:
#             # mpDraw.draw_landmarks(frame,handLandMarks)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
#             # mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
#             # print(handLandMarks)    ## above the mpDraw draws the landmarks on the frame(in RGB)
#             myHand = []

#             for LandMark in handLandMarks.landmark:## 
#                 # print(int(LandMark.x*width),int(LandMark.y*height))
#                 # myHand.append((LandMark.x,LandMark.y))## must be a tuple to append
#                 myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
#             cv2.circle(frame,myHand[8],25,(255,255,0),2)
#             print(myHand[8])
#             myHands.append(myHand)
#             print(f'\n\n\n{myHands}')
#             cv2.imshow('my WEBcam',frame)
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('c'):
#         break
# cam.release()
####~~~~~~~~~~~~
# made the above program into a function=Works fine, 
# import sys
# import cv2
# print(cv2.__version__)
# import numpy as np
# print(f"This is version {sys.version}")
# print(np.__version__)
# import mediapipe as mp
# ###hands is global object
# hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#             min_tracking_confidence=0.5)
# mpDraw = mp.solutions.drawing_utils 
    
# def parseLandmarks(frame):
#     width= 1280  #640
#     height= 720  #360
#     frame = cv2.resize(frame,(width,height))
#     # frame=cv2.flip(frame,1)
#     frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     myHands=[]
#     results = hands.process(frameRGB)       # call the HANDS object and process it in RGB. reuslts is the object with lots of arrays
#     if results.multi_hand_landmarks  !=None:## the data in the multi_hand_landmarks are the arrays of handmarks in the results object, (actually for two hands in our case) 
#         for handLandMarks in results.multi_hand_landmarks:
#             # mpDraw.draw_landmarks(frame,handLandMarks)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
#             # mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
#             # print(handLandMarks)    ## above the mpDraw draws the landmarks on the frame(in RGB)
#             myHand = []

#             for LandMark in handLandMarks.landmark:## 
#                 # print(int(LandMark.x*width),int(LandMark.y*height))
#                 # myHand.append((LandMark.x,LandMark.y))## must be a tuple to append
#                 myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
#             # cv2.circle(frame,myHand[8],25,(255,255,0),2)
#             # print(myHand[8])
#             myHands.append(myHand)
#             print(f'\n\n\n{myHands}')
#     return myHands
# def main():

#     cam = cv2.VideoCapture(0)
#     cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#     cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
#     cam.set(cv2.CAP_PROP_FPS, 30)
#     cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
            
            
#     while True:
#         ignore,frame=cam.read()
#         frame=cv2.flip(frame,1)
#         myHands=parseLandmarks(frame)
#         print(myHands)
#         for hand in myHands:
#             for dig in [8,12,16,20]:
                
            
#                 cv2.circle(frame,hand[dig],25,(255,255,0),2)
#         cv2.imshow('my WEBcam',frame)
#         cv2.imshow('my WEBcam', frame)
#         cv2.moveWindow('my WEBcam',0,0)
#         if cv2.waitKey(1) & 0xff ==ord('c'):
#             break
#     cam.release() 
# main()
#### Make the def above into a class!!
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
import logging  
  
class mpHands:
    import mediapipe as mp
    def __init__(self,static_image_mode=False,max_num_hands=2,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
            min_tracking_confidence=0.5)
        self.mpDraw = self.mp.solutions.drawing_utils 
        var=self.hands
        logging.basicConfig(format='%(message)s')

        logging.warning(f'THis is my log message + var={var}')  
    def parseLandmarks(self,frame):
        width= 1280  #640
        height= 720  #360
        frame = cv2.resize(frame,(width,height))
        # frame=cv2.flip(frame,1)
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        myHands=[]
        results = self.hands.process(frameRGB)       # call the HANDS object and process it in RGB. reuslts is the object with lots of arrays
        if results.multi_hand_landmarks != None:## the data in the multi_hand_landmarks are the arrays of handmarks in the results object, (actually for two hands in our case) 
            for handLandMarks in results.multi_hand_landmarks:
                # mpDraw.draw_landmarks(frame,handLandMarks)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
                # mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)## we are moving each set of arrays to the method of the mpDraw objects method named 'draw-landmarks'
                # print(handLandMarks)    ## above the mpDraw draws the landmarks on the frame(in RGB)
                myHand = []

                for LandMark in handLandMarks.landmark:## 
                    # print(int(LandMark.x*width),int(LandMark.y*height))
                    # myHand.append((LandMark.x,LandMark.y))## must be a tuple to append
                    myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
 
                print(myHand[8])
                myHands.append(myHand)
                print(f'\n\n\n{myHands}')
        return myHands
def main():

    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
    cam.set(cv2.CAP_PROP_FPS, 30)
    cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
            
    myHandObject=mpHands()      
    while True:
        ignore,frame=cam.read()
        frame=cv2.flip(frame,1)
        frame=cv2.resize(frame,(1280,740))
        myHands=myHandObject.parseLandmarks(frame)
        print(myHands)
        for hand in myHands:
            cv2.circle(frame,hand[8],25,(255,255,0),2)
            for i in [4,8,12,16,20]:
                cv2.circle(frame,hand[i],20,(125,125,0),3)
        cv2.imshow('my WEBcam',frame)
        cv2.imshow('my WEBcam', frame)
        cv2.moveWindow('my WEBcam',0,0)
        if cv2.waitKey(1) & 0xff ==ord('c'):
            break
    cam.release() 
if __name__=='__main__':
    print('running on main')
    main()