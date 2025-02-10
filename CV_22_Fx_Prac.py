'''Zip Practice

'''


import cv2

python_fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'pink']

for fruit, color in zip(python_fruits, colors):
    print(fruit, color)
data1 = list(zip(python_fruits,colors))
print(data1)    
print('')
data1 = tuple(zip(python_fruits,colors))
print(data1)    
print('')
data1 = tuple(zip(python_fruits,colors))
print(data1)    
print('')
data1 = dict(zip(python_fruits,colors))
print(data1)    
print('')
python_fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'pink']
python_zipped = list(zip(python_fruits,colors))
print('this is python zipped: ',python_zipped)
print('This is how to unzip a file')

unzipped_fruits, unzipped_colors = zip(*python_zipped)

print(unzipped_fruits)
print(type(unzipped_colors))
print(type(unzipped_fruits))
print(unzipped_colors)

    
python_names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
countries = ['USA', 'UK', 'Canada', 'japan']
data = list(zip(python_names, ages, countries))

formatted_data = [f"Name: {name}, Age: {age}, Country: {country}" for name, age, country in data]
print(formatted_data) 
'''
Python zip() with enumerate

The combination of zip() and enumerate() is useful in scenarios where you want to process multiple lists or tuples in parallel, 
and also need to access their indices for any specific purpose.
'''

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
	print(i, name, age)
print(type(names))
print(names[0:2])
print('')
print('')
print('')
'''
Python zip() with Multiple Iterables

Python’s zip() function can also be used to combine more than two iterables. It can take multiple iterables as input and return an iterable of tuples, 
where each tuple contains elements from the corresponding positions of the input iterables.
'''
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
result = list(zipped)
print(result)
print('\n\n')
# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]
print('\n')
# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)
print("The end result of the zipped lists is:",mapped)
print("\n")

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)
'''The zipped result is : [('Manjeet', 4, 40), ('Nikhil', 1, 50), ('Shambhavi', 3, 60), ('Astha', 2, 70)]
the end result of the zipped lists is: [('Manjeet', 4, 40), ('Nikhil', 1, 50), ('Shambhavi', 3, 60), ('Astha', 2, 70)]
The unzipped result: 
The name list is : ('Manjeet', 'Nikhil', 'Shambhavi', 'Astha')
The roll_no list is : (4, 1, 3, 2)
The marks list is : (40, 50, 60, 70
'''
# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
	print("Player : %s	 Score : %d" % (pl, sc))
print('\n\n')


print("Exercises of the np.hstack()")
import numpy as np
x = np.array((3,5,7,4,5,22))
y = np.array((5,7,9))
a = np.hstack((x,y))
print(np.hstack((x,y)))
print(a)
print(len(a))
#array([3, 5, 7, 5, 7, 9])
'''n the above code there are two one-dimensional numpy arrays 'x' and 'y' with three elements each. By applying np.hstack((x,y)), we get a new one-dimensional numpy array that has all the elements of x and y stacked horizontally. The resulting numpy array has six elements in total.
np.hstack() is useful when we want to combine multiple numpy arrays horizontally. It can be used to concatenate multiple numpy arrays with the same number of rows, but different number of columns, into a single numpy array.
'''
import numpy as np
x = np.array([[3], [5], [7]])
y = np.array([[5], [7], [9]])
b=np.hstack((x,y))
print(b)
'''
[[ 3  5]
 [ 5  7]
 [ 7  9]
 The above code uses the numpy.hstack() function to horizontally stack two numpy arrays. The first array x is a column vector of shape (3,1) and the second array y is also a column vector of the same shape.
The numpy.hstack() function stacks the two arrays horizontally to produce a new 2-dimensional array of shape (3,2) where the elements of the first array appear in the first column and the elements of the second array appear in the second column.
The resulting array contains the elements [3, 5] in the first row, [5, 7] in the second row, and [7, 9] in the third row.
'''
print(dir(print)) # this gives all the methods for print method
print('\n\n')
print(dir('print')) # THIS GIVES ALL THE Methods for a string
  
    