# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:03:42 2022

@author: JUAN S SAAVEDRA
"""

from numpy import sin,pi,linspace
from pylab import plot,show,subplot,axis
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


function = lambda x : np.sqrt(1+ np.exp(-x**2))

def simpsons38(a, b, N, f):
    
    I = 0
    
    if N % 3 == 0 : 
         n = N
         narr = np.linspace(a, b, n+1)
         dx = (b - a)/n
    else : 
         n = N * 3
         narr = np.linspace(a, b, n+1)
         dx = (b - a)/n
    
    for i in range(int((n-3)/3)+1):

            I = I + 3*dx/8 * (f(narr[3*i]) + 3*f(narr[3*i + 1]) + 3*f(narr[3*i + 2]) + f(narr[3*i + 3]))

    return round (I , 10)

print(simpsons38(-1,1,100,function))







#def numero_pasos (f): 
 #   
  #  x = sym.Symbol('x',Real=True)
   # y = sym.Symbol('y',Real=True)
    
   #lista = np.linspace(-1,1,80)
    #p = sym.diff(f,x,4)
    #dx = lambda x : p
    #maximo = max(dx(lista))
    #b_a = (lista[-1]-lista[0])
    #E = ((-1-1)/80)*((b_a)**4)*maximo
    #n = (((b_a**5)*maximo/(E*180)))**(1/4)
    
    #return n

#print(numero_pasos(function))



