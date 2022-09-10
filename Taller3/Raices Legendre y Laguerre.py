# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:30:11 2022

@author: isaca
"""

import numpy as np
import sympy as sym

derivada = lambda f,x,h= 1*(10**-6): (f(x+h)-f(x-h))/(2*h)
x1 = np.linspace(-1,1,100)
x2 = np.linspace(0,100,200)

def newton_raphson (f,fx,xn):
    
    error = 1 
    precision = 1*(10**-5)
    it = 1 
    it_max = 100
    while error > precision : 
        
        x_1 = xn - f(xn)/fx(xn)
        error = abs(f(xn)/fx(xn))
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



def Legendre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = (x**2-1)**n
    
    p = (sym.diff(y,x,n)/(2**n * np.math.factorial(n)))
    
    return p


def Laguerre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = sym.exp(-x)*x**n
    
    p = sym.exp(x)*sym.diff(y,x,n)/(np.math.factorial(n))
    
    return p


PolinomioLegendre = []
DerivPoliLegendre = []

x = sym.Symbol('x',Real=True)
n=20

for i in range(1, n+1):
    
    poly = Legendre(i)
    
    PolinomioLegendre.append(poly)
    DerivPoliLegendre.append(sym.diff(poly,x,1))
    

PolinomioLaguerre = []
DerivPoliLaguerre = []

x = sym.Symbol('x',Real=True)
n=20

for i in range(1, n+1):
    
    poly = Laguerre(i)
    
    PolinomioLaguerre.append(poly)
    DerivPoliLaguerre.append(sym.diff(poly,x,1))


def raiceslegendre(n,X,polinomio,dx):
    
    Raices = []
    
    x = sym.Symbol('x',Real=True)
    
    for i in range(0, (len(polinomio))):
        
        poli = sym.lambdify([x],polinomio[i],'numpy')
        derivada = sym.lambdify([x],dx[i],'numpy')
        Raices.append(total_raices(X,poli,derivada))
        print("Raíces del polinomio de Legendre grado", i+1, "son:", total_raices(X,poli,derivada))
    

print(raiceslegendre(20,x1,PolinomioLegendre,DerivPoliLegendre))


def raiceslaguerre(n,X,polinomio,dx):
    
    Raices = []
    
    x = sym.Symbol('x',Real=True)
    
    for i in range(0, len(polinomio)):
        
        poli = sym.lambdify([x],polinomio[i],'numpy')
        derivada = sym.lambdify([x],dx[i],'numpy')
        Raices.append(total_raices(X,poli,derivada))
        print("Raíces del polinomio de Laguerre grado", i+1, "son:", total_raices(X,poli,derivada))

print(raiceslaguerre(20,x2,PolinomioLaguerre,DerivPoliLaguerre))

