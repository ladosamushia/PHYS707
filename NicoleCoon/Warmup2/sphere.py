# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:31:08 2019

@author: alecc
"""
import random as rd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
xtotal = np.array([])
ytotal = np.array([])
ztotal = np.array([])
i=0
def vector():
    vect = np.array([rd.uniform(-1,1),rd.uniform(-1,1),rd.uniform(-1,1)])
    phi = np.arctan(vect[0]/vect[1])
    theta = np.arccos(vect[2]/np.linalg.norm(vect))
    point = np.array([phi,theta])
    return(point)
while i < 1000:
    i=i+1
    r = np.cbrt(rd.uniform(0,1))
    a = vector()
    sint =np.sin(a[1])
    cost=np.cos(a[1])
    sinp = np.sin(a[0])
    cosp = np.cos(a[0])
    x = r*sinp*cost
    y = r*sinp*sint
    z = r*cosp
    x = np.array([x])
    y = np.array([y])
    z = np.array([z])
    xtotal = np.concatenate((xtotal,x))
    ytotal = np.concatenate((ytotal,y))
    ztotal = np.concatenate((ztotal,z))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xtotal, ytotal, ztotal, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
#print(ztotal)