# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 09:32:09 2019

@author: blainef
"""
#%% set things up
# import packages
import numpy as np
from matplotlib import pyplot as plt

# Write the model equation
def H_theory(z,H_0,Omega_m):
    return H_0*np.sqrt(Omega_m*((1.+z)**3)+1-Omega_m)

# load the data
z,H,sigma0 = np.loadtxt('C:\\Users\\kilof\\OneDrive\\Documents\\\\Hz.txt',unpack=True)
sigma=sigma0/2
# plot the data
plt.figure(1)
plt.xlabel('z')
plt.ylabel(r'$H_0$')
plt.errorbar(z,H,yerr=sigma,fmt='b.')

#%% compute chi-squared values
# define a function
def Chi2(H_0t,Omega_mt):
    chi_squared = 0
    for i in range(len(z)):
        H_t = H_theory(z[i],H_0t,Omega_mt)
        chi_squared += ((H[i]-H_t)**2)/(sigma[i]*sigma[i])
    return chi_squared

# make some arrays
gridN = 100
results = np.zeros((gridN,gridN))
H_0_test = np.linspace(50,100,gridN)
Omega_m_test = np.linspace(0,1,gridN)

# loop through those values and store results
for i in range(gridN):
    for j in range(gridN):
        results[i][j] = Chi2(H_0_test[i],Omega_m_test[j])

# find the best fit values
min_idx = np.where(results == np.min(results))

#%% plot results
# make a contour plot
plt.figure(2)
plt.xlabel(r'$H_0$')
plt.ylabel(r'$\Omega_m$')
plt.contour(H_0_test,Omega_m_test,results,[15,30,60,120,240,360,480,600],colors=['black'])
plt.plot(H_0_test[min_idx[0][0]],Omega_m_test[min_idx[1][0]],'r.')

# put the best fit line on figure 1
plt.figure(1)
plt.plot(z,H_theory(z,H_0_test[min_idx[0][0]],Omega_m_test[min_idx[1][0]]),'r--')


