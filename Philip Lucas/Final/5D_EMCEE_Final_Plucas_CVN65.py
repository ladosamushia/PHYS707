# -*- coding: utf-8 -*-
"""
5D EMCEE approximation with priors

Phys 707 Final assignment

Philip Lucas 

"""

import numpy as np
from matplotlib import pyplot as plt
import emcee
from mpl_toolkits.mplot3d import Axes3D

# load the data
z,H,sigma = np.loadtxt('Hz.txt',unpack=True)

def H_theory(z,H_0,Omega_m,Omega_k,w_0,w_a): #Defining H function
    return H_0*np.sqrt(Omega_m*((1.+z)**3)+Omega_k*((1.+z)**2)+(1-Omega_m-Omega_k)*((1.+z)**(3*(1+w_0)))*np.exp((-3)*w_a*(z/(1.+z))))                 

def Chi2(H_0t,Omega_mt,Omega_kt,w_0t,w_at): #Defining Chi function
    chi_squared = 0
    for i in range(len(z)):
        H_t = (H_theory(z[i],H_0t,Omega_mt,Omega_kt,w_0t,w_at))
        if H_t == np.nan:
            H_t = np.nan_to_num(H_theory(z[i],H_0t,Omega_mt,Omega_kt,w_0t,w_at)) + H_theory(z[i], np.random.uniform(50,100), np.random.uniform(0.1,0.5), np.random.uniform(-1.00), np.random.uniform(-0.8,-1.2), np.random.uniform(-1.0,1.0))
        chi_squared += ((H[i]-H_t)**2)/(sigma[i]*sigma[i])    
    return chi_squared

def log_prob(opt_parameters): #defining Log prob for walkers and their bounds
    H_0,Omega_m,Omega_k,w_0,w_a = opt_parameters
    if H_0 > 100.0 or H_0 < 50.0:
        H_0 = np.random.uniform(50,100)
    if Omega_m > 0.1 or Omega_m < 0.5:
        Omega_m = np.random.uniform(0.1,0.5)
    if Omega_k > 1.0 or Omega_k < -1.0:
        Omega_k = np.random.uniform(-1.0,1.0)
    if w_0 > -0.8 or w_0 < -1.2:
        w_0 = np.random.uniform(-0.8,-1.2)
    if w_a > 1.0 or w_0 < -1.0:
        w_a = np.random.uniform(-1.0,1.0)
    if np.min(Omega_m*((1.+z)**3)+Omega_k*((1.+z)**2)+(1-Omega_m-Omega_k)*((1.+z)**(3*(1+w_0)))*np.exp((-3)*w_a*(z/(1.+z)))) < 0:
        return -np.inf
    return -0.5*Chi2(H_0,Omega_m,Omega_k,w_0,w_a)


#note: after experimenting its better to have a lot of walkers and a few steps rather than the otherway around. 
N_steps = 10 #Number of steps for walkers to take

N_walkers = 20000 #number of walkers

#the following list are used to build walker start point matrix
HH = []
OmM =[]
OmK = []
W0 =[]
Wa = []

i = 0
#generating numbers for the walker start points. 
while i < N_walkers:
    Hh = np.random.uniform(50,100)
    HH.append(Hh)
    Omm = np.random.uniform(0.1,0.5)
    OmM.append(Omm)
    Omk = np.random.uniform(-1.0,1.0)
    OmK.append(Omk)
    w0 = np.random.uniform(-0.8,-1.2)
    W0.append(w0)
    wa= np.random.uniform(-1.0,1.0)
    Wa.append(wa)
#    Hh = np.random.normal(75, 25, 1)
#    HH.append(Hh)
#    Omm = np.random.normal(0.3,0.2,1)
#    OmM.append(Omm)
#    Omk = np.random.normal(0,1.0,1)
#    OmK.append(Omk)
#    w0 = np.random.normal(-0.9,0.1,1)
#    W0.append(w0)
#    wa= np.random.normal(0,1.0,1)
#    Wa.append(wa)
    
    i+=1
