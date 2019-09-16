# -*- coding: utf-8 -*-
"""
@author: Philip Lucas
Warmup Homework 2 
Spherical distribution of data
*note* I still need to set up a way to sample it to show its uniform
I referenced this 
http://mathworld.wolfram.com/SpherePointPicking.html
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
X = [] # x points for plotting 
Y = [] # y points for plotting 
Z = [] # z points for plotting 
N = 100
n =  0.0
while n <= N:
    #r = 1
    r = (np.random.uniform(0,1))**(1.0/3.0) #radius of point
    #using Marsaglia method to creat points on a unit spheres surface
    x1 = np.random.uniform(-1,1) 
    x2 = np.random.uniform(-1,1)
    if x1**2 + x2**2 >= 1: 
        x1 = np.random.uniform(-1,1)
        x2 = np.random.uniform(-1,1) 
    a = (2*x1*np.sqrt(1-x1**2 -x2**2)) #xpoint on surface
    b = (2*x2*np.sqrt(1-x1**2 -x2**2 ))#ypoint on surface
    c = (1 - 2*(x1**2 + x2**2))#zpoint on surface
    x = r*(a/(a**2 +b**2 +c**2)**0.5) #unit vector of point a times the radius
    y = r*(b/(a**2 +b**2 +c**2)**0.5) #unit vector of point b times the radius
    z = r*(c/(a**2 +b**2 +c**2)**0.5) #unit vector of point c times the radius
    X.append(x)
    Y.append(y)
    Z.append(z)
    n+=1
print np.sum(X)
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(azim=0, elev=90)
ax.set_title('Top Down View')
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='g', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(azim=90, elev=0)
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='r', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(azim=180, elev=0)
ax.set_title('X-Z Side View')
fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='black', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Isometric View')


