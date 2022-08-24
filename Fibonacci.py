# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:17:36 2022

@author: isaca
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim



def sucesion(n):
    

    numeros = np.linspace(2,n,n-2)

    numeros2 = np.linspace(0,n,n)

    lista_numeros=[]
    
    f0 = 0
    f1 = 1
    i = 1
    
    lista_numeros.append(f0)
    lista_numeros.append(f1)
    
    for i in range(len(numeros)):
        f= f0+f1
        f0= f1
        f1=f
        
        i+=1
        
        lista_numeros.append(f)
        
    
    return lista_numeros

plt.plot(sucesion(20), color = "black")
plt.show()
print(sucesion(20))

def aureo(x):
    
    lista = sucesion(x)
    lista_num_aureo = []
    #i = 1
    #au = n[len(n)-1]/(n[len(n)-2])
    
    for j in range(1, len(lista)-1):
            
          au= lista[j+1]/lista[j]
          lista_num_aureo.append(au)
    j+=1
     
    return lista_num_aureo

numero_aureo = ((1+((5)**(1/2)))/2)
imagen_2 = plt.plot(aureo(20), color = "green")
plt.axhline(numero_aureo, linestyle = "--", color = "red" )
plt.grid()
plt.show()
