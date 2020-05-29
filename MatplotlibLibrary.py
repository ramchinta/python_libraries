import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# #Resize your graph
# plt.figure(figsize=(8,5) , dpi=100)
#
#
# # #Basic Graph
# x = [0,1,2,3,4]
# y = [0,2,4,6,8]
# # plt.plot(x,y, label = '2x',color = 'red',linewidth = 2,linestyle = '--' ,marker = '*',markersize = 5,markeredgecolor = 'blue') #Plots line, labels the line, colors the line
#
# # #Short hand notation
# # #Format = [color],[marker],[line]
# plt.plot(x,y, 'b*--',label = 'Reverse')
#
# # #Line 2
# x2 = np.arange(0,4.5,0.5)
# plt.plot(x2[:6],x2[:6]**2, 'r^-', label = 'x^2')
# plt.plot(x2[5:],x2[5:]**2, 'b--', label = 'Projected')
#
# plt.title("My first Graph!!", fontdict={'fontname': 'Comic Sans MS','fontsize':32}) #Label for the graph
# plt.xlabel('X-axis')  #Label for X-axis
# plt.ylabel('Y-axis')  #Label for Y-axis
#
# plt.xticks([0,1,2,3])  #Plots on x-axis
# plt.yticks([2,4,6,8,10])   #Plots on y-axis
#
# plt.legend()  #Plots the line in the graph
#
# plt.savefig('My First Graph.png')  ##Saves the graph
#
# plt.show() #Displays graph



# #Bar Chart
labels = ["A","B","C"]
values = [4,3,7]
bars = plt.bar(labels,values)

bars[0].set_hatch('/')
bars[1].set_hatch('|')
bars[2].set_hatch('*')


plt.show()




