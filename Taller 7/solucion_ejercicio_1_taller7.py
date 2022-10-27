# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:06:52 2022

@author: JUAN S SAAVEDRA
"""


import numpy as np
import matplotlib.pyplot as plt

Matriz = np.array([[2,-1],[1,2],[1,1]])
Solucion  = np.array([[2,1,4]])

#primera parte 
E1 = lambda x :2*x-2
E2 = lambda x: (1-x)/2
E3 = lambda x : 4-x

lista = np.linspace(0,5,100)

def GetFit(A,b,n):
    
    B = b.T
    AT = np.dot(A.T,A)
    bT = A.T @ B

    xsol = np.linalg.solve(AT,bT)
    
    return xsol

Sol = GetFit(Matriz,Solucion,1)
print("las coordenadas de las solucion ( x,y ):" , GetFit(Matriz,Solucion,1))

plt.scatter(Sol[0],Sol[1])
plt.plot(lista , E1(lista))
plt.plot(lista , E2(lista))
plt.plot(lista , E3(lista))

#segunda parte

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
X = np.arange(-5, 5, 0.03)
Y = np.arange(-5, 5, 0.03)
X, Y = np.meshgrid(X, Y)
ax.set_xlabel ("X")
ax.set_ylabel ("Y")
ax.set_zlabel ("Distancia")

dis = np.sqrt((2*X-Y-2)**2+(X+2*Y-1)**2+(X+Y-4)**2) 
surf = ax.plot_surface(X, Y, dis,cmap = "coolwarm", rstride=1, cstride=1,linewidth=0, antialiased=False,)
ax.set_zlim(0, 22.5)
ax.view_init(7,45) #Se puede rotar el ángulo de cualquier manera, para observar que el punto rojo es solución.
                   #Es más visible si se cambia el segundo número y el primero se mantiene en 0.
menor = 5
for i in range(len(dis)):
    if min(dis[i]) < menor:
        menor = min(dis[i])
    
        
ax.scatter(Sol[0],Sol[1],menor,c='r')

