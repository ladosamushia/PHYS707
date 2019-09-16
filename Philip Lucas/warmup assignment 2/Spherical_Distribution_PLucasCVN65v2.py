"""
@author: Philip Lucas
Warmup Homework 2 
Spherical distribution of data
I referenced Marsaglia technique from the following URL
http://mathworld.wolfram.com/SpherePointPicking.html
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
X = [] # x points for plotting 
Y = [] # y points for plotting 
Z = [] # z points for plotting 
U = [] # x point non-corrected Radius 
V = [] # y point non-corrected Radius 
T = [] # z point non-corrected Radius
A = [] # x point on unit sphere
B = [] # y point on unit sphere
C = [] # z point on unit sphere
N = 1000
n =  0.0
while n <= N:
    #r = 1
    r1 = (np.random.uniform(0,1))
    r = (np.random.uniform(0,1))**(1.0/3.0) #radius of point
    x1 = np.random.uniform(-1,1) 
    x2 = np.random.uniform(-1,1) 
    a = (2*x1*np.sqrt(1-x1**2 -x2**2)) #xpoint on surface
    b = (2*x2*np.sqrt(1-x1**2 -x2**2 ))#ypoint on surface
    c = (1 - 2*(x1**2 + x2**2))#zpoint on surface
    x = r*(a/(a**2 +b**2 +c**2)**0.5) #unit vector of point a times the radius
    y = r*(b/(a**2 +b**2 +c**2)**0.5) #unit vector of point b times the radius
    z = r*(c/(a**2 +b**2 +c**2)**0.5) #unit vector of point c times the radius
    u = r1*(a/(a**2 +b**2 +c**2)**0.5) #unit vector of point a times the radius
    v = r1*(b/(a**2 +b**2 +c**2)**0.5) #unit vector of point b times the radius
    t = r1*(c/(a**2 +b**2 +c**2)**0.5) #unit vector of point c times the radius
    X.append(x)
    Y.append(y)
    Z.append(z)
    U.append(u)
    V.append(v)
    T.append(t)
    A.append(a)
    B.append(b)
    C.append(c)
    n+=1
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
ax.set_title('Distribution in a sphere with corrected r')
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(U, V, T, c='r', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(azim=0, elev=90)
ax.set_title('Distribution in a Sphere with an uncorrected r distribution ')
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='.')
ax.scatter(A, B, C, c='g', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(azim=0, elev=90)
ax.set_title('Distribution in a sphere with same unit sphere surface points')
fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(A, B, C, c='g', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(azim=0, elev=90)
ax.set_title('Distribution on surface of a unit sphere')
fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='.')
ax.scatter(U, V, T, c='r', marker='.')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(azim=0, elev=90)
ax.set_title('fig 1 and 2 overlap plot')
