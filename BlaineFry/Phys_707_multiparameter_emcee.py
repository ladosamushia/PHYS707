# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:15:48 2019

@author: Blaine Fry

Use emcee to optimize a many-parameter system
"""
#%% set things up
# import packages
import numpy as np
from matplotlib import pyplot as plt
import emcee

# Write the model equation
def H_theory(z,H_0,Omega_m,Omega_k,w_0,w_a):
    return H_0*np.sqrt(Omega_m*((1.+z)**3)+Omega_k*((1.+z)**2)+(1-Omega_m-Omega_k)*((1.+z)**(3*(1-w_0)))*np.exp((-3)*w_a*(z/(1.+z))))                 

# load the data
z,H,sigma = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\\\Hz.txt',unpack=True)
# plot the data
plt.figure(1)
plt.xlabel('z')
plt.ylabel(r'$H$')
plt.errorbar(z,H,yerr=sigma,fmt='b.')

#%% define some functions to calculate probabilities
# Chi Squared Function
def Chi2(H_0t,Omega_mt,Omega_kt,w_0t,w_at):
    chi_squared = 0
    for i in range(len(z)):
        H_t = H_theory(z[i],H_0t,Omega_mt,Omega_kt,w_0t,w_at)
        chi_squared += ((H[i]-H_t)**2)/(sigma[i]*sigma[i])
    return chi_squared

# rough probability
def log_prob(opt_parameters):
    H_0,Omega_m,Omega_k,w_0,w_a = opt_parameters
    if np.min(Omega_m*((1.+z)**3)+Omega_k*((1.+z)**2)+(1-Omega_m-Omega_k)*((1.+z)**(3*(1-w_0)))*np.exp((-3)*w_a*(z/(1.+z)))) < 0:
        return -np.inf
    return -0.5*Chi2(H_0,Omega_m,Omega_k,w_0,w_a)

#%% find optimal values with emcee
N_steps = 100
# initialize position of walkers
N_walkers = 20
walkers = np.ones((N_walkers,5)) + np.random.rand(N_walkers,5)

# run emcee
sampler = emcee.EnsembleSampler(N_walkers,5,log_prob)
sampler.run_mcmc(walkers, N_steps, progress=True)
samples = sampler.get_chain(flat=True)

#%% analyize results
# set up some lists to store values
H_0_mc = [] 
Omega_m_mc = []
Omega_k_mc = []
w_0_mc = []
w_a_mc = []
# unpack the walkers
for s in samples:
    H_0_mc.append(s[0])
    Omega_m_mc.append(s[1])
    Omega_k_mc.append(s[2])
    w_0_mc.append(s[3])
    w_a_mc.append(s[4])





