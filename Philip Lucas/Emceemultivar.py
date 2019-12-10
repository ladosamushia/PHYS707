# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:15:48 2019
@author: Phili

"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import emcee
from mpl_toolkits.mplot3d import Axes3D



# Write the model equation
def H_theory(z,H_0,Omega_m,Omega_k,w_0,w_a):
    return H_0*np.sqrt(Omega_m*((1.+z)**3)+Omega_k*((1.+z)**2)+(1-Omega_m-Omega_k)*((1.+z)**(3*(1+w_0)))*np.exp((-3)*w_a*(z/(1.+z))))                 

# load the data
z,H,sigma = np.loadtxt('Hz.txt',unpack=True)

def Chi2(H_0t,Omega_mt,Omega_kt,w_0t,w_at):
    chi_squared = 0
    for i in range(len(z)):
        H_t = np.nan_to_num(H_theory(z[i],H_0t,Omega_mt,Omega_kt,w_0t,w_at))
        chi_squared += ((H[i]-H_t)**2)/(sigma[i]*sigma[i])


    #print(chi_squared, H_t, H_0t, Omega_mt, Omega_kt, w_0t, w_at)
    
    return chi_squared


def log_prob(opt_parameters):
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
        w_0 = np.random.uniform(-1.0,1.0)
    if np.min(Omega_m*((1.+z)**3)+Omega_k*((1.+z)**2)+(1-Omega_m-Omega_k)*((1.+z)**(3*(1+w_0)))*np.exp((-3)*w_a*(z/(1.+z)))) < 0:
        return -np.inf
    return -0.5*Chi2(H_0,Omega_m,Omega_k,w_0,w_a)

N_steps = 100

N_walkers = 200
walkers = np.ones((N_walkers,5)) + np.random.rand(N_walkers,5)


sampler = emcee.EnsembleSampler(N_walkers,5,np.nan_to_num(log_prob))
sampler.run_mcmc(walkers, N_steps, progress=True)
samples = sampler.get_chain(flat=True)



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
    

#i=0
#while i <= 4: 
#    if i + 1 >= 5:
#        break
#    plt.figure(i)
#    hist,dumby1,dumby2 =np.histogram2d(-samples[:,i],samples[:,i+1],bins=100)
#    plt.imshow(hist)
#    i += 1
    
#fig = plt.figure(1)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,0], samples[:,1], samples[:,2], c='b', marker='.')
#ax.set_xlim([-100,100])
#ax.set_ylim([-5,5])
#ax.set_zlim([-10,10])
#fig = plt.figure(2)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,0], samples[:,1], samples[:,2], c='b', marker='.')
#
#fig = plt.figure(3)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,2], samples[:,3], samples[:,4], c='b', marker='.')
#ax.set_xlim([-10,10])
#ax.set_ylim([-10,10])
#ax.set_zlim([-10,10])
#fig = plt.figure(4)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(samples[:,0], samples[:,1], samples[:,2], c='b', marker='.')

plt.figure(2)
plt.plot(samples[:,0],samples[:,1],".")
plt.xlim([-100,100])
plt.ylim([-10,10])
plt.figure(3)
plt.plot(samples[:,1],samples[:,2],".")
plt.xlim([-10,10])
plt.ylim([-10,10])
print(np.mean(samples[:,0]))
