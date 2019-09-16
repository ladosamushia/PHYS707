# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:44:33 2019

@author: Blaine Fry
"""
# Phys 707 Warmup 2

# Given two normal distributions, find the probability of wrongly inferring
# which mean is greater when drawing N samples.

# import relevant libraries
import numpy as np
from numpy import random as rand
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define some analytical curves for plotting etc.
def gauss(x,mu,sigma):
    return np.exp(-((x-mu)**2)/(2*sigma*sigma))

# plot the distributions
plt.figure(1) # make a plot
plt.title('Normal Distributions')
plt.ylabel('Probability')
plt.xlabel('X')
x = np.linspace(0,20,num=10**3) # generate x values
plt.plot(x,gauss(x,10,1),'b-',label = 'Distribution 1')
plt.plot(x,gauss(x,11,1),'m-',label = 'Distribution 2')
plt.grid()
plt.legend()

# define the experiment
def normal_experiment(N_samples_drawn,mu_1,mu_2,sigma_1,sigma_2,N_trials):
    times_wrong = 0
    for i in range(N_trials):
        dist1 = rand.normal(loc=mu_1,scale=sigma_1,size=N_samples_drawn)
        dist2 = rand.normal(loc=mu_2,scale=sigma_2,size=N_samples_drawn)
        if np.mean(dist1) > np.mean(dist2):
            times_wrong += 1           
    return float(times_wrong)/float(N_trials)

plt.figure(2)
plt.title('Probability of Wrongly Inferring the Mean')
plt.xlabel('Number of Samples Drawn')
plt.ylabel('Probability')
plt.grid()
printed_result = False
for i in range(1,30):
    result = normal_experiment(i,10,11,1,1,10**4)
    plt.semilogy(i,result,'b.')
    if result < 0.01 and not printed_result:
        print 'Prob(wrong mean) < 0.01 when N_samples_drawn = ' + str(i)
        printed_result = True

# randomly generate points within a sphere without "cheating"

num_points = 1000
points = []

for i in range(num_points):
    # generate a random vector (pointing in a random direction)
    v0 = np.array([rand.rand(),rand.rand(),rand.rand()])
    # normalize
    v1 = v0/(np.linalg.norm(v0))
    # multiply by a random length
    v2 = v1*rand.rand()
    points.append(v2)

# plot the sphere
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
for p in points:
    ax.plot([p[0]],[p[1]],[p[2]],'r.',alpha=0.7) # writing the brackets like this makes it happy...

# well that doesn't work! I knew it couldn't be that easy...
# this only makes one quadrant, and the points tend to cluster at the origin.
# we need the volume element r*r*sin(phi)drdphidtheta to be uniform... parametrize? 

num_points = 2000
points = []

for i in range(num_points):
    # generate two random parameters
    u = rand.rand()
    v = rand.rand()
    # plot these points in parameter space
    plt.figure(4)
    plt.plot(v,u,'m.')
    # convert these to angles (this parametrization makes an eighth of a sphere that looks decent, but I can't justify it)
    phi = np.arccos(u)
    theta = np.arcsin(v)
    # use these angles as points on a unit sphere
    x = np.cos(theta)*np.sin(phi) 
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(phi)
    # append these values to points, scaled by a random radius
    points.append([x*(rand.rand()**(1/3.)),y*(rand.rand()**(1/3.)),z*(rand.rand()**(1/3.))]) # scale by rand^(1/3) to avoid origin clustering

    
    
# plot the sphere
fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d')
for p in points:
    ax.plot([p[0]],[p[1]],[p[2]],'m.',alpha=0.3) # writing the brackets like this makes it happy...

# I don't really understand the parametrizations I've seen on math forums etc.
# so I don't want to use them here. 


