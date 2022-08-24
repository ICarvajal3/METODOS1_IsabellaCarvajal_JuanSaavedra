# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 23:31:58 2022

@author: JUAN S SAAVEDRA
"""

#Librerias importadas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Se importan los datos de Excel
Ruta = 'Datos_Tarea_METODOS3.xlsx' 
datos = pd.read_excel(Ruta, header = 0)
datos2 = np.array(datos)
dat = np.array(datos2[:,1])
dat2 = np.array(datos2[:,0])


lista_maximos = []
lista_x = []

for i in range(len(dat)-1):
      numero = 0
      if dat[i] > dat[i-1] and dat[i] > dat[i+1]: 
          numero = dat[i]
          lista_maximos.append(numero)
          lista_x.append(dat2[i])
    
print(lista_maximos)

plt.scatter(lista_x , lista_maximos, color = "red")
plt.plot(datos2[:,0], datos2[:,1])
plt.legend()
plt.grid()





