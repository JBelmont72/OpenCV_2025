'''PW_16_2_faceRecogENCODING and PW_16_TrainFaces.py are same and work Jan2025
In CV_16_3 will compare the faces loaded and encoded int CV_16_2.py and COMPARE them.
CV_16_1 this FINDS the face and displays it in a box. 
CV_16_2 will encode the face of any group (array)of people.  
WIll take an unknown photo with faces and encode each of those.
 
Note - we obtained the images from github/com/mcwhorpj
train openCV to detect and recognize faces. find and identify the ones it has been trained for.
(venv) judsonbelmont@Judsons-Air OpenCV_1 % python -m pip install
 face_recognition == 1.2.3
need to do first
1 download Python 3.6.8 64bit is what was recommended, i have 3.9.6
2 create a virtual environment 
3 download Cmake 3.21
4 download dlib  (i could not the 19.7 version so downloaded latest)
5 download face_recognition 1.2.3
python -m venv .venv
source .venv/bin/activate
USE 3.9.6 pyenv!!!!!!!
use the 3.9.6 ('venv':venv)  version in the interpreter!!
Note that the array for the face is an array within in array so as to accommodate multiple faces.
Note that the digits are first the Right SIde, then the Top, then bottom and then the left side!

note: if going to show images in OpenCV then have to be BGR!!
The Jpg files are RBG
so need to convert the RGB to gbr so we can show them in OpenCV
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
import face_recognition as FR
print(f"Face Recogniton Version: {FR.__version__}")
font = cv2.FONT_HERSHEY_SIMPLEX
donFace = FR.load_image_file('images/demoImages/known/Donald Trump.jpg')
faceLoc =FR.face_locations(donFace)[0]  #the zero is so we detect the first face
#HERE start encoding the face by the next line of code
donFaceEncode = FR.face_encodings(donFace)[0]
nancyFace = FR.load_image_file('images/demoImages/known/Nancy Pelosi.jpg')
faceLoc =FR.face_locations(nancyFace)[0]  #the zero is so we detect the first face
#HERE start encoding the face
nancyFaceEncode = FR.face_encodings(nancyFace)[0]
penceFace=FR.load_image_file('images/demoImages/known/Mike Pence.jpg')
faceLoc=FR.face_locations(penceFace)[0]
penceFaceEncode=FR.face_encodings(penceFace)[0]

# next two lines have two arrays, the third line will be an unknown face( we chose unkown face 3)

knownEncodings = [donFaceEncode,nancyFaceEncode,penceFaceEncode]
names= ['Donald Trump','Nancy Pelosi','Mike Pence']

#   add unknown photo of unknown faces if any
unknownFace =FR.load_image_file('images/demoImages/unknown/u5.jpg')
unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
# next step is to see if we can recognize the persons in the photo, an array of arrays with each array being a face location
# looks at the unknownFace and finds all the locations. will encode every face
#1 NOTE: find the locations of any faces in unknownFace
faceLocations =FR.face_locations(unknownFace)## remember FR works in RGB
# encode every face it finds in unknownFace.jpg with the faces located in the unknownEncodings

#2 NOTE:ENCODE those faceLocations that are found in unknownFace, 
unknownEncodings =FR.face_encodings(unknownFace,faceLocations)
#knownEncodings are the encodings of the people we know. unknwonEncodings are the encodings of the peole we don't know.
# FACELOCATIONS LOOKS for all the faces in unknownFace.
# encode every face found in 'unkownFace' and go to the face locations where the locations are of all the faces it finds.

# want to step through faceLocations and at same time the encodings. first has all the faceLocatons and for each faceLoaction there is a 
for faceLocation, unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left =faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(0,0,255),3)
    ## at this point a rectangle is around each face
    name='Unknown Person'
    matches =FR.compare_faces(knownEncodings,unknownEncoding,0.6)## one unknownEncoding cyles through the multiple unknownEncodings looking for a match
    print(matches)
    
    if True in matches: ## if anythong in the array matches is true:
        matchIndex=matches.index(True) ## if true then find the index of the array where the true is
        print(matchIndex)
        print(names[matchIndex])
        name=names[matchIndex]##if a match then name is the person, if not a match, use the 'unknown name' in the putText
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)

cv2.imshow('My Image',unknownFaceBGR)
# cv2.waitKey(5000)
cv2.waitKey(0)
    

cv2.destroyAllWindows()
# the below was from the first sketch and dealt with SHOWING the image with a box
'''
topLoc  = faceLoc[0]
rightLoc   = faceLoc[1]
bottomLoc= faceLoc[2]
leftLoc = faceLoc[3]

# he has top,right,bottom,left = faceLoc  
# top left = (leftLoc,topLoc)
# bottom right = (rightLoc,bottomLoc)
print(faceLoc)
print(faceLoc[0])
cv2.rectangle(donFace,(leftLoc,topLoc),(rightLoc,bottomLoc),(0,0,255),2,)
donFaceBGR=cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR)
cv2.imshow('My Image',donFaceBGR)
cv2.waitKey(5000)

'''