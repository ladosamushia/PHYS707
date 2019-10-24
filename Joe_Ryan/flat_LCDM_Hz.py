# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:03:18 2019

@author: jwryan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:10:17 2018

@author: jwryan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:03:49 2017

@author: jwryan
"""

from numpy import savetxt, loadtxt, arange
import time
start_time = time.time()

z_obs, Hz_obs, sigHobs = loadtxt('H(z)data.dat',unpack = True)
##From Table 1 of 1607.03537v2, refs. 4,6,7,10 excluded.

O1 = []
H1 = []
chi2Hz = []

def E(z, O, L): #Expansion parameter
    return (O*((1 + z)**3) + (1 - O - L)*((1 + z)**2) + L)**(1/2)

def H(H0, z, O, L): #Hubble parameter
    return H0*E(z, O, L)
    
def chi2h(H0, O, L):
    return sum(((1/sigHobs)*(H(H0, z_obs, O, L) - Hz_obs))**2)

Orange = arange(0.10, 0.71, 0.01)
Hrange = arange(50, 85.001, 0.01)

Ostep = len(Orange)
H0step = len(Hrange)
steps = [Ostep, H0step]
savetxt('flat-LCDM_steps.dat', steps)
    
for O in Orange:
    for H0 in Hrange:
        chi2Hz.append(chi2h(H0, O, 1-O))
        O1.append(O)
        H1.append(H0)

savetxt('flat_LCDM_chi2_H(z)only.dat', chi2Hz)
del chi2Hz
savetxt('flat_LCDM_Omega_m0.dat', O1)
del O1
savetxt('flat_LCDM_H0.dat', H1)
del H1
        
print("--- %s seconds ---" % (time.time() - start_time))