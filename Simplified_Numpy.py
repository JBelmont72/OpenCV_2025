''' python simplified tutorial
important resource
https://numpy.org/doc/stable/reference/routines.html
https://numpy.org/doc/stable/reference/arrays.html
https://realpython.com/np-linspace-numpy/#creating-ranges-of-numbers-with-uneven-spacing
code for the future
Rows, then columns
'''


import numpy as np

# a= np.zeros((3,3,1),dtype=np.uint64)
# a[:]=2
# print(a)
# print(np.shape(a))
# print(a.dtype)
# print('itemsize: ',a.itemsize)
# print('numberbytes ', a.size)
# print('numberbits ', a.nbytes)
# zero_dimensional=np.array(2345)

# two_dimen= np.array([[1,2,3],[4,5,6]])
# print(two_dimen)
# three_dimen = np.array([[[1,2,3],[4,5,6]]])
# print('three_dimen: ',three_dimen)
# print(np.shape(three_dimen))
# print(three_dimen.ndim)
# # Give an array any dimention you want!
# new_array =np.array(17,ndmin=5)
# print(new_array)
# new_array =np.array(([ (17,1,33),(11,1,2)] , [(17,1,33),(11,1,2)]),ndmin=5)
# print(new_array)
# print(np.shape(new_array))
# new_array =np.array(([[ (17,1,33)],[(11,1,2)] , [(17,1,33)],[(11,1,2)]]),ndmin=5)
# print(new_array)
# ## two ways to get array shape
# print(np.shape(new_array))
# print(new_array.shape)

# print(new_array.dtype)
# print(new_array[0][0][0][0][0])
# print('\n')

# new_array =np.array(([[ (17,1,33)],[(11,1,2)] , [(17,1,33)],[(11,1,2)]]),ndmin=3)
# print(new_array)
# ## two ways to get array shape
# print(np.shape(new_array))
# print(new_array.shape)

# print(new_array.dtype)
# print(new_array[0][0][0])
# new_array[3][0]=[1,1,1]
# print(new_array)
# print('\n')
# new_array[3][0][2]=(2)
# print(new_array)


# my_array = np.arange(8)
# print(my_array)
# my_array1 = np.arange(2,18,2)
# print(my_array1)
# print(type(my_array1))

# ## convert LISTS to ARRAYS

# list1 = [1,2,3,4]  # lists can store many types of datra but very inefficient with much memory
# from_list1 = np.array(list1)
# print(from_list1)
# print(type(from_list1))  #numpy.ndarray
# print(type(from_list1[0]))  #numpy.int64
# # will do the same but take up only 8 bits instead of 64 per digit
# from_list1 = np.array(list1,dtype=np.int8)
# print(from_list1)
# print(type(from_list1[0]))  #numpy.int8

# ## two dimensional array
# list2 = [[1,2,3,4],[5,6,7,8]]
# from_list2 = np.array(list2,dtype=np.int8)
# print(from_list2)
# print(type(from_list2[0][0]))  #numpy.int8
# print(from_list2[0][0])
# ## can also use a np.arrange()
# array_2d=np.array((np.arange(0,8,2),np.arange(1,8,2)))
# print(array_2d)
# array_2D = np.array(([1,2,3,4],[5,6,7,8]))
# print('array_2D: ', array_2D)
# print(np.shape(array_2D))
# ''' two rows , four columns  (2,4)
# [[0 2 4 6]
#  [1 3 5 7]]
# '''
# # to reshape
# array_2d =array_2d.reshape((4,2))
# print(array_2d)
# array_2d =array_2d.reshape((2,1,4))  ## 2 CHANNELS 1 ROW,4 COLUMNS (2,1,4)
# print(array_2d)
# print(np.shape(array_2d))
# array_2d =array_2d.reshape((1,2,4))  ## 1 CHANNELS 2 ROW,4 COLUMNS (2,1,4)
# print(array_2d)
# print(np.shape(array_2d))  
# '''
# [[[0 2 4 6]
#   [1 3 5 7]]]
# '''
# eye_array = np.eye(4,k=0)
# # eye_array[eye_array ==0] =4
# eye_array[eye_array <2] =9
# # eye_array = np.eye(3,k=0)
# print(eye_array)
# sorted_array = np.sort(eye_array,axis =0)
# ### copy arrays 
# my_view = sorted_array.view()
# my_copy = sorted_array.copy()

