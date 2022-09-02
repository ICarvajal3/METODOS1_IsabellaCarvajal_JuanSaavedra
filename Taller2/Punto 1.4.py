# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 00:24:40 2022

@author: JUAN S SAAVEDRA
"""


import matplotlib.pyplot as plt
import numpy as np


X = np.linspace(-10,10,200)
print(len(X))
h = X[1]-X[0]
Kernel = [-1,0,1]

derivados = []
derivados.append(0)
function = lambda x : 1 / ((1+ np.exp(-x**2))**(1/2))
func_deriv = lambda x : ((np.exp(-2*x**2))*((x**2)-(2*np.exp(x**2)*(x**2))+(np.exp(x**2))+1))/((1+np.exp(-x**2))**(5/2))
derivada = lambda x,f,h : (f(x+h)-f(x-h))/(2*h)
for i  in range(len(X)-1):  
       valor = ((derivada(X[i-1],function,h)*Kernel[0])+(derivada(X[i],function,h)*Kernel[1])+(derivada(X[i+1],function,h)*Kernel[2]))/(2*h)
       derivados.append(valor)
              
error = abs(func_deriv(X)-derivados)
fig = plt.figure(figsize = (12,3))
ax = fig.add_subplot(1,2,1)
ax.plot(X,func_deriv(X) , color = "orange")
ax.scatter(X,derivados, color = "black")
plt.legend(["d2x/dx2 analitica","d2x/dx2 numérica"] )
plt.grid()
ax1 = fig.add_subplot(1,2,2)
ax1.plot(X , error)
plt.grid()
plt.legend(["Error"])


