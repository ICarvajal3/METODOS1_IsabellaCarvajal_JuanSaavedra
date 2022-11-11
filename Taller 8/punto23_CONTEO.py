# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 10:15:56 2022

@author: JUAN S SAAVEDRA
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def combinacion_con_repeticion(r , n): 
    
    com =  np.math.factorial(n+r-1) / (np.math.factorial(r)*np.math.factorial(n-1))
    return com
  
    
combin = combinacion_con_repeticion(4, 3)

print("las posibles combinaciones son:" , combin-3)




