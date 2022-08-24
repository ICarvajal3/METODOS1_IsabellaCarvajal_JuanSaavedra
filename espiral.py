# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:23:53 2022

@author: isaca
"""

import numpy as np
import matplotlib.pyplot as plt

theta= np.linspace(0,6*np.pi,100)


#print(theta)

def espiral(n):
    
    X= []
    Y= []
    
    a= 0
    b= 1
    r= 0
    
    for i in range(len(n)):
        
        rp= a+b*n[i]
        
        x= rp*np.cos(n[i])
        y= rp*np.sin(n[i])
        
        X.append(x)
        Y.append(y)
        
    imagen= plt.plot(X, Y, color="blue")
    
    
    
    return imagen
    
print(espiral(theta))