## accessing and changing elements
# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]],dtype=np.uint8)
# print(a)
# print('shape: ',a.shape)
# print(a.size)
# print(a.ndim)
# ## get a specific row,column
# a[1]=[11,12,13,14,15,16,17]
# print(a)
# a[:,3:]=(3)
# print(a)
# c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]],dtype=np.uint8)
# c[0:1,0:4]=(55)  # these two the same
# c[0:1,0:4]=[55,55,55,55]
# print(c)
# print(c[:,3:4]) #this gives the 3d column of all rows
# ## above gives the two values in a   2rows1 cololun  2X1 array 

# print(c[:,3]) #this gives the 3d column of all rows
# d =(c[:,3:4]) #this gives the 3d column of all rows
# ## above gives the two values in a   2rows1 cololun  2X1 array 
# print(d.shape)
# e =(c[:,3]) #this gives the 3d column of all rows
# ##  gives a  an array with just 2 values 1 dimension
# print(e.shape)
# # little more involved,   [start index: end eindex" stepsize]
# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]],dtype=np.uint8)
# print(a[0,1:6:2])   #all give same start at row 0 (index 1) and go to index 6 n 2 increments
# print(a[0,1:-1:2])      #[2 4 6]
# print(a[1,1:-1:2]) ## here started at roe 1 index 1 and wen tujp to column -1 in increments of 2
# print(a[1,1:-1:3]) ## here started at roe 1 index 1 and went up to column -1 in increments of 3
# ##############
# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]],dtype=np.uint8)
# print(a)
# print(a[:,3:5])
# a[:,3:5]=[21,23]
# print(a)
# print(a[1][6])
# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]],dtype=np.uint8)
# print(a.shape)
# print(a[3,4:])

# ## initializing all types of arrays 
# a = np.zeros((2,3,3))
# print(a)
# a[1:,:1,1:]=255

# print(a)

# b = np.ones((4,2,2),dtype=np.int16)
# print(b)
# c=np.full((2,2),99,dtype=np.int32)
# print(c)
# g = np.ones((3,1,3,1,1))
# print(g)
# d = np.full_like(g.shape,4) # not much use
# print(d)
# d = np.full_like(g,4,dtype=np.uint8) # not much use
# print(d)

# g[:]=5
# print(type(g))
# print(g.ndim)
# print(g.shape)
# RANDOM
# print(a)
# print(np.full_like(a,125))
# print(np.random.rand(4,2)) # this generates float numbers in an array that is 4 rows, 2 columns
# print(np.random.random_sample(a.shape))
# print(np.random.random_sample(a.size*2)) # probably not useful but fun( one element for every element of the original array, can  even multiply it)
# b=(np.random.random_sample(int(a.size*2))) # probably not useful but fun( one element for every element of the original array, can  even multiply it)
# # produced floats
# print('type of b: ',type(b[0]))
## TO OBTAIN RANDOM INTEGERS

# print(np.random.randint(2,4,4))
# i =122
# print(np.random.randint((int(i)),int((222)),4))
# d=(np.random.randint((int(i)),int((222)),4))
# print('type:',type(d[0]))  #  type: <class 'numpy.int64'>

# print(np.random.randint(7,100,size=(3,4),dtype=np.uint8)) # the first arguemt and the dtype are optional
# # identity matrix  , by default is square
# print('identity matrix: ',np.identity(5))
# g=(np.array([50,127,250]))

# ## REPEAR AN ARRAY
# print(np.repeat(a,4,axis=1))
# print(np.repeat(a,4,axis=1))

