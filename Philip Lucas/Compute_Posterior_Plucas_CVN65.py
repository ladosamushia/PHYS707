#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Posterior Determinination Phys 707
Philip Lucas
"""


# NOTE: Makes sure you update "Data" to import the right .txt file from the proper location

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

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
    return H0*np.sqrt(omega*((1+z)**3) + 1 - omega)
def Chi2(H_0t,Omegat): #Function for Chi squared values
    chi_sq = 0
    for i in range(len(Z)):
        H_t = Ht(H_0t,Omegat,Z[i])
        chi_sq += ((H[i]-H_t)**2)/(SIGMA[i]**2)
    return chi_sq
for i in range(N): #Nested loops to determine Chi Squared values. 
    for j in range(N):
        results[i][j] = Chi2(Htest[i],Omegatest[j])
        
minimum_chisq = np.where(results == np.min(results))
Hprime = Htest[minimum_chisq[0]] #H Value at minimum Chi Squared value
Omegaprime = Omegatest[minimum_chisq[1]] #Omega Value at minimum Chi Squared 

for i in range(len(Z)): #computing data to plot the fit based on lowest chi squared values
    mod = Ht(Hprime,Omegaprime,Z[i])
    MOD.append(mod)

print ('Minimum Chi Squared Value:' , np.min(results)) # printing results
print ('Minimum Chi Squared Value location:', minimum_chisq )
print ('Best estimate for H:', Hprime)
print ('Best estimate for Omega:', Omegaprime)


plt.figure(1) #plot of experimental data
plt.title('Model and Data')
plt.xlabel('z')
plt.ylabel(r'$H_0$')
plt.errorbar(Z, H, SIGMA, fmt = 'o')
plt.plot(Z,MOD)
plt.figure(2)#contour plot of Chi Squared values
plt.title(r'$X^2$')
plt.xlabel(r'$H_0$')
plt.ylabel(r'$\Omega_m$')
plt.contour(Htest,Omegatest,results,np.linspace(0,100,15),colors=['black'])
plt.plot([Hprime], [Omegaprime], marker='o', markersize=3, color="red")
plt.figure(3)
plt.title(r'$X^2$')
plt.xlabel(r'$H_0$')
plt.ylabel(r'$\Omega_m$')
plt.pcolormesh(Htest,Omegatest,results, norm= colors.LogNorm(), cmap='inferno')
plt.colorbar()
plt.contour(Htest,Omegatest,results,np.linspace(0,100,15),colors=['black'])
plt.plot([Hprime], [Omegaprime], marker='o', markersize=3, color="red")
