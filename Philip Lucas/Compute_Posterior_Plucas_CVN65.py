#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Posterior Determinination Phys 707
Philip Lucas
"""

import numpy as np
import matplotlib.pyplot as plt


N = 100 #matrix size
Data = np.loadtxt("Hz.txt") #Pulls data into pythonfile for further analysis 
ordered = np.transpose(Data) #transposes data for easier extraction without a loop
Z = ordered[0] #data extracted from file
H = ordered[1] #data extracted from file
SIGMA = ordered[2] #data extracted from file
MOD = [] # for plotting the 'best' model against the data

Htest = np.linspace(50,100,N) #Tested H values in range 50-100
Omegatest = np.linspace(0,1,N) #Tested Omega values in range 0 to 1
results = np.zeros((N,N)) # for storing Chi Squared results

def Ht(H0,omega,z): #function of the model
    return H0*np.sqrt(omega*((1+z)**3) + 1 + omega)
def Chi2(H_0t,Omegat): #Function for Chi squared values
    chi_sq = 0
    for i in range(len(Z)):
        H_t = Ht(H_0t,Omegat,Z[i])
        chi_sq += ((H[i]-H_t)**2)/(SIGMA[i]*SIGMA[i])
    return chi_sq
for i in range(N): #Nested loops to determine Chi Squared values. 
    for j in range(N):
        results[i][j] = Chi2(Htest[i],Omegatest[j])
        
minimum_chisq = np.where(results == np.min(results))

print ('Minimum Chi Squared Value location:', minimum_chisq )

Hprime = Htest[minimum_chisq[0]] #H Value at minimum Chi Squared value
Omegaprime = Omegatest[minimum_chisq[1]] #Omega Value at minimum Chi Squared Value

for i in range(len(Z)): #computing data to plot the fit based on lowest chi squared values
    mod = Ht(Hprime,Omegaprime,Z[i])
    MOD.append(mod)

plt.figure(1) #plot of experimental data
plt.xlabel('z')
plt.ylabel(r'$H_0$')
plt.errorbar(Z, H, SIGMA, fmt = 'o')
plt.plot(Z,MOD)
plt.figure(2)
plt.xlabel(r'$H_0$')
plt.ylabel(r'$\Omega_m$')
plt.contour(Htest,Omegatest,results,np.linspace(0,50,15),colors=['black'])
plt.figure(3)
plt.xlabel(r'$H_0$')
plt.ylabel(r'$\Omega_m$')
plt.contour(Htest,Omegatest,results,np.linspace(0,100,N))
plt.figure(4)
plt.imshow(results)
plt.xlim(50,100)
plt.ylim(0,1)
