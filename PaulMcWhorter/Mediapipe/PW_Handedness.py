'''
https://youtu.be/dux3KcKxtCw

we explore how to parse the data set returned from mediapipe to understand whether a given hand is a right hand or a left hand. Mediapipe has a method which determines the handedness of a found hand. We will show how to alter our data parsing class from earlier lessons to include the handedness of the found  hands. Enjoy!

help(mp.solutions.hands.Hands) this command gives all the arguemnents and cover handedness,etc
'''

import cv2
print(cv2.__version__)

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
     min_tracking_confidence=0.5)
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                print(hand)
                print(hand.classification)
                print(hand.classification[0])
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
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    frame=cv2.flip(frame,1)
    handData, handsType=findHands.Marks(frame)
    for hand,handType in zip(handData,handsType):
        # if handType=='Right':
        #     handColor=(255,0,0)
        # if handType=='Left':
        #     handColor=(0,0,255)
        ### if image flipped for camera, reverse right and left as below
        if handType=='Left':
            handColor=(255,0,0)
        if handType=='Right':
            handColor=(0,0,255)
        for ind in [0,5,6,7,8]:
            cv2.circle(frame,hand[ind],15,handColor,5)
            if  handType=='Left':
                cv2.putText(frame,'Left Hand',(hand[8][0],hand[8][1]),cv2.FONT_HERSHEY_SIMPLEX,2,(125,125,0),2)        
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()