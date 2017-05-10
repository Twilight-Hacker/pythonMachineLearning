'''
Created on 24 Ìבס 2017

@author: Galadar
'''


import matplotlib.pyplot as plt
import time


plt.scatter(xV, yV, c=labelsV) #scatterplot, c for  colours
plt.plot([0, fun.calc((0,0))], [1, fun.calc((1,1))] , 'k-', lw=2) #plot a line on the previous plot
plt.show() #show the plot (BLOCKING FUNCTION)
            