# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:39:42 2022

@author: JUAN S SAAVEDRA
"""


import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])

b = np.array([1.,3.,7.])


def GetacobiMethod(A,b,itmax=1000,error = 1e-10):
    
    M,N = A.shape
    
    x = np.zeros(N)
    
    sumk = np.zeros_like(x)
    
    x = [0,0,0]
    
    it = 0
    
    residuo = np.linalg.norm( b - np.dot(A,x) )
    
    while ( residuo > error and it < itmax ):
        
        it += 1
        
        for i in range(M):
            sum_ = 0
            for j in range(N):
                if i != j:
                     x[i] = (b[i]-sum(A[i][:i]*x[:i])-sum(A[i][i+1:]*x[i+1:]))/A[i][i]
 
      
        residuo = np.linalg.norm( b - np.dot(A,x) )
        
    return x, it , residuo

print(GetacobiMethod(A,b))