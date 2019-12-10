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
    # this stuff is from phil... I can't get it to work though... 
    # However, if I use 100 walkers and 20 steps, I seem to have decent results without it
#    if H_0 > 100.0 or H_0 < 50.0:
#        H_0 = np.random.uniform(50,100)
#    if Omega_m > 0.1 or Omega_m < 0.5:
#        Omega_m = np.random.uniform(0.1,0.5)
#    if Omega_k > 1.0 or Omega_k < -1.0:
#        Omega_k = np.random.uniform(-1.0,1.0)
#    if w_0 > -0.8 or w_0 < -1.2:
#        w_0 = np.random.uniform(-0.8,-1.2)
#    if w_a > 1.0 or w_0 < -1.0:
#        w_0 = np.random.uniform(-1.0,1.0)
    #print(-0.5*Chi2(H_0,Omega_m,Omega_k,w_0,w_a),'\n')
    return -0.5*Chi2(H_0,Omega_m,Omega_k,w_0,w_a)

#%% find optimal values with emcee
N_steps = 30
# initialize position of walkers
N_walkers = 100
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

def find_opt(param):
    hist,bins = np.histogram(param)
    hist_list = hist.tolist()
    idx = hist_list.index(np.max(hist_list))
    return bins[idx]

H_0_opt = find_opt(H_0_mc)
Omega_m_opt = find_opt(Omega_m_mc)
Omega_k_opt = find_opt(Omega_k_mc)
w_0_opt = find_opt(w_0_mc)
w_a_opt = find_opt(w_a_mc)

# plot fit line on figure 1
# the result with this doesn't look too good
Z = np.linspace(min(z),max(z),num=1000)
plt.figure(1)
plt.plot(Z,H_theory(Z,H_0_opt,Omega_m_opt,Omega_k_opt,w_0_opt,w_a_opt),'r-')

# plot histograms with a method similar to what Phil Lucas did in "emceemultivar"
for i in range(4):
    plt.figure(i+2)
    hist,dumby1,dumby2 =np.histogram2d(-samples[:,i],samples[:,i+1],bins=100)
    plt.imshow(hist)


