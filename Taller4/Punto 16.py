# -*- coding: utf-8 -*-
"""
Created on Wed Sep  14 16:08:10 2022

@author: isaca
"""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

f= lambda x : np.exp(x)*x**3/ (np.exp(x)-1)

x=np.arange(2,10)


def gaussLaguerre(f,n):
    raiz,peso = np.polynomial.laguerre.laggauss(n)
    I = np.sum(peso*f(raiz))
    return I


def error(x,f):
    
    Vexacto= np.pi**4/15
    error=[]
    
    for n in x:
        e= gaussLaguerre(f,n)/Vexacto
        error.append(e)
        
    return error

Respuesta1= gaussLaguerre(f, 3)
print('Punto a) respuesta:', Respuesta1)
        
y = error(x,f)

plt.grid()
plt.scatter(x, y, color='r')
plt.legend(["Gauss-Laguerre error"])
plt.xlabel('n')
plt.ylabel('error(n)')