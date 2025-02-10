'''

https://youtu.be/Y7Tww4fu5m8
Gesture based game
in zip
l1=['left','right','left','right']
# l1 = [[1, 2], [3, 4], [5, 6],[7,8]]
l2=  [[7, 8], [9, 10], [11, 12],[13,14]]

 # Zipping list
# res = [(a, b) for a, b in zip(l1, l2)]
# print(res)
for handType,hand in zip(l2,l1):
    # print(hand,handType)
    # print(type(hand),'   ',type(handType))
    if hand =='left':
        print('left handtype: ',hand,handType)
        
         # Zipping list
res = [(a, b) for a, b in zip(l1, l2) if 'left' in a]
print(res)

'''

# import cv2
# print(cv2.__version__)
 
# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#      min_tracking_confidence=0.5)
#         # self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
#         return myHands
 
# width=1280
# height=720
# cam=cv2.VideoCapture(1)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# findHands=mpHands(2)
# paddleWidth=125
# paddleHeight=25
# paddleColor=(0,255,0)
# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handData=findHands.Marks(frame)
#     for hand in handData:
#         cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()
########~~~~~~~~~my version 22 Jan 2025
import cv2
print(cv2.__version__)
 
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
     min_tracking_confidence=0.5)
        # self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        myHandTypes=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
                
            for hand in results.multi_handedness:
                myHandType=[]
                # print(hand)
                # print(hand.classification)
                # print( f"{hand.classification[0].index} is {hand.classification[0].label}")
                myHandType=hand.classification[0].label
                # myHandTypes.append(hand.classification[0].label)
                myHandTypes.append(myHandType)
                
        
        
        
        
        return myHands,myHandTypes
 
width=1280
height=720
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
paddleWidth=125
paddleHeight=25
paddleColor=(0,255,0)
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData,myHandTypes=findHands.Marks(frame)
    for hand in handData:
        # print(hand)
        cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)

    for hand,handType in zip(handData,myHandTypes):
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