# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:08:10 2022

@author: JUAN S SAAVEDRA
"""

from numpy import sin,pi,linspace
from pylab import plot,show,subplot,axis
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math

X = np.array([1.4 , 3.5 , 5.6])
Y = np.array([0.4007954931819738 ,0.594128102489774,0.29802795523938164 ])

def Lagrange(x,xi,yi):
    
    n = len(xi)
    poli = 0
    
    for i in range(n):
        num = 1 
        for j in range(n):
            if i != j:
                num *= (x - xi[j])/(xi[i]-xi[j] )
        poli += num*yi[i]
        
    return poli

x = np.linspace(np.min(X),np.max(X),100)
y = Lagrange(x,X,Y)
Coef = np.polyfit(X,Y,(len(X)-1))
theta = np.arctan(Coef[1])
theta_grados = np.degrees(theta)
vx = np.sqrt((1/2) * (-9.8/(Coef[0])))
print("vx es:" , math.ceil(vx))
print("theta es:" , round(theta_grados,0))


plt.plot(x,y)
plt.scatter(X,Y)
x = sym.Symbol('x')
f = Lagrange(x,X,Y)
f = sym.expand(f)
print("el polinomio de Lagrange es:" , f)