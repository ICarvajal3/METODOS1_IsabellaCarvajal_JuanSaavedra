# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 18:26:06 2022

@author: JUAN S SAAVEDRA
"""

from numpy import sin,pi,linspace
from pylab import plot,show,subplot,axis
import matplotlib.pyplot as plt
import numpy as np


phi = [0 , np.pi/4 , np.pi/2]
theta = linspace(0, 2*np.pi, 100)

for j in range (0,3):
    for i in range(1,6):
        for k in range(1,6):
            if  k >= i :
                
                y = sin(k*theta + phi[j])
                x = sin(i*theta)
                fig = subplot(6,5,i*5 + k)
                k+=1
                plt.axis("off")
                plot(x,y)
                
    plt.show()
             
                