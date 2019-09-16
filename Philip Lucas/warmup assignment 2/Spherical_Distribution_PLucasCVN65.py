# -*- coding: utf-8 -*-
"""
@author: Philip Lucas
Warmup Homework 2 
Spherical distribution of data
*note* I still need to set up a way to sample it to show its uniform
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
X = [] # x points for plotting 
Y = [] # y points for plotting 
Z = [] # z points for plotting 
N = 1000
n =  0.0
while n <= N:
    h = np.random.uniform(0,1) 
    theta = np.random.uniform(0,2*np.pi) #picks an angle on the x y plane
    r = (np.random.uniform(-1, 1)**2 + np.random.uniform(-1,1)**2)**0.5 # for angle determination
    p = (np.random.uniform(0,1))**0.5 #radius of sphere 
    phi = np.arctan2(h,r) # determines azi angle
    x = p*np.cos(phi)*np.sin(theta) #xpoint
    y = p*np.sin(phi)*np.sin(theta) #ypoint
    z = p*np.cos(theta)  #zpoint
    X.append(x)
    Y.append(y)
    Z.append(z)
    n+=1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='.')
ax.set_xlim([-1.0,1.0])
ax.set_ylim([-1.0,1.0])
ax.set_zlim([-1.0,1.0])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()