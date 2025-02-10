'''
https://youtu.be/54PswFK6Agw
we show how to create python classes to parse the data coming from Mediapipe for hand Landmarks, Pose Landmarks and the bounding boxes for found faces. Creating these classes allows the difficult parsing to be done in the class, and then have a simple way to parse and use all the data.

stackovers for help https://stackoverflow.com/questions/78751176/tensorflow-lite-model-compatibility-issues-with-feedback-manager-and-onednn-cust


'''

import cv2
print(cv2.__version__)
import time
class mpFace:
    import mediapipe as mp 
    def __init__(self):
        self.myFace=self.mp.solutions.face_detection.FaceDetection()
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myFace.process(frameRGB)
        faceBoundBoxs=[]
        if results.detections != None:
            for face in results.detections:
                bBox=face.location_data.relative_bounding_box
                topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                faceBoundBoxs.append((topLeft,bottomRight))
        return faceBoundBoxs
 
class mpPose:
    import mediapipe as mp
    def __init__(self,static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5
    ):
        self.myPose=self.mp.solutions.pose.Pose(static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5)
    # def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5):
    #     self.myPose=self.mp.solutions.pose.Pose(still,upperBody,smoothData,tol1,tol2)
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks
 
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
     min_tracking_confidence=0.5)
        # self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                #print(hand)
                #print(hand.classification)
                #print(hand.classification[0])
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType
 
width=1280
height=720
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
 
findHands=mpHands(2)
findFace=mpFace()
findPose=mpPose()
print(findHands.__dict__)
font=cv2.FONT_HERSHEY_SIMPLEX
fontColor=(0,0,255)
pTime=0
cTime=0
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    # frame=cv2.flip(frame,1)
    handsLM,handsType=findHands.Marks(frame)
    faceLoc=findFace.Marks(frame)
    poseLM=findPose.Marks(frame)
    # print(findPose.__dict__)
    if poseLM != []:
        for ind in [13,14,15,16]:
            cv2.circle(frame,poseLM[ind],20,(0,255,0),-1)
            
        for ind in [19]:
            cv2.circle(frame,poseLM[ind],20,(0,255,255),-1)
            # print(poseLM[19])
 
    for face in faceLoc:
        cv2.rectangle(frame,face[0],face[1],(255,0,0),3)
    for hand,handType in zip(handsLM,handsType):
        if handType=='Right':
            lbl='Right'
        if handType=='Left':
            print(hand[8])
            lbl='Left'

        cv2.putText(frame,lbl,hand[8],font,2,fontColor,2)
        
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()