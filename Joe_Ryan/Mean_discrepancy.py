# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:37:50 2019

@author: Owner
"""

from numpy.random import normal
from numpy import mean, savetxt
import matplotlib.pyplot as plt
import sys

n = sys.argv[1]
syscount = 0

Px = []
Py = []
Nb = []

Nl = 10**4 #Number of samples in Gaussian distribution.
nl = 10**5 #Number of times the mean is sampled from the distribution.
for N in range(1, Nl+1, 1):
    syscount += 1
    px = 0
    py = 0
    if str(syscount) == n:
        break
    
for n in range(0, nl, 1):
    x = normal(1, 1, N) #Gaussian distribution with mean = 1, stdev = 1, N samples.
    y = normal(1.1, 1, N) #Gaussian distribution with mean = 1.1, stdev = 1, N samples.
    
    if mean(x) > mean(y):
        px += 1/nl #Probability that sample mean of x is greater than sample mean of y.
    if mean(x) <= mean(y):
        py += 1/nl    
if px < 0.01:
    Nb.append(N) #Records all N for which P(<x> < <y>) < 0.01.
    savetxt('temp_Nb_' + str(syscount) + '.dat', Nb)
    
Px.append(px)
Py.append(py)
    
savetxt('temp_Px_' + str(syscount) + '.dat', Px)
savetxt('temp_Py_' + str(syscount) + '.dat', Py)
savetxt('temp_Nb_' + str(syscount) + '.dat', Nb)

    
    
    
    
    