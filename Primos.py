# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:33:07 2022

@author: JUAN S SAAVEDRA
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#numeros = np.linspace(0,8000,8001)
def primos (n):
    
    h = n*n+2
    lista = []
    lista_posicion = []
    lista.append(2)
    
    for j in range(2,h):
        eu = False
        for i in range (2,h): 
            if  i <= j : 
            #print("i=",i)
                if j%i == 0:
                    eu = True
                    break
                if eu == False and len(lista)<n and i == j - 1: 
                    lista.append(j) 
            
    for k in range (0, len(lista)): 
        lista_posicion.append(int(k))
            
    imagen = plt.scatter(lista_posicion, lista , color = "green")
            
    return imagen , lista[0:10]

print(primos(1000))
