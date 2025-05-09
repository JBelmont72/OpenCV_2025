'''PW_16_2_faceRecogENCODING and PW_16_TrainFaces.py are same and work Jan2025
learn how to not only detect faces in an image, 
but also recognize who the person is. We start by training our model with known faces,
and then find and identify those faces in other pictures.


'''

import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
 
donFace=FR.load_image_file('images/demoImages/known/Donald Trump.jpg')
faceLoc=FR.face_locations(donFace)[0]
donFaceEncode=FR.face_encodings(donFace)[0]
 
 
nancyFace = FR.load_image_file('images/demoImages/known/Nancy Pelosi.jpg')
faceLoc=FR.face_locations(nancyFace)[0]
nancyFaceEncode=FR.face_encodings(nancyFace)[0]
 
penceFace=FR.load_image_file('images/demoImages/known/Mike Pence.jpg')
faceLoc=FR.face_locations(penceFace)[0]
penceFaceEncode=FR.face_encodings(penceFace)[0]
 
knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode]
names=['Donald Trump','Nancy Pelosi','Mike Pence']
 
unknownFace=FR.load_image_file('images/demoImages/unknown/u3.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknownFace)
unknownEncodings=FR.face_encodings(unknownFace,faceLocations)
 
for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left=faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name='Unknown Person'
    matches=FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex=matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name=names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)
 
cv2.imshow('My Faces',unknownFaceBGR)
 
cv2.waitKey(10000)