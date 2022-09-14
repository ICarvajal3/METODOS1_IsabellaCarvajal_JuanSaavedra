# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:13:19 2022

@author: isaca
"""
import mpmath
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0.1,1.1,100)
h=0.01

tan = lambda x: np.sqrt(np.tan(x))
f = tan(x)

def Progresiva(x,f,h):
    valores = []
    for i in range(0,len(x)-2): 
        deriv = ((-f(x[i+2])+4*f(x[i+1])-3*f(x[i]))/2*h)*10000
        valores.append(deriv)
    valores.append(0)
    valores.append(0)    
        
    return valores

def Progresiva2(x,f,h): 
        deriv = ((-f(x+2*h)+4*f(x+h)-3*f(x))/2*h)*10000
    
        return deriv


def Central(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)


DerivadaProgresiva = Progresiva2(x,tan,h)


DerivadaCentral = Central(x,tan,h)
Derivada = lambda x: 1/2*(1/(np.sqrt(np.tan(x))))*(1/np.cos(x))**2
DA= Derivada(x)

fig = plt.figure(figsize=(10,5))




plt.plot(x,DerivadaProgresiva, color = "orange")
plt.plot(x,DerivadaCentral , color = "red")
plt.plot(x,DA , color = "green")
plt.legend(["progresiva","Central","Analitica"])
plt.show()


plt.scatter(x,Derivada(x)-DerivadaProgresiva)
plt.scatter(x,abs(Derivada(x)-abs(DerivadaCentral)))
plt.legend(["Error progresiva" , "Error Central"])



print("Se observa que los dos metodos tienen el mismo orden de error")


