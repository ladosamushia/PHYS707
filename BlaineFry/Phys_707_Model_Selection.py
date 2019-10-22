# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 10:10:29 2019

@author: Blaine Fry
"""
# import packages
import numpy as np
from numpy import random as rand
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

#%% generate some data
Npoints = 50
mu_0 = 1.0
sigma_0 = 2.0
data = rand.normal(loc=mu_0,scale=sigma_0,size=Npoints)
# and make a histogram of it
xbounds = [-5,5]
Nbins = 20
Bins = np.linspace(xbounds[0],xbounds[1],num=Nbins+1)
plt.figure(1)
plt.xlim(xbounds[0],xbounds[1])
plt.xlabel('value')
plt.ylabel('Normalized Frequency')
plt.title('Data Histogram')
plt.grid(alpha=0.5)
plt.hist(data,bins=Bins,alpha=0.8,color='m',normed=True,label='Data') # may need to switch normed to density if this line calls an error
plt.legend()

#%% define the models to test out
# first, a general gaussian 
def gauss(x,mu,sigma):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-((x-mu)*(x-mu))/(2*sigma*sigma))
# then the models
def mod1(x):
    return gauss(x,1.0,1.0)
def mod2(x):
    return gauss(x,1.2,1.0)
def mod3(x):
    return gauss(x,1.0,2.0)
def mod4(x):
    return gauss(x,1.2,2.0)

x = np.linspace(xbounds[0],xbounds[1],num=1000)
plt.plot(x,mod1(x),'c-',label='Model 1')
plt.plot(x,mod2(x),'b-',label='Model 2')
plt.plot(x,mod3(x),'y-',label='Model 3')
plt.plot(x,mod4(x),'g-',label='Model 4')
plt.legend()

#%% start comparing models
## we need some numbers for the data histogram, so make a numerical histogram w/ numpy
#hist,bins_dummy = np.histogram(data,bins=Bins,density=True)
##plt.plot(Bins[1:],hist,'md')
## use chi squared values to assess model validity
#def chi_squared(x,y,Model):
#    chi2 = 0
#    for i in range(len(x)):
#        chi2 += (y[i]-)

# let's try this a different way
# P({x_i}) = P(x_1)*P(x_2)*P(x_3)*... should there be some normalization factor???

Ntrials = 1000
prob_ratio = []
for i in range(Ntrials):
    data = rand.normal(loc=mu_0,scale=sigma_0,size=Npoints)
    # find the probability of the data set given model 1
    prob1 = 1
    for i in range(Npoints):
        prob1 *= mod1(data[i])
    # find the probability of the data set given model 2
    prob2 = 1
    for i in range(Npoints):
        prob2 *= mod2(data[i])
    # find the probability of the data set given model 3
    prob3 = 1
    for i in range(Npoints):
        prob3 *= mod3(data[i])
    # find the probability of the data set given model 4
    prob4 = 1
    for i in range(Npoints):
        prob4 *= mod4(data[i])
    prob_ratio.append(prob1/prob3)


plt.figure(2)
plt.hist(prob_ratio,normed=True)









