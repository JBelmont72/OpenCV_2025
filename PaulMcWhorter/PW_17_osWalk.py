'''CV_17.py  used os.walk to parse through path(root directory), folders(directories), and files and put them in a useabel form_
the form desired is the path of each photo and the name (sans '.jpg')
python -m venv .venv
source .venv/bin/activate

use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

The os.walk() method generates the file and directory names in a directory tree by walking the tree using top-down or bottom-up approach.

Each directory in the tree is rooted to the top directory. It yields a tuple that contains directory path, directories name and file name

The os.walk() method use os.scandir() method for produce listing

Syntax
os.walk(top, topdown=True, onerror=None, followlinks=False)

for pickling  work practice at bottom.  https://www.tutorialspoint.com/python-pickling
Pickling is the process through which a Python object hierarchy is converted into a byte stream. To serialize an object hierarchy, you simply call the dumps() function.

Unpickling is the inverse operation. A byte stream from a binary file or bytes-like object is converted back into an object hierarchy. To de-serialize a data stream, you call the loads() function.

Pickling and unpickling are alternatively known as serialization.
'''
import os
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
width=640
height=360
imageDir ='images/demoImages'
'''
os.walk it lists where it is( the root) 1st time will be imageDir, then all the folders in the directory and then all the folders inside the first foleder and the folders within each folder within each folder until it gets down to the files in each folder.
We want to return the 'root' (or path to the the folder/directory we want to start at)
Returns Root directory, directories(or Folders), and all the files
root is the present folder
dirs and files are arrays
'''

import os
###THis would print ALL the files with.py on my folder
# print("Listing Python file:")
'''
for dirpath, dirnames, filenames in os.walk("."):
   for filename in filenames:
      if filename.endswith(".py"):
         print(filename)

'''
### os.walk(dir)  root,dirs,files os.path.join(root,file), os.path.split(file)[0]
# for  root,dirs,files in os.walk(imageDir):
#     print('My working folder(root): ',root)
#     print('\nDIRS in root: ',dirs)
#     print('\nMy FIles in root: ',files)

#     for file in files:
#         print('Person Name is(with .jpg): ',file)
#         fullFilePath = os.path.join(root,file)
#         print('root:',root)
#         print(fullFilePath)
#         name = os.path.splitext(file)[0]
#         print(name)

            
  
    ##my solution to concatenate the file name with the path
    # for file in files:
    #     print(f'\n{file}')
    #     fullFilePath=os.path.join(root,file)
    #     print(fullFilePath)
    #     print('Person name is: ',os.path.splitext(file)[0])
    #     filePath = (root+'/'+str(file))
    #     print(filePath)
    ## want to get the path to each file and also the file names without the .jpg
   
# cam = cv2.VideoCapture(0)
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

#### pickle practice
# import pickle
# myDict={1:'Jan',2:'Jon',3:'Judson',4:'Sam',5:'Cheryl'}
# myList=['apples','oranges','peaches','pears']
# try:
#     with open('PaulMcWhorter/pickleData.pkl','wb')as f:
#         pickle.dump(myDict,f)
#         pickle.dump(myList,f)
        
#     pickle_off=open('PaulMcWhorter/pickleData.pkl','rb')
#     emp=pickle.load(pickle_off)
#     next=pickle.load(pickle_off)
#     print(emp)
#     print(next)
# except Exception as err:
#     print('ERROR: ',err)

# import pickle
# myDict={1:'Jan',2:'Jon',3:'Judson',4:'Sam',5:'Cheryl'}
# myList=['apples','oranges','peaches','pears']
# try:
#     with open('PaulMcWhorter/pickleData.pkl','wb') as file_handler:
#         pickle.dump(myDict,file_handler)
#         pickle.dump(myList,file_handler)
    
#     with open('PaulMcWhorter/pickleData.pkl','rb') as anything:
#         a= pickle.load(anything)
#         b=pickle.load(anything)

