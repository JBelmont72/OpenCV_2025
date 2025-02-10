'''
https://www.geeksforgeeks.org/change-numpy-array-data-type/

Change the Data Type of the Given NumPy Array
NumPy arrays are homogenous, meaning all elements in a NumPy array are of the same data type and referred to as array type. You might want to change the data type of the NumPy array to perform some specific operations on the entire data set. 

In this tutorial, we are going to see how to change the data type of the given NumPy array. We will use the astype() function of the NumPy library to change the data type of the NumPy array.

NumPy astype() Method
The numpy.astype() method is used to change the data type NumPy array from one data type to another.

The function takes an argument which is the target data type. The function supports all the generic types and built-in types of data.
Syntax

Syntax: ndarray.astype(dtype, order=’K’, casting=’unsafe’, subok=True, copy=True)

Parameters:

dtype: The data type you want to change into.
order: Controls the memory layout order of the result. Options are ‘C’, ‘F’, ‘A’, ‘K’.
casting: Controls the type of data casting. Options are ‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’.
subok: If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array.
copy: By default, astype() returns a newly allocated array. If set to false, the input array is returned instead of a copy.
Return: The method returns a new array with new data typ

#    https://www.geeksforgeeks.org/change-numpy-array-data-type/  
# change the dtype to 'int84'
arr = np.array([10, 20, 30, 40, 50])
print(type(arr[0]))  
arr = arr.astype('int8') 
print(arr) 
print(type(arr[0]))

# print the data type 
print(arr.dtype)
print(arr[1])
for a in range(0,len(arr),1):
    print(arr[a])

'''
import cv2
import numpy as np
import random
frameHeight =512
frameWidth = 512
frame = np.zeros((frameHeight,frameWidth,3),dtype=np.int8)
zero = np.copy(frame)
# backColor = np.random.randint((30,30,30),(255,255,255),size =3)
# color =np.random.randint((0,0,0),(255,255,255),size = 3,dtype=np.uint8)
# rColor =np.random.randint(200,255,size =1,dtype=np.int16)

# frame[:,:]=[255,0,0]
rColor =np.random.randint(1,255,size =1,dtype=np.int16)
bColor =np.random.randint(1,255,size =1,dtype=np.int16)
rColor=int(rColor)
bColor=int(bColor)
print(rColor)
print(bColor)
frame[:,:]=[bColor,0,rColor]
# draw background
cv2.rectangle(frame,(frameWidth,200), (0, frameHeight), (bColor,100,rColor), -1)
# cv2.rectangle(bg,(width, ground_level), (0, height), green, -1)
while True:
    # imageBGR =cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    # frame = np.zeros([frameHeight,frameWidth,3],dtype=np.int16)
    cv2.rectangle(frame,(0,512),(256,512),9255,0,0,3)
    # rColor =np.random.randint(200,255,size =1,dtype=np.int16)
    # print(rColor[0])
    # print(type(rColor[0]))
    # rColor=int(rColor[0])
    # print(type(rColor))
    # color=[255,12,rColor]
    # cv2.rectangle(frame,(0,0), (380, 300), (255,255,0), -1)
    cv2.imshow('Frame',frame)
    cv2.imshow('Zero',zero)

    if cv2.waitKey(1) & 0xff ==ord('c'):
        break
    

cv2.destroyAllWindows()
