'''

https://youtu.be/Vq9ctZGOBgI
https://toptechboy.com/tag/mediapipe/
In this video lesson we show you how you can improve the accuracy of your gesture recognition program developed in the last lesson. We do this by normalizing the hand landmarks distance matrix to a standard size. By doing this, you get accurate results independent of the distance your hand is from the camera. 

'''
# Lesson26 Gesture accurate   mediapipe THIS WORKS FINE!

# https://toptechboy.com/category/opencv/page/3/


import time
import cv2
print(cv2.__version__)
import numpy as np
 
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.width=1280
        self.height=720
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
     min_tracking_confidence=0.5)
 
    
    # def __init__(self,maxHands= 2,tol1=.5,tol2=.5):
    #     self.hands=self.mp.solutions.hands.Hands(  False,max_num_hands = 2, min_detection_confidence = .5, min_tracking_confidence=0.5)
    
    # def Marks(self,frame,draw=False):
    #     myHands=[]
    #     handsType=[]
    #     frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #     self.results=self.hands.process(frameRGB)
    #     if self.results.multi_hand_landmarks != None:
    #         #print(results.multi_handedness)
    #         for hand in self.results.multi_handedness:
    #             #print(hand)
    #             #print(hand.classification)
    #             #print(hand.classification[0])
    #             handType=hand.classification[0].label
    #             handsType.append(handType)
    #         for handLandMarks in self.results.multi_hand_landmarks:
                
    #             myHand=[]
    #             for landMark in handLandMarks.landmark:
    #                 myHand.append((int(landMark.x*self.width),int(landMark.y*self.height)))
    #             myHands.append(myHand)
    #             if draw:
    #                 self.mpDraw.draw_landmarks(frame,handLandMarks,self.mp.solutions.hands.HAND_CONNECTIONS)
    #     return frame,myHands,handsType
    
    
        
        
    def Marks(self,frame):
        myHands=[]
        frameRGB=  cv2.cvtColor ( frame, cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands
def findDistances(handData):
    distMatrix=np.zeros([len(handData),len(handData)], dtype='float')
    palmSize=((handData[0][0]-handData[9][0])**2+(handData[0][1]-handData[9][1])**2)**(1./2.)
    for row in range(0, len(handData)):
        for column in range(0, len(handData)):
             distMatrix[row][column]=(((handData[row][0]-handData[column][0])**2+(handData[row][1]-handData[column][1])**2)**(1./2.))/palmSize
    return  distMatrix
 
def findError( gestureMatrix,unknownMatrix,keyPoints):
    error=0
    for row in keyPoints:
        for column in keyPoints:
            error=error+abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    print(error)
    return error
def findGesture( unknownGesture,knownGestures,keyPoints,gestNames,tol):
    errorArray=[]
    for i in range(0, len(gestNames),1):
        error=findError(knownGestures[i], unknownGesture,keyPoints)
        errorArray.append(error)
    errorMin=errorArray[0]
    minIndex=0
    for i in range(0, len(errorArray),1):
        if errorArray[i]<errorMin:
            errorMin=errorArray[i]
            minIndex=i
    if errorMin< tol:
        gesture= gestNames[minIndex]
    if errorMin>= tol:
        gesture='Unknown'
    return gesture
 
 
width=1280
height=720
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set( cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set( cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)
time.sleep(5)
keyPoints=[0,4,5,9,13,17,8,12,16,20]
train=True
tol=10
trainCnt =0
knownGestures=[]
numGest =int(input('How Many Gestures Do You Want? '))
gestNames =[]
for i in range(0, numGest,1):

    prompt='Name of Gesture #'+str(i+1)+' '

    name=input(prompt)

    gestNames.append(name)
print( gestNames)
 
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,( width,height))
    # frame,handData,handsType = findHands.Marks(frame)
    handData=findHands.Marks(frame)
    if train==True:
        if handData!=[]:
            print('Please Show Gesture ',  gestNames [ trainCnt ],': Press t when Ready')
            if cv2.waitKey(1) & 0xff== ord('t'):
                knownGesture=findDistances(handData[0])
                print(knownGesture)
                knownGestures.append(knownGesture)
                trainCnt=  trainCnt+1
                if  trainCnt== numGest:
                    train=False
    if train == False:
        if handData!=[]:
            unknownGesture=findDistances(handData[0])

            myGesture=findGesture(unknownGesture, knownGestures,keyPoints,gestNames,tol)

            # error = findError( knownGesture, unknownGesture,keyPoints)

            cv2.putText(frame, myGesture,(100,175),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),8)
    for hand in handData:
        for ind in keyPoints:
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    cv2. imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()










'''
import time
import cv2
print(cv2.__version__)
import numpy as np
 
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands
def findDistances(handData):
    distMatrix=np.zeros([len(handData),len(handData)],dtype='float')
    palmSize=((handData[0][0]-handData[9][0])**2+(handData[0][1]-handData[9][1])**2)**(1./2.)
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            distMatrix[row][column]=(((handData[row][0]-handData[column][0])**2+(handData[row][1]-handData[column][1])**2)**(1./2.))/palmSize
    return distMatrix
 
def findError(gestureMatrix,unknownMatrix,keyPoints):
    error=0
    for row in keyPoints:
        for column in keyPoints:
            error=error+abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    print(error)
    return error
def findGesture(unknownGesture,knownGestures,keyPoints,gestNames,tol):
    errorArray=[]
    for i in range(0,len(gestNames),1):
        error=findError(knownGestures[i],unknownGesture,keyPoints)
        errorArray.append(error)
    errorMin=errorArray[0]
    minIndex=0
    for i in range(0,len(errorArray),1):
        if errorArray[i]<errorMin:
            errorMin=errorArray[i]
            minIndex=i
    if errorMin<tol:
        gesture=gestNames[minIndex]
    if errorMin>=tol:
        gesture='Unknown'
    return gesture
 
 
width=1280
height=720
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)
time.sleep(5)
keyPoints=[0,4,5,9,13,17,8,12,16,20]
train=True
tol=10
trainCnt=0
knownGestures=[]
 
numGest=int(input('How Many Gestures Do You Want? '))
 
gestNames=[]
 
for i in range(0,numGest,1):
    prompt='Name of Gesture #'+str(i+1)+' '
    name=input(prompt)
    gestNames.append(name)
print(gestNames)
 
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    if train==True:
        if handData!=[]:
            print('Please Show Gesture ',gestNames[trainCnt],': Press t when Ready')
            if cv2.waitKey(1) & 0xff==ord('t'):
                knownGesture=findDistances(handData[0])
                knownGestures.append(knownGesture)
                trainCnt=trainCnt+1
                if trainCnt==numGest:
                    train=False
    if train == False:
        if handData!=[]:
            unknownGesture=findDistances(handData[0])
            myGesture=findGesture(unknownGesture,knownGestures,keyPoints,gestNames,tol)
            #error=findError(knownGesture,unknownGesture,keyPoints)
            cv2.putText(frame,myGesture,(100,175),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),8)
    for hand in handData:
        for ind in keyPoints:
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
'''