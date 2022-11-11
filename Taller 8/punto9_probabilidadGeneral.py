# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:27:28 2022

@author: JUAN S SAAVEDRA
"""

import numpy as np
import matplotlib.pyplot as plt


P1 = np.linspace(0.1 , 0.9 , 1000)
P2 = np.linspace(0.1 , 0.5 , 1000)

#esta es la funcion para la probabilidad de 2 caras y 2 cruces 
probabilidad = lambda P1 , P2: (0.25*P1*P2)+(0.5*(1-P1)*P2)+(0.5*P1*(1-P2))+(0.25*(1-P1)*(1-P2))


def menor_probabilidad(P1,P2):
    min_= 3
    p1 = 0 
    p2 = 0 
    for i in range(len(P1)):
       
        x = probabilidad(P1[i],P2[i])
        if x < min_:
            min_ = x 
            p1 = P1[i]
            p2 = P2[i]
            
    return min_ , "p1 = "+ str(p1) , "p2 = "+ str(p2)

print("la menor probabilidad es :" , menor_probabilidad(P1, P2))


def mayor_probabilidad(P1,P2):
    max_= 0
    p1 = 0 
    p2 = 0 
    for i in range(len(P1)):
        x = probabilidad(P1[i],P2[i])
        if x > max_:
            max_ = x 
            p1 = P1[i]
            p2 = P2[i]
            
    return max_ , "p1 = "+ str(p1) , "p2 = "+ str(p2)

print("la mayor probabilidad es: " , mayor_probabilidad(P1, P2))

p1, p2 = np.meshgrid(P1,P2)
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(1,1,1,projection='3d')
superficie = ax.plot_surface(p1,p2,probabilidad(p1,p2),cmap = "coolwarm")
ax.set_xlabel("P1" , fontsize=18)
ax.set_ylabel("P2" , fontsize=18)
ax.set_zlabel("P(p1,p2)" , fontsize=15)
ax.view_init(10,200)
fig.colorbar(superficie , cmap = "colorwarm")