#walkers = np.ones((N_walkers,5)) + np.random.uniform(50,100)*np.random.rand(N_walkers,5)
walkers = np.column_stack((HH,OmM,OmK,W0,Wa))
sampler = emcee.EnsembleSampler(N_walkers,5,np.nan_to_num(log_prob))
sampler.run_mcmc(walkers, N_steps, progress=True)
samples = sampler.get_chain(flat=True)


#list for the value returns of samples from walker data
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
j = 0

#list confined to 150% expected values to remove extreme walker transit values
meanH =[]
meanOmegaM = []
meanOmegaK = []
meanW0 = []
meanWa = []
while j < N_walkers: # removing outilers keeping values within 150% expected to not skew mean with scale
    if H_0_mc[j] >= 0 and H_0_mc[j] <= 150:
        meanH.append(H_0_mc[j])
    if Omega_m_mc[j] >= -0.1 and Omega_m_mc[j] <= 0.7:
        meanOmegaM.append(Omega_m_mc[j])
    if Omega_k_mc[j] >= -2.0 and Omega_k_mc[j] <= 2.0:
        meanOmegaK.append(Omega_k_mc[j])    
    if w_0_mc[j] >= -2.4 and w_0_mc[j] <= -0.2:
        meanW0.append(w_0_mc[j])    
    if w_a_mc[j] >= -2.0 and w_a_mc[j] <= 2.0:
        meanWa.append(w_a_mc[j])    
    j+=1

print('H_0_mean =',np.mean(meanH))
print('Omega_m_mean=',np.mean(meanOmegaM))
print('Omega_k_mean=',np.mean(meanOmegaK))
print('w_0_mean=', np.mean(meanW0))
print('w_a_mean=', np.mean(meanWa))
#plots of data to play with
#fig = plt.figure(1)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,0], samples[:,1], samples[:,2], c='b', marker='.')
#plt.xlabel(r'$H_0$')
#plt.ylabel(r'$\Omega_k$')
#ax.set_zlabel(r'$\Omega_m$')
#fig = plt.figure(2)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,3], samples[:,1], samples[:,2], c='b', marker='.')
#plt.xlabel(r'$\omega_0$')
#plt.ylabel(r'$\Omega_k$')
#ax.set_zlabel(r'$\Omega_m$')
#fig = plt.figure(3)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,3], samples[:,2], samples[:,4], c='b', marker='.')
#plt.xlabel(r'$\omega_0$')
#plt.ylabel(r'$\Omega_k$')
#ax.set_zlabel(r'$\omega_a$')
#fig = plt.figure(4)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,0], samples[:,3], samples[:,4], c='b', marker='.')
#plt.xlabel(r'$H_0$')
#plt.ylabel(r'$\omega_0$')
#ax.set_zlabel(r'$\omega_a$')
#plt.figure(5)
#plt.plot(samples[:,0],samples[:,1],".")
#plt.xlim([-100,100])
#plt.ylim([-10,10])
#plt.xlabel(r'$H_0$')
#plt.ylabel(r'$\Omega_m$')
#plt.figure(6)
#plt.plot(samples[:,2],samples[:,1],".")
#plt.xlabel(r'$\Omega_k$')
#plt.ylabel(r'$\Omega_m$')
#plt.xlim([-10,10])
#plt.ylim([-10,10])
plt.figure(8)
plt.hist(samples[:,0],bins=300)
plt.xlabel(r'$H_0$')
plt.xlim(-100,250)
plt.figure(9)
plt.hist(samples[:,1],bins=300)
plt.xlabel(r'$\Omega_m$')
plt.figure(10)
plt.hist(samples[:,2],bins=300)
plt.xlabel(r'$\Omega_k$')
plt.figure(11)
plt.hist(samples[:,3],bins=300)
plt.xlabel(r'$\omega_0$')
plt.figure(12)
plt.hist(samples[:,4],bins=300)
plt.xlabel(r'$\omega_a$')
plt.xlim(-10,10)


