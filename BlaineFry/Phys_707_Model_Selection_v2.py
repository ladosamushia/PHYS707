# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:52:28 2019

@author: Blaine Fry
"""
# import packages
import numpy as np
from numpy import random as rand
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

#%% generate some data
Npoints = 100
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
def Gauss_A(x):
    return gauss(x,1.0,1.0)
def Gauss_B(x):
    return gauss(x,1.2,1.0)


x = np.linspace(xbounds[0],xbounds[1],num=1000)
plt.plot(x,mod1(x),'c-',label='Gauss A')
plt.plot(x,mod2(x),'b-',label='Gauss B')
plt.legend()

#%% start comparing models
# P({x_i}) = P(x_1)*P(x_2)*P(x_3)*...
# logs would be better... consider revising

Ntrials = 1000
def compare_models(mu_ex,sigma_ex,model_1,model_2):
    log_ratios = []
    for i in range(Ntrials):
        data = rand.normal(loc=mu_ex,scale=sigma_ex,size=Npoints)
        # find the probability of the data set given model 1
        prob1 = 1
        for i in range(Npoints):
            prob1 *= model_1(data[i])
        # find the probability of the data set given model 2
        prob2 = 1
        for i in range(Npoints):
            prob2 *= model_2(data[i])
        log_ratios.append(np.log10(prob1/prob2))
    return log_ratios

ratios_A = compare_models(1.0,1.0,Gauss_A,Gauss_B) # compare the models if A is true
ratios_B = compare_models(1.2,1.0,Gauss_A,Gauss_B) # compare the models if B is true

plt.figure(2)
plt.title('Model Comparison')
plt.ylabel('Normalized Frequency')
plt.xlabel(r'$\log_{10} \left(\frac{f_A}{f_B}\right)$')
plt.hist(ratios_A,bins=Ntrials/10,alpha=0.7,normed=True,label='A is True')
plt.hist(ratios_B,bins=Ntrials/10,alpha=0.7,normed=True,label='B is True')

#%% Now we want to do the same, but with Cauchy vs Gauss

mu_star = 0
sigma_star = 1

def GAUSS(x):
    return gauss(x,mu_star,sigma_star)
def CAUCHY(x):
    return 1.0/((np.pi*sigma_star)*(1.0+(((x-mu_star)/sigma_star)**2)))

plt.figure(3)
x = np.linspace(-5,5,100)
plt.plot(x,GAUSS(x),'b')
plt.plot(x,CAUCHY(x),'r-')



