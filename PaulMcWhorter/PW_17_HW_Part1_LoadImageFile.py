'''Part1.py  pickles the known images and part 2.py  unpickles loads
line 85 starts my practice and attempts, worked well

python -m venv .venv
source .venv/bin/activate

use the 3.9.6 ('venv':venv)  version in the interpreter!!
we are going to use pickle to save the files
Pickle lesson   https://www.youtube.com/watch?v=eWrTSBIQess

one persons solution hard to read for me    https://www.youtube.com/watch?v=AOZCG8lcpqE
'''
'''
import pickle
import os
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
import face_recognition as FR
width=640
height=360
encodings = []
names = []
# in windows use a double \\  after the 'C:\\
imageDir ='images/demoImages/known'
'''
# os.walk it lists where it is( the root) 1st time will be imageDir, then all the folders in the directory and then all the folders inside the first foleder and the folders within each folder within each folder until it gets down to the files in each folder.
# We want to return the 'root' (or path to the the folder/directory we want to start at)
# Returns Root directory, directories(or Folders), and all the files

'''
for  root,dirs,files in os.walk(imageDir):
    # print('My working folder(root): ',root)
    # print('\nDIRS in root: ',dirs)
    # print('\nMy FIles in root: ',files)
    for file in files:
        # print('Person Name(with .jpg) is: ',file)
        fullFilePath = os.path.join(root,file)
        print(fullFilePath)
        myPicture = FR.load_image_file(fullFilePath)## loads the one image with the file name with path
        # print(type(myPicture),myPicture.shape)
        # want to encode one face in the one photo from the myPicture
        # this will encode the file in the 'myPicture'
        encoding =FR.face_encodings(myPicture)[0]       
        name = os.path.splitext(file)[0]
        print(name)
        encodings.append(encoding)
        names.append(name)
# with open('train.pkl','wb')as f:
with open('images/train.pkl','wb')as f:
    pickle.dump(names,f)
    pickle.dump(encodings,f)
      
    #     myPicture = FR.load_image_file(fullFilePath)
    #     myPicture = cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
    #     cv2.imshow(name,myPicture)
    #     cv2.moveWindow(name,0,0)
        
    # cv2.waitKey(2500)
    # cv2.destroyAllWindows
           
    
    #my solution to concatenate the file name with the path
    for file in files:
        print('Person name is: ,file)
        filePath = (root+'/'+str(file))
        print('')
        print(filePath)
    # want to get the path to each file and also the file names without the .jpg
'''    
# cam = cv2.VideoCapture(0)
# # cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

# while True:
#     ignore,  frame = cam.read()
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
    # if cv2.waitKey(1) & 0xff ==ord('q'):
    #     break
# cam.release()

########  my take 1, look below for take 2  images/demoImages/known,pickle path /Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_3/PaulMcWhorter/pickleData.pkl
# import cv2
# import pickle, os
# import numpy as np, face_recognition as FR
# rootDir='images/demoImages/known'
# pickleFile='/Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_3/PaulMcWhorter/pickleData.pkl'
# knownNames=[]
# knownPaths=[]
# for (root,dirs,files) in os.walk(rootDir):
#     print(root,dirs,files)
#     for file in files:
#         fullPathName=os.path.join(root,file)
#         print(fullPathName)
#         name=os.path.splitext(file)
#         name=name[0]
#         print(name)
#         # img=cv2.imread(fullPathName,-1)
#         # cv2.imshow(name,img)
#         # cv2.waitKey(2000)
#         # cv2.destroyAllWindows()
#         knownNames.append(name)
#         knownPaths.append(fullPathName)
    # print(knownNames)
    # print(knownPaths)
    
# with open(pickleFile,'wb')as file_handler:
#     pickle.dump(knownNames,file_handler)
#     pickle.dump(knownPaths,file_handler)
    
# with open(pickleFile,'rb')as f:
#     myKnownNames=pickle.load(f)
#     myKnownPaths=pickle.load(f)
      
# print('myKnownNames',myKnownNames) 
# print(f'\n{myKnownPaths}')
## example for one person loading facefile and encoding: penceFace=FR.load_image_file('images/demoImages/known/Mike Pence.jpg')
##      faceLoc=FR.face_locations(penceFace)[0]
##      penceFaceEncode=FR.face_encodings(penceFace)[0]
##### take two   encode the knownfiles and pickle

import cv2
import pickle, os
import numpy as np
import face_recognition as FR
rootDir='images/demoImages/known'
pickleFile='/Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_3/PaulMcWhorter/pickleData.pkl'
# knownNames=[]
# knownPaths=[]
# knownFaceEncodings=[]
# for (root,dirs,files) in os.walk(rootDir):
#     # print(root,dirs,files)
#     for file in files:
#         fullPathName=os.path.join(root,file)
#         # print(fullPathName)
#         name=os.path.splitext(file)
#         name=name[0]
#         # print(name)
#         # img=cv2.imread(fullPathName,-1)
#         # cv2.imshow(name,img)
#         # cv2.waitKey(2000)
#         # cv2.destroyAllWindows()
#         knownNames.append(name)
#         knownPaths.append(fullPathName)
#         knownFace=FR.load_image_file(fullPathName)
#         knownFaceLoc=FR.face_locations(knownFace)[0]
#         # print(knownFaceLoc)## returns the bounding box
#         knownFaceEncoding=FR.face_encodings(knownFace)[0]
#         knownFaceEncodings.append(knownFace)
#         # print(f'\nknownFaceEncoding: {knownFace.shape}')
        

# with open(pickleFile,'wb')as file_handler:
#     pickle.dump(knownNames,file_handler)
#     pickle.dump(knownFaceEncodings,file_handler) 
# with open(pickleFile,'rb')as f:
#     myKnownNames=pickle.load(f)
#     myKnownEncodings=pickle.load(f)

 
 ######## below I will unpickle the pickled knownName and knownPath
 ##### in pickleFile='/Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_3/PaulMcWhorter/pickleData.pkl' 
 ## use FR to compare with an unknownfile and then on Cam
# rootDir='images/demoImages/known'
# pickleFile='/Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_3/PaulMcWhorter/pickleData.pkl'
 
with open (pickleFile,'rb') as f:
    myKnownNames=pickle.load(f)
    myKnownEncodings=pickle.load(f)
# print('')   
# print('myKnownName',myKnownNames)
# print(f'\n\nmyKnownEncodings {myKnownEncodings}') 

### now I will open the camera and load my webcam and the image is unknownFace
cam=cv2.VideoCapture(1) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
print(cam.get(3))
print(cam.get(4))
while True:
    ret,unknownFace=cam.read()
    unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
    faceLocations=FR.face_locations(unknownFaceRGB)
    unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)
 
    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings): 
        top,right,bottom,left=faceLocation
        print(top,right,bottom,left)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),2)
        cv2.imshow('image',unknownFace) ## up to this point I have the rectangle around the unknown faces
    
    cv2.imshow('image',unknownFace)
    
    if cv2.waitKey(1) & 0xFF==27:
        break
cam.release()
cv2.destroyAllWindows()
 
 ## example for one person loading facefile and encoding: penceFace=FR.load_image_file('images/demoImages/known/Mike Pence.jpg')
##      faceLoc=FR.face_locations(penceFace)[0]
##      penceFaceEncode=FR.face_encodings(penceFace)[0]

