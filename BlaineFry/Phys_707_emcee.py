# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:39:44 2019

@author: Blaine Fry
"""

import numpy as np
from matplotlib import pyplot as plt
import emcee

z,H_m,sigma0 = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\\\Hz.txt',unpack=True)

def log_prob(x):
    H_0,Omega_m = x
    Hsq = Omega_m*((1.+z)**3)+1-Omega_m
    if np.min(Hsq) < 0:
        return -10000
    H_t = H_0*np.sqrt(Omega_m*((1.+z)**3)+1-Omega_m)
    Chi2 = np.sum(((H_m-H_t)**2)/(sigma0**2))
    L = -0.5*Chi2
    return L
    
ndim, nwalkers = 2,4
H_0i = 50*np.random.rand(4) + 50
Omega_mi = 0.2*np.random.rand(4) + 0.2

p0 = np.asarray([H_0i,Omega_mi])

sampler = emcee.EnsembleSampler(nwalkers,ndim,log_prob)
sampler.run_mcmc(p0.T,10000)

samples = sampler.get_chain(flat=True)

hist,dumby1,dumby2 =np.histogram2d(samples[:,0],samples[:,1],bins=100)
plt.imshow(hist)
