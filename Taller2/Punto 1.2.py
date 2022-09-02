# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 08:38:34 2022

@author: JUAN S SAAVEDRA
"""


import matplotlib.pyplot as plt
import numpy as np


h = 0.05
x = np.linspace(-10,10,100)
function = lambda x : 1 / ((1+ np.exp(-x**2))**(1/2))
func_deriv = lambda x : ((np.exp(-x**2))*x)/((1+np.exp(-x**2))**(3/2))
derivada = lambda x,f,h : (f(x+h)-f(x-h))/(2*h)
deriv = derivada(x,function,h)
error = abs(func_deriv(x)-derivada(x, function, h))

fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(1,2,1)
ax.plot(x,func_deriv(x), color = "blue")
ax.scatter(x,deriv,color = "orange")
plt.legend(["dx/dy analitica " , "dx/dy numérica"  ] )
plt.grid()
ax1 = fig.add_subplot(1,2,2)
ax1.plot(x , error)
plt.legend(["Error" ] )
plt.grid()