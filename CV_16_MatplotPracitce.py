'''
matplotlib quickstart guide
https://matplotlib.org/stable/users/explain/quick_start.html#sphx-glr-users-explain-quick-start-py

'''

import numpy as np

import matplotlib as mpl
import cv2 
import matplotlib.pyplot as plt
import os
image_path = os.path.join('.','images/butterfly.jpg')
img =cv2.imread(image_path,-1)
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)

# b = np.matrix([[1, 2,3], [3, 4,5]])
# b_asarray = np.asarray(b)
# print(b_asarray)
# print(b_asarray.shape)
# print(b_asarray.ndim)

# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# print(data)

cv2.imshow("IMAGE",img1)

plt.imshow(img)


plt.show()




           
cv2.waitKey(0) 
cv2.destroyAllWindows          
           