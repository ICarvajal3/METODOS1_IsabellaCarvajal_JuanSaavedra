# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:49:01 2022

@author: JUAN S SAAVEDRA
"""

from numpy import sin,pi,linspace
from pylab import plot,show,subplot,axis
import matplotlib.pyplot as plt
import numpy as np

N = 25
x = np.linspace(-4,4,N )
y = np.linspace(-4,4,N )
h = 0.001


X,Y = np.meshgrid(x,y)
def GetCharges(N=2):
    
    Q = np.zeros(N)
    r = np.zeros((N,2))
    
    Q[0] = 1
    Q[1] = -1
    
    r[0] = [0.05,0.1]
    r[1] = [0.05,-0.1]
    
    for i in range(N):
        r[i] = [ 2*np.cos( 2*np.pi*i/N ), 2*np.sin( 2*np.pi*i/N ) ] 
        Q[i] = 1
    
    return Q,r

Q,rq=GetCharges(1000)

def Potencial ( x, y ): 
    return  2*x*(1-((2**2)/(x**2 + y**2)))
     
             
derivadaCx= lambda  x,f,h,y :  (f(x+h , y )-f(x-h , y ))/(2*h)

derivadaCy= lambda  x,f,h,y :  -(f(x,y+h )-f(x,y-h ))/(2*h)


def campo(x,y):
    
  
    campo_x = derivadaCx(x,Potencial,h,y)
    campo_y = derivadaCy(x,Potencial,h,y)
        
    return campo_x,campo_y

u = 1.6

def GetField(x,y):
    
    Ex = np.zeros((N,N))
    Ey = np.zeros((N,N))
    
    for i in range(N):
        for j in range(N):
            if x[i]<=-u or x[i] >=  u or y[j]<=-u or y[j]>=u:
                Ex[i,j],Ey[i,j] = campo(x[i],y[j])
            
    return Ex,Ey

Ex,Ey = GetField(x,y)

fig = plt.figure(figsize=(8,3))
ax = fig.add_subplot(1,2,1)

for i in range(N):
    for j in range(N):
        ax.quiver(x[i],y[j],Ex[i,j],Ey[i,j],color='blue',alpha=0.7)
        
ax.scatter(rq[:,0],rq[:,1],color='r',s=0.1)
ax1 = fig.add_subplot(1,2,2)
ax1.streamplot(X,Y,Ex.T,Ey.T)
