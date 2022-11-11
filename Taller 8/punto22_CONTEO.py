# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:06:11 2022

@author: JUAN S SAAVEDRA
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#opcion 1 

lista = [0,1,2,3,4,5,6,7,8,9,10]


n = 200000
Ntimes = 0

combinaciones = []

for i in range(int(n)):
        
        m = np.random.choice(lista) 
        m2 = np.random.choice(lista)
        m3 = np.random.choice(lista)
        
        if m+m2+m3 == 10 : 
            Ntimes += 1 
            combinaciones.append([m,m2,m3])
            

for combinacion in combinaciones: 
    while combinaciones.count(combinacion) > 1: 
        combinaciones.remove(combinacion)
    
#print(combinaciones)
print(len(combinaciones))    


#opcion 2 


def combinacion_con_repeticion(r , n): 
    
    com =  np.math.factorial(n+r-1) / (np.math.factorial(r)*np.math.factorial(n-1))
    return com
  
    
combin = combinacion_con_repeticion(10, 3)
print(combin)

