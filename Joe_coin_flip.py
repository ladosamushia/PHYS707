# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import matplotlib.pyplot as plt
from numpy import arange

a = []
N = 10**2
N2 = 10**6

P55 = 0
P45 = 0
Pe = 0
Narr = []
xx = []

for x in range(N2):
    xx.append(x)
    for y in range(N):
        b = random.randint(0, 1)
        a.append(b)
    
    if a.count(1) > 55:
        P55 += 1
    if a.count(1) < 45:
        P45 += 1
    else:
        Pe += 1
    Narr.append(1 - Pe/(P45 + P55 + Pe))
    a = []
    
print(P55/(P55 + P45 + Pe), 'P(55)')
print(P45/(P45 + P55 + Pe), 'P(45)')
print(Pe/(P45 + P55 + Pe), 'P(else)')
print(1 - Pe/(P45 + P55 + Pe), '1 - P(else)')

plt.plot(xx, Narr)
plt.show()
   
      