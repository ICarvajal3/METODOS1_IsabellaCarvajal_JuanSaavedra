# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 15:11:51 2022

@author: JUAN S SAAVEDRA
"""


import numpy as np
import matplotlib.pyplot as plt


matriz1 = ([[1,0,0],[5,1,0],[-2,3,1]])
matriz2 = ([[4,-2,1],[0,3,7],[0,0,2]])

def producto_matrices(a, b):
    filas_a = len(a)
    columnas_a = len(a[-1])
    columnas_b = len(b[-1])
    
    if filas_a != columnas_b :
        return "Las matrices no son multiplicables"
    
    else:
        matriz_multi = np.zeros((columnas_b ,filas_a))

        for i in range(filas_a):
            for j in range(columnas_b):
                suma = 0
                for k in range(columnas_a):
                    suma += a[j][k]*b[k][i]
                    matriz_multi[j][i] = suma
                    
        return matriz_multi

print(producto_matrices(matriz1, matriz2))