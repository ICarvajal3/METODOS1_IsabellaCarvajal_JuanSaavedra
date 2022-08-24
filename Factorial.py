# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:36:52 2022

@author: isaca
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def factorial(n):
    
    numeros = np.linspace(1,n,n)
    lista_factoriales=[]

    fac = 1
    i = 1
    j = 1
    
    for i in range(n+1):
        
        while j <= i:
            fac= fac*j
            
            lista_factoriales.append(fac)
            j+=1
        
        i+=1
    #while i <= n:
    #    fac= fac*i
     #   i+=1
    
    return lista_factoriales

print(factorial(20))

def factorial2(n):
    fac = 1
    i = 1
    
        
    while i <= n:
        fac= fac*i
        
        i+=1
    
    return fac

def variaciones(n,r):
    
    factorial2(n)

    
    V = factorial2(n)/factorial2(n-r)
    
    return V

print("El numero de Varaiaciones es:" , variaciones(6, 3))

def combinacion(n,m):
    
     factorial2(n)
     
     C = factorial2(n)/(factorial2(n-m)*factorial2(m))
     
     return C
 
print("El numero de Combinaciones es:" , combinacion(21, 11))


     


    

        