# output = np.ones((5,5),dtype=np.uint8) # otherwise are floats
# print(output)
# z =np.zeros((3,3))
# #can put a 9 in the middle
# z[1][1]=9

# print(z)
# output[1:4,1:4]=z
# output[1:-1,1:-1]=z # is the same as above
# print((output))
# print('be careful copying arrays!')
# a = np.array([1,2,3],dtype=np.int8)
# print(a)
#next two are same to copy an array
# b=np.copy(a)
# b =a.copy()
# print(b)

# b=a  #this does NOT creatre a copy but simply tells python to point to a when you call b
# # problem is tha tnow if you hange a value in b,  a ALSO GETYS CHANGED
# print(b)
## arrithmetic with arrays
# print(a*2)
# print(a**2)
# d=np.sin(a)
# print(d)
# print('##LINEAR ALGEBRA')
# s=np.ones((2,3),dtype=np.int64) # FLOAT UNLESS I SPECIFY DTYPE
# print('s:','\n',s)
# r=np.full((3,2),2)
# print('r full_matrix: ','\n', r)
# t=np.matmul(r,s)
# '''
# [[4. 4. 4.]
#  [4. 4. 4.]
#  [4. 4. 4.]] the three rows of the r times the three columns of the s
# '''
# print(t)
# q=np.matmul(s,r)
# print(q)
'''
[[6. 6.]
 [6. 6.]] the two rows of s times the two columns of r
'''

# c= np.identity(3)
# print(c)
# print(np.linalg.det(c)) # to find the determinant

# print('min : ',np.min(c))
# print('min : ',np.max(c))
# print('max axis : ',np.max(c,axis =1))
# print('min axis : ',np.min(c,axis =1))
# print("REORGANIZING ARRAYS")
# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(np.shape(before))
# print(np.ndim(before))
# print(np.size(before))
# after = before.reshape((1,8)) # as long as it multiplies out to same as np.size!
# print(after)
'''
https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random
Random Number Generators
The function numpy.random.default_rng will instantiate a Generator with numpy’s default BitGenerator.

'''

# rng = np.random.default_rng()
# print(np.random.default_rng())
# print(rng)
# # Generate one random float uniformly distributed over the range [0, 1)
# # rng.random()
# print(rng.random())  
# # #0.06369197489564249  # may vary
# # # Generate an array of 10 numbers according to a unit Gaussian distribution.
# print(rng.standard_normal(10))  
# #array([-0.31018314, -1.8922078 , -0.3628523 , -0.63526532,  0.43181166,  # may vary
# #        0.51640373,  1.25693945,  0.07779185,  0.84090247, -2.13406828])
# # Generate an array of 5 integers uniformly over the range [0, 10).
# print(rng.integers(low=0, high=10, size=5) ) 
# #array([8, 7, 6, 2, 0])  # may vary
# print(rng.integers(low=0, high=255, size=5) )
# import secrets
# print(secrets.randbits(128)) 
# print(np.linspace(0, 10, 3) + np.random.normal(size=3, scale=0.5))
# r = (0,10) ## range 
# num = 4 ## number of values

# x = np.linspace(r[0],r[1], num+1)
# s = x.shape[0] - 1
# y = np.zeros(s)
# print(x)

# for i in range(s):
#     low = x[i]
#     high = x[i+1]*num/(num+1) ## account for spacing 
#     y[i] = np.random.uniform(low=low, high=high, size=(1,1))
    
# print(y)

print(np.random.randint(2, size=10))
#array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random
print(np.random.randint(1,30, size=10))
#array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(np.random.randint(5, size=(2, 4)))

color =(np.random.randint((0,0,0),(255,255,255),size = 3))
print(color)
i=0
for i in range(i,3,1):
    print(color[i])
i=0    
for i in range(10):
    color =(np.random.randint((0,0,0),(255,255,255),size = 3))
    print(color)
    
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