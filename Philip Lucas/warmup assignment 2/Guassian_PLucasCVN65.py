# -*- coding: utf-8 -*-
"""
@author: Philip Lucas
HW 2 Due 16Sep2019
"""
import numpy as np
import matplotlib.pyplot as plt
N = 100000.0 #data set
number = 10 #times I run the set
mu1, sigma = 1.0 , 1.0 
mu2, sigma = 1.1, 1.0
G = []
P = []
n = 0
m=0
while n < N:
    distribution1 = np.random.normal(mu1, sigma, n)
    mean1 = np.mean(distribution1)
    distribution2 = np.random.normal(mu2, sigma, n)
    mean2 = np.mean(distribution2)
    n += 1    
    #following lines help to determine if you picked the right model based on means
    if mean1 > mean2:
        g = 1
        G.append(g)
        #P.append(np.mean(G))
    elif mean1 < mean2: 
        g = 0 
        G.append(g)
        P.append(np.mean(G))
print""
print "Likelyhood of choosing incorrect model:", np.mean(P),"%"
plt.figure(1) # likelyhood of choosing wrong model based on number of data points sampled
plt.plot(P, 'r')
plt.xlabel (" N ")
plt.ylabel (" Chance of picking wrong ")
plt.xlim([1,N])
plt.figure(2)
plt.plot((distribution1))# to see how "random" the data looks for distribution 1
plt.xlabel (" N  ")
plt.ylabel (" Distribution 1 Value")
plt.figure(3)
plt.plot((distribution2)) # to see how much "random" the data looks for distribution 2
plt.xlabel (" N  ")
plt.ylabel (" Distribution 2 Value")
plt.figure(4) # to check that data actually came from Gaussian distributions and to show seperation
plt.plot(np.sort(distribution1))
plt.plot(np.sort(distribution2))
plt.xlabel (" Least Greatest Distribution values ")
plt.ylabel (" Distribution Value")