#     print(a,b)
# except Exception as err:
#     print('ERROR: ',err)
#######~~~~~~~~
import pickle
import math
myDict={1:'Jan',2:'Jon',3:'Judson',4:'Sam',5:'Cheryl'}
myList=['apples','oranges','peaches','pears']
mySet=(2,4,'first',True,False,0,0,1,1)
myPi=math.pi
file_handler=open('PaulMcWhorter/pickleData.pkl','wb')
pickle.dump(myDict,file_handler)
pickle.dump(mySet,file_handler)
pickle.dump(myPi,file_handler)
pickle.dump(myList,file_handler)
file_handler.close()  
# with open('PaulMcWhorter/pickleData.pkl','wb') as file_handler:
#     pickle.dump(myDict,file_handler)
#     pickle.dump(mySet,file_handler)
#     pickle.dump(myPi,file_handler)
#     pickle.dump(myList,file_handler) 
file_handle =open('PaulMcWhorter/pickleData.pkl','rb')
a=pickle.load(file_handle)  
b=pickle.load(file_handle)   
c=pickle.load(file_handle)   
d=pickle.load(file_handle)  
# with open('PaulMcWhorter/pickleData.pkl','rb') as file_handle:
#     a=pickle.load(file_handle)   
#     b=pickle.load(file_handle)   
#     c=pickle.load(file_handle)   
#     d=pickle.load(file_handle) 
print(a,b,c,d)
#######~~~~~~~~more ways to cycle through files of photos
###Iterate through Images Python


# https://www.geeksforgeeks.org/how-to-iterate-through-images-in-a-folder-python/

# https://stackoverflow.com/questions/70278475/python-converting-all-files-in-a-folder-to-jpg-but-only-jpg-and-png-should-be
# Purpose is to select only JPG files
# Becasue .DS_Store gets in the way of the os.walk
# Below is a second method to select multiple suffixes

# links to getting list of files in directory with size.list files in directory with extension, etc
# Another method:
# Method 2: Using  pathlib module
# At first, we imported the pathlib module from Path.
# Then we pass the directory/folder inside Path() function and used it .glob(‘*.png’) function to iterate through all the images present in this folder.






##import the modules
import os
from os import listdir
myArray=[]
# get the path/directory
folder_dir = "images/demoImages/known"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".jpg") or images.endswith(".jpeg")):
        print(images)
        print(os.path.splitext(images)[0])
        myArray.append(images)
        fullFilePath=os.path.join(folder_dir,images)
        print('full path for file: ',fullFilePath)
print(myArray)        
'''

# # import required module
# from pathlib import Path
 
# ### get the path/directory
# folder_dir = 'images/demoImages/known'
# myList=[]
# # ##iterate over files in
# # ##that directory
# images = Path(folder_dir).glob('*.jpg')
# for image in images:
#     print(image)
#     fullFilePath = os.path.join(folder_dir,image)
#     print(fullFilePath)
#     name = os.path.splitext(image)[0]
#     print(name)
#     myList.append(name) 
# print(myList)


# Example 2: Iterating through all kinds of images

# Here we have mentioned .png, .jpg, .jpeg files to be loaded using the endswith() function.


      

# import the modules
import os
from os import listdir
 
# get the path or directory
folder_dir = "C:/Users/RIJUSHREE/Desktop/Gfg images"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png or jpg or jpeg
    if (images.endswith(".png") or images.endswith(".jpg")\
        or images.endswith(".jpeg")):
        # display
        print(images)

'''
'''
Method 3: Using glob.iglob()
At first we imported the glob module.
Then with the help of glob.iglob() function we iterate through the images and print the names in order.
Here we have mentioned .png files to be loaded using the endswith() function

'''

# # import required module
# import glob
 
# # get the path/directory
# folder_dir = 'Gfg images'
 
# iterate over files in
# that directory
# for images in glob.iglob(f'{folder_dir}/*'):
   
#     # check if the image ends with png
#     if (images.endswith(".png")):
#         print(images)

