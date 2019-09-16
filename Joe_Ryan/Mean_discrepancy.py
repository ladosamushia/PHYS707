# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:37:50 2019

@author: Owner
"""

from numpy.random import normal
from numpy import mean
import matplotlib.pyplot as plt

Px = []
Py = []
Na = []
Nb = []

Nl = 10**4
nl = 10**2
for N in range(1, Nl+1, 1):
    Na.append(N)
    px = 0
    py = 0
    print(N)
    
    for n in range(0, nl, 1):
        x = normal(1, 1, N)
        y = normal(1.1, 1, N)
        
        if mean(x) > mean(y):
            px += 1
        if mean(x) <= mean(y):
            py += 1    
    if (px/nl) < 0.01:
        Nb.append(N)
    
    Px.append(px/nl)
    Py.append(py/nl)
       
plt.plot(Na, Px, label='$P(\mu_x > \mu_y)$')
plt.plot(Na, Py, label='$P(\mu_y > \mu_x)$')
plt.plot([0, 1000], [1, 1])
plt.plot([0, 1000], [0, 0])
plt.legend(loc='lower right', bbox_to_anchor=(0.95, 0.35), prop={'size':12}) # << mcase 3
plt.show()
        
print(min(Nb))


    
    
    
    
    