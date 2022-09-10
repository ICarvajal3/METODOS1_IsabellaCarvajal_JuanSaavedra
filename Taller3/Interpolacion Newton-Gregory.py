# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:08:27 2022

@author: JUAN S SAAVEDRA
"""

from numpy import sin,pi,linspace
from pylab import plot,show,subplot,axis
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

x = np.array([0,1.5,2,3.8,4.2,5.9])
y = np.array([-18 , -13 , 0 , 5 , 3 , 10])
lista = np.linspace(np.min(x),np.max(x),100)



def interpolación_newton (x , y): 
    
    n = len(x)
    a = []
    valores_a = np.zeros([n,n])
    for i in range (len(x)): 
        for j in range (len(y)): 
            if j == 0: 
                valores_a[i,j] = y[i]
            elif i < j:
                valores_a[i,j] = (y[j]-y[j-1])/(x[i]-x[i-1])
            else : 
                valores_a[i,j] = ( valores_a[i,j-1] - valores_a[i-1,j-1])/(x[i]-x[i-j])
            
            if i == j : 
                a.append(valores_a[i,j])
                
    return a 


def polinomio_newton (lista , x , y ): 
    
    a = interpolación_newton(x, y)
    suma = a[0]
    poly = 1.0
    
    for i in range(1,len(x)):
        
        poly *= ( lista - x[i-1] )
        suma += poly*(a[i])
    
    return suma 
    
w = sym.Symbol('x')
f = polinomio_newton(w,x,y)
f = sym.expand(f)
print("el polinomio de newton es:" , f)
valor = polinomio_newton(lista, x, y)

plt.plot(lista ,valor, color = "blue")
plt.scatter(x,y, color = "r")
plt.grid()
plt.ylabel("y")
plt.xlabel("x")
plt.title("Interpolacion de Newton-Gregory")
leyenda = plt.legend(["Data","Interpolación"] , title ="leyenda")


           