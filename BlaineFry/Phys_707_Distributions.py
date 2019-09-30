# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:29:50 2019

@author: Blaine Fry
"""

import numpy as np
import numpy.random as rand
from matplotlib import pyplot as plt

# load the data files
binom_data = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\Data Analysis For Physicists\\Blaine_binomial.txt')
gauss_data = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\Data Analysis For Physicists\\Blaine_Gauss.txt')
poisson_data = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\Data Analysis For Physicists\\Blaine_Poisson.txt')
uni_data = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\Data Analysis For Physicists\\Blaine_Uniform.txt')

#%%
"""
Gaussian
"""
# plot histogram to visualize data
plt.figure(1)
plt.title('Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Normalized Frequency')
plt.hist(gauss_data,bins=20,color='b',alpha=0.7,label='Data')

# make a function that returns the mean and sigma squared
def gauss_fit(data):
    # start with the best estimate of the mean
    mu = np.mean(data) # for the gaussian, mu is just the mean of the data
    # now for sigma squared
    ddev = []
    for i in range(len(data)):
        ddev.append((data[i]-mu)*(data[i]-mu))
    sigma2 = (1./(len(data)-1))*np.sum(ddev)
    return mu,sigma2

gauss_mu,gauss_sigma2 = gauss_fit(gauss_data)

# now get the errors on those estimates
N_trials = 1000
mu_sim = []
sigma2_sim = []
for i in range(N_trials):
    gauss_sim = rand.normal(loc=gauss_mu,scale=np.sqrt(gauss_sigma2),size=len(gauss_data))
    mu,sigma2 = gauss_fit(gauss_sim)
    mu_sim.append(mu)
    sigma2_sim.append(sigma2)
    if i == 0:
        plt.hist(gauss_sim,bins=20,color='y',alpha=0.7,label='Replicated')

plt.legend()

plt.figure(2)
plt.title(r'Gaussian $\mu$ Estimates')
plt.xlabel(r'$\mu$')
plt.xlim(0,4)
plt.hist(mu_sim,bins=20,color='b')

plt.figure(3)
plt.title(r'Gaussian $\sigma^2$ Estimates')
plt.xlabel(r'$\sigma^2$')
plt.xlim(0,2)
plt.hist(sigma2_sim,bins=20,color='b')

# look for a correlation between mu and sigma2 estimates
plt.figure(4)
plt.title('Monte Carlo Estimates for Gaussian')
plt.xlabel(r'$\mu$')
plt.ylabel(r'$\sigma^2$')
for i in range(len(mu_sim)):
    plt.plot(mu_sim[i],sigma2_sim[i],'b.')

#%%
"""
Poisson
"""
# make a histogram
plt.figure(5)
plt.title('Poisson Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.hist(poisson_data,bins=13,color='g',alpha=0.7,label='Data')

# find best estimate of lambda (arithmatic mean)
poisson_lambda = np.mean(poisson_data)

# generate distributions with this calculated lambda to find the error on the estimate
N_trials = 1000
lambda_sim = []
for i in range(N_trials):
    poisson_sim = rand.poisson(lam=poisson_lambda,size=len(poisson_data))
    l = np.mean(poisson_sim)
    lambda_sim.append(l)
    if i == 0:
        plt.hist(poisson_sim,bins=13,color='y',alpha=0.7,label='Replicated')

plt.legend()    
    
plt.figure(6)
plt.title(r'Poisson $\lambda$ Estimates')
plt.xlabel(r'$\lambda$')
plt.xlim(0,7)
plt.hist(lambda_sim,color='g')

#%%
"""
Binomial
"""
# make a histogram... not super useful here
plt.figure(7)
plt.title('Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.hist(binom_data,color='m',alpha=0.7,label='Data')

# find the best estimate of P
binomial_P = float(sum(binom_data))/len(binom_data)

# monte carlo errors, as before
N_trials = 1000
P_sim = []
for i in range(N_trials):
    binom_sim = rand.binomial(1,binomial_P,len(binom_data))
    p = float(sum(binom_sim))/len(binom_sim)
    P_sim.append(p)
    if i == 0:
        plt.hist(binom_sim,color='y',alpha=0.7,label='Replicated')

plt.legend()

plt.figure(8)
plt.title(r'Binomial $P$ Estimates')
plt.xlabel(r'$P$')
plt.xlim(0,1)
plt.hist(P_sim,color='m')

#%%
"""
Uniform
"""
# make a histogram
plt.figure(9)
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.hist(uni_data,color='c',alpha=0.7,label='Data')

# find the best estimate of x_max
uni_x_max = max(uni_data)

# monte carlo errors, as before
N_trials = 1000
x_max_sim = []
for i in range(N_trials):
    uni_sim = rand.randint(0,uni_x_max+1,size=len(uni_data))
    x_max = max(uni_sim)
    x_max_sim.append(x_max)
    if i == 0:
        plt.hist(uni_sim,color='y',alpha=0.7,label='Replicated')

plt.legend()

plt.figure(10)
plt.title(r'Uniform $X_{max}$ Estimates')
plt.xlabel(r'$X_{max}$')
plt.xlim(0,150)
plt.hist(x_max_sim,color='c')
#%%