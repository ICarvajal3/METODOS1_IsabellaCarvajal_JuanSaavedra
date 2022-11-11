# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:40:19 2022

@author: JUAN S SAAVEDRA
"""

import numpy as np
import matplotlib.pyplot as plt

Cable = 80/100
diario = 60/100
ambos = 50/100



#punto a) 

Probabilidad_cable = Cable 
Probabilidad_diario = diario
Probabilidad_ambos = ambos

#P(A U B) = P(A)+P(B)-P(A n B)

P = Probabilidad_diario + Probabilidad_cable - Probabilidad_ambos
print( "probabilidad a) = ", round(P, 5 ))


#punto b) 

#P(( A n BC ) U (B n AC)) = (P(A)*P(BC))+(P(B)*P(AC))-P(( A U BC ) n (B U AC))

BC = 1-Probabilidad_cable
AC = 1-Probabilidad_diario

P2 = Probabilidad_diario*BC + Probabilidad_cable*AC - (Probabilidad_diario*BC*Probabilidad_cable*AC)
print("probabilidad b) = " , round(P2,2))


