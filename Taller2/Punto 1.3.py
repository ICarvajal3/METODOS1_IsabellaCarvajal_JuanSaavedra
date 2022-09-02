# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


X = np.linspace(-10,10,200)
h = X[1]-X[0]
Kernel = [-1,0,1]

derivados = []
derivados.append(0)
function = lambda x : 1 / ((1+ np.exp(-x**2))**(1/2))
func_deriv = lambda x : ((np.exp(-x**2))*x)/((1+np.exp(-x**2))**(3/2))
for i  in range(len(X)-1):  
       valor = ((function(X[i-1])*Kernel[0])+(function(X[i])*Kernel[1])+(function(X[i+1])*Kernel[2]))/(2*h)
       derivados.append(valor)
       
error = abs(func_deriv(X)- derivados)         

fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(1,2,1)
ax.plot(X,func_deriv(X) , color = "orange")
ax.scatter(X,derivados, color = "black")
plt.legend(["dx/dy analitica" , "dy/dx numérica"] )
plt.grid()

ax1 = fig.add_subplot(1,2,2)
ax1.plot(X , error)
plt.legend(["Error" ] )
plt.grid()