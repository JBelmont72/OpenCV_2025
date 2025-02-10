import matplotlib.pyplot as plt

import numpy as np
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# # plt.plot(x, y)
# fig, ax = plt.subplots()
# ax.plot(x, y)
'''matplotlib.pyplot.title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs)[source]#
Set a title for the Axes.

Set one of the three available Axes titles. The available titles are positioned above the Axes in the center, flush with the left edge, and flush with the right edge.
the defajult fontdict is {'fontsize': rcParams['axes.titlesize'],
 'fontweight': rcParams['axes.titleweight'],
 'color': rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}

'''

# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)

x= [0,1,2,3,4]
y=[0,2,4,6,8]
# # plt.plot(x,y)
# plt.plot(x,y,label = '2X',color = 'magenta',linewidth= 2,marker='*',linestyle ="--",markersize =20,markeredgecolor ='fuchia ')
x2 =np.arange(0.4,0.5)
print(x2)
plt.plot(x2,x2**2)
plt.title('My graph!!',loc = 'left',fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('X_ Axis')
plt.ylabel('Y_ Axis')


# fig, axs = plt.subplots(1,3, layout='constrained')

# ax = axs[0]
# ax.plot(range(10))
# ax.xaxis.set_label_position('top')
# ax.set_xlabel('X-label')
# ax.set_title('Center Title')



# ax = axs[1]
# ax.plot(range(10))
# ax.xaxis.set_label_position('bottom')
# ax.xaxis.tick_top()
# ax.set_xlabel('X-label')
# ax.set_title('Another Center Title')
# ax =axs[2]
# ax.plot(range(100))

# ax.xaxis.set_label_position('top')
# ax.xaxis.tick_bottom()
# ax.set_xlabel(('more X=label'))
plt.show()