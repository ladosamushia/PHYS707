# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:20:33 2019

@author: Owner
"""

import matplotlib.pyplot as plt
from numpy import loadtxt

Px = loadtxt('Px_2.dat', unpack=True)
Py = loadtxt('Py_2.dat', unpack=True)

Na = []
for N in range(1, 10000+1, 1):
    Na.append(N)
print(len(Na))
    
Nb = loadtxt('Nb.dat', unpack=True)

plt.plot(Na, Px, label='$P(\mu_x > \mu_y)$')
plt.plot(Na, Py, label='$P(\mu_y > \mu_x)$')
plt.plot([0, 2000], [1, 1], linestyle='--', color='k') #Asymptotic probability
plt.plot([0, 2000], [0, 0], linestyle='--', color='k') #Asymptotic probability
plt.ylim(-0.05, 1.05)
plt.xlim(0, 2000)
plt.xlabel('N')
plt.ylabel('Probability')
plt.legend(loc='lower right', bbox_to_anchor=(0.85, 0.4), prop={'size':12})
plt.savefig('Mean_discrepancy_plot.pdf')

print(min(Nb))