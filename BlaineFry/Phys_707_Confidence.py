# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 10:06:47 2019

@author: Blaine Fry
"""
#%% Import packages
import numpy as np
import numpy.random as rand
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#%% define some relevant functions
def coin_flip(Nsides,Nflips):
    return rand.randint(0,Nsides,size=Nflips)
def count_value(array,value):
    running_count = 0
    for i in range(len(array)):
        if array[i] == value:
            running_count += 1
    return running_count

#%% Run an experiment for varying Nflips and compare to P=0.5
Ntrials = 1000
results = []
for i in range(1,Ntrials+1):
    experiment = coin_flip(2,i)
    results.append(float(count_value(experiment,1))/i)

# then, generate the plot related bits
plt.figure(1)
plt.title('Coin Experiment')
plt.ylim(0,1)
plt.ylabel(r'$\mu$')
plt.xlabel('Number of Flips')
plt.grid()
for i in range(1,1+len(results)):
    plt.plot(i,results[i-1],'b.',alpha=0.5)
plt.plot(np.linspace(1,Ntrials+1,num=10**3),np.ones(10**3)*0.5,'r--')

#%% Use the binomial distribution to analytically generate a contour plot
# make a function that returns the number of ways n heads can be had with N flips
def binom_coeff(n,N): # n: # of heads ; N: # of flips
    return float(np.math.factorial(N))/(np.math.factorial(N-n)*np.math.factorial(n))

# loop through values of n and N to get values
x = []
y = []
z = []
for N in range(1,31):
    for n in range(N+1):
        x.append(N)
        y.append(n)
        z.append(binom_coeff(n,N)/(2**N))

# make a plot of the results
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_xlabel('Number of Flips')
ax2.set_ylabel('Number of Heads')
ax2.set_zlabel('Probability')
ax2.set_title('Binomial Coefficients')
ax2.scatter(x,y,z,c=z)

"""
I'm not quite sure how to take this stuff and 
turn it into an assessment of model validity,
but I feel like this is the right direction.
"""
