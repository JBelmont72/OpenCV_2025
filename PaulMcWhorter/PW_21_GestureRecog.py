'''
works great, i had to change the parameters for mp.pose to update accoridng to :
https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/pose.md
very helpful
'''
import cv2
print(cv2.__version__)
 
class mpPose:
    import mediapipe as mp
    '''mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5)
    '''
    def __init__(self,static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5):
        self.myPose=self.mp.solutions.pose.Pose(static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5)
    # def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5):
    #     self.myPose=self.mp.solutions.pose.Pose(still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5)
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks
 
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
     min_tracking_confidence=0.5)
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
 
width=1280
height=720
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
 
findHands=mpHands(2)
findPose=mpPose()
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    for hand in handData:
        for ind in [0,5,6,7,8]:
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    poseData=findPose.Marks(frame)
    if len(poseData)!=0:
        cv2.circle(frame,poseData[0],5,(0,255,0),3)
 
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()