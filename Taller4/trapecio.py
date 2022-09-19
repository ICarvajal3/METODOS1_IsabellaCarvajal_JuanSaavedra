# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:21:15 2022

@author: JUAN S SAAVEDRA
"""

from numpy import sin,pi,linspace
from pylab import plot,show,subplot,axis
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym



ecuacion = lambda x: np.exp(-x**2)

derivada2 = lambda x,f,h=1*10**-6 : (f(x+h) - 2*f(x) + f(x-h))/h**2

def int_trapecio (f,x0,xn,n):
    
    x = np.linspace(x0,xn,n)
    error = 0.005
    h = x[-1]-x[0]
    inter = 0
    error = ((h**3)/(12*(len(x)-1)**2))*max(abs(derivada2(x, f)))
    for i in range( len(x)-1): 
        inter += ((x[i+1]-x[i])/2)*(f(x[i])+f(x[i+1]))
    if   error < 0.005:
        return inter , (error)
    else : 
        return "el error es mayor a 0.005"
    
print(int_trapecio(ecuacion,  0 , 1 , 7))


