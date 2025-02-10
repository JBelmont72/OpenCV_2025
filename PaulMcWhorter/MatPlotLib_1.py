'''
lesson 9 of PW ai on the jetson nano
F made ut karge aand g creates a grud
'''
# import matplotlib.pyplot as plt 
# x=[1,2,3,4]
# y=[5,6,7,8]
# plt.grid(True)
# # plt.plot(x,y,':m*',linewidth=3)
# # plt.plot(x,y,'b-*',linewidth=2,markersize=10,marker=8)
# plt.plot(x,y,'b-^',linewidth=2,markersize=10,marker=8)
# plt.xlabel('My X values')
# plt.ylabel('My Y values')
# plt.title('My First Graph')
# plt.axis([0,5,0,10])        ## first tow are the x and the last two are y range
# plt.show()
###~~~
# import matplotlib.pyplot as plt 
# x=[1,2,3,4]
# y=[5,6,7,8]
# z=[10,8,6,4]
# plt.grid(True)
# # plt.plot(x,y,':m*',linewidth=3)
# # plt.plot(x,y,'b-*',linewidth=2,markersize=10,marker=8)
# plt.plot(x,y,'b-^',linewidth=2,markersize=10,marker=8,label='blue line')
# plt.plot(x,z,'r:o',linewidth=2,markersize=10,label='red line')
# plt.xlabel('My X values')
# plt.ylabel('My Y values')
# plt.title('My First Graph')
# plt.axis([0,5,0,12])        ## first tow are the x and the last two are y range
# # plt.legend()
# plt.legend(loc='lower center')
# plt.show()

####~~~~~~~~~~~~~~
# import matplotlib.pyplot as plt 
# import numpy as np
# # x=np.arange(-4,4,.1)
# x=np.linspace(-4,4,25)
# # y =x*x
# y=np.square(x)
# # y2 =x*(x+2)
# y2=np.square(x-2)
# # y3=x*(x-2)
# y3=np.square(x-4)
# plt.grid(True)
# # plt.plot(x,y,':m*',linewidth=3)
# plt.plot(x,y2,'r-*',linewidth=2,markersize=10,marker=8,label='red line')
# plt.plot(x,y,'b-^',linewidth=2,markersize=10,marker=8,label='blue line')
# plt.plot(x,y3,'m-^',linewidth=2,markersize=10,marker=8,label='magenta line')
# plt.xlabel('My X values')
# plt.ylabel('My Y values')
# plt.title('My First Graph')
# # plt.axis([-5,5,-2,12])        ## first two are the x and the last two are y range
# ### i can specify the axis as above or let it autoscale
# # plt.legend()
# plt.legend(loc='upper center')
# plt.show()
####~~~~~
import matplotlib.pyplot as plt 
import numpy as np
x=np.linspace(0,6*np.pi)
y=np.sin(x)
# y2=np.cos(x)
y2=np.cos(x-np.pi/2)


plt.grid(True)
# plt.plot(x,y,':m*',linewidth=3)
plt.plot(x,y2,'r-',linewidth=2,markersize=10,marker=8,label='red line')
plt.plot(x,y,'b^',linewidth=2,markersize=10,marker=8,label='blue line')
# plt.plot(x,y3,'m-^',linewidth=2,markersize=10,marker=8,label='magenta line')
plt.xlabel('My X values')
plt.ylabel('My Y values')
plt.title('My First Graph')
# plt.axis([-5,5,-2,12])        ## first two are the x and the last two are y range
### i can specify the axis as above or let it autoscale
# plt.legend()
plt.legend(loc='upper center')
plt.show()