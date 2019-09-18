# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:20:30 2019

@author: wangjam
"""
import numpy as np
from numpy.random import random

import matplotlib.pyplot as plt
#print(random())#generates random numbers from [0,1)
X=[]
Y=[]
Z=[]  
i=0
N=10000#sampling is radius dependent, as each volume element goes wiht r^2 we need to inverse transform sampling i.e. taking the the inverse of cfd in this case
while (i<N):
    r=np.cbrt(random())
    theta = 2 * np.pi*random()
    phi=np.arccos(1 - 2 *random())
    x = r*np.sin(phi) * np.cos(theta)  
    y = r*np.sin(phi) * np.sin(theta)
    z = r*np.cos(phi)
    X.append(x)
    Y.append(y)
    Z.append(z)
    i+=1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X,Y,Z,c='b')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()