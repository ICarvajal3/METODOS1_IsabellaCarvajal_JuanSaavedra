# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:08:38 2022

@author: JUAN S SAAVEDRA
"""

import numpy as np
import matplotlib.pyplot as plt

I = 1/100
n = 1/(I**2)

limites = np.linspace(0,1,1000)

Ro = lambda x : np.math.factorial(x-1)
function = lambda x , a = 2 , B = 4: (Ro(a+B)/(Ro(a)*Ro(B)))*(x**(a-1))*((1-x)**(B-1))
x = np.random.uniform(0,1,size=int(n))
maximo = max(function(x))
y = np.random.uniform(0, maximo, size=int(n))

lista = []
for i in range(len(x)): 
    if y[i] < function(x[i]): 
        lista.append(x[i])
valores = lista
area = (maximo*len(lista))/len(x)
plt.plot(limites , function(limites))
#plt.plot(valores , function(valores))
plt.grid()
print("El area bajo la curva es:" , area , "Con una incertidumbre del 1%")