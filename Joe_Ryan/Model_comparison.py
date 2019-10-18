# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy.random import normal
from numpy import pi, exp, sqrt, log, mean
import matplotlib.pyplot as plt

g = []

def f(x, N, m, s):
    d = (2*pi*(s**2))**(N/2)
    num = exp((-1/2)*sum((1/(s**2))*(x - m)**2))
    return num/d   

n = 10**4
pr = range(0, n, 1)
m1 = 1
s1 = 1
m2 = 1
s2 = 1.5

for p in pr:
    N = 100
    x = normal(1, 1, N)
    g.append(log(f(x, N, m1, s1))/log((f(x, N, m2, s2))))

#Theoretical average of ln(f1/f2):       
print((N/2)*(log(s2**2) - log(s1**2) + (s1**2)/(s2**2) + ((m2-m1)**2)/(s2**2) - 1))

y, bins, _ = plt.hist(g, 250)
bin_w = bins[1] - bins[0]
I = bin_w*(sum(y[0:249]))
rang1 = 250*bin_w
rang2 = max(x) - min(x)
print(I/rang1)
print(I/rang2)
print(mean(y))
plt.show()