# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 00:07:29 2022

@author: JUAN S SAAVEDRA
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(size =10**4)


def correlacion ( x , N): 
    
    solucion = []
    
    for i in range ( 1, 30 ): #saca los valores de k
        multiplicador = 1
        suma = 0
        for j in range(N-30): #saca X
            multiplicador = x[j]*x[j+i]
            suma += multiplicador  
        c_k_i = suma/N
        solucion.append(c_k_i)
        
    return  solucion


plt.plot(correlacion(x,10**4))
plt.xlim(-1.5,30)
plt.ylim(0.2 , 0.3)
plt.ylabel("C(k)")
plt.xlabel("k")
plt.title("Generador numpy")
plt.grid()