# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 10:06:47 2019

@author: kilof
"""
#%% Import packages
import numpy as np
import numpy.random as rand
from matplotlib import pyplot as plt

#%% define some relevant functions
def coin_flip(Nsides,Nflips):
    return rand.randint(0,Nsides,size=Nflips)
def count_value(array,value):
    running_count = 0
    for i in range(len(array)):
        if array[i] == value:
            running_count += 1
    return running_count
#%% Run the experiment for varying Nflips and compare to P=0.5
Ntrials = 1000
results = []
for i in range(1,Ntrials+1):
    experiment = coin_flip(2,i)
    results.append(float(count_value(experiment,1))/i)
print results
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




