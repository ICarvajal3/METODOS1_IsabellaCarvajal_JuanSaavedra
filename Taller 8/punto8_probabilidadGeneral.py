# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:40:06 2022

@author: JUAN S SAAVEDRA
"""
import numpy as np
import matplotlib.pyplot as plt


def proba(n):
    
    Ntimes = 0
    
    Moneda= [-1,1]
    
    
    for i in range(int(n)):
        
        m = np.random.choice(Moneda)
        m2 = np.random.choice(Moneda)
        m3 = np.random.choice(Moneda)
        m4 = np.random.choice(Moneda)
        
        if m+m2+m3+m4 == 0:
            Ntimes += 1
    
    return Ntimes/n

print("la probabilidad de tener dos caras y dos sellos es : " ,proba(10**5))


