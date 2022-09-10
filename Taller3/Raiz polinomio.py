# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:46:32 2022

@author: isaca
"""

from numpy import sin,pi,linspace
from pylab import plot,show,subplot,axis
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

polinomio = lambda x: 3*(x**5) + 5*(x**4)-(x**3)
function = lambda x: (5*(1-np.exp(-x)))-x
derivada = lambda f,x,h= 1*(10**-6): (f(x+h)-f(x-h))/(2*h)
X = np.linspace(-3,2,100)

plt.plot(X,polinomio(X))
plt.ylim(-2,8)
plt.axhline(0 , color = "r")
plt.grid()
plt.show()

def newton_raphson (f,fx,xn):
    
    error = 1 
    precision = 1*(10**-5)
    it = 1 
    it_max = 100
    while error > precision : 
        
        x_1 = xn - f(xn)/fx(f,xn)
        error = abs(f(xn)/fx(f,xn))
        #(x_1 - xn)/(x_1)
        xn = x_1
        
    if it == it_max: 
        return False 
    else : 
        return xn 
    
def total_raices(X,f,fx): 
    
    raices = np.array([])
    raiz = 0
    r = 1
    for i in X: 
        raiz = newton_raphson(f,fx,i)
        
        if raiz != False: 
            r = round(raiz,4)
            
            if r not in raices: 
                raices = np.append(raices,r)
    
    raices.sort()
    
    return (raices)

print(total_raices(X, polinomio , derivada))


