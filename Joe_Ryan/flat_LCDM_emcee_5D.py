# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:12:23 2019

@author: Owner
"""

from numpy import dstack, split, loadtxt, exp, trapz, arange, savetxt, array, random, reshape, inf, isfinite
import time
from getdist import plots, MCSamples
import emcee
import matplotlib.pyplot as plt
start_time = time.time()

z_obs, Hz_obs, sigHobs = loadtxt('H(z)data.dat',unpack = True)
##From Table 1 of 1607.03537v2, refs. 4,6,7,10 excluded.

def logL(paras):
    H0, O, Ok, w0, wa = paras[0], paras[1], paras[2], paras[3], paras[4]
    def E(z, O, Ok, w0, wa): #Expansion parameter
        w0e = 3*(1 - w0) #Should be 1 + w0?
        wae = -3*wa*(z/(1 + z))
        return (O*((1 + z)**3) + Ok*((1 + z)**2) + (1 - O - Ok)*((1 + z)**w0e)*exp(wae))**(1/2)
    
    def H(H0, z, O, Ok, w0, wa): #Hubble parameter
        return H0*E(z, O, Ok, w0, wa)
        
    def chi2h(H0, O, Ok, w0, wa):
        return sum(((1/sigHobs)*(H(H0, z_obs, O, Ok, w0, wa) - Hz_obs))**2)
    
    Larg = (-1/2)*chi2h(H0, O, Ok, w0, wa)
    return Larg

def lnprior(paras):
    H0, O, Ok, w0, wa = paras[0], paras[1], paras[2], paras[3], paras[4]
    if ((60 <= H0 <= 100) and (0.1 <= O <= 0.5) and (-0.4 <= Ok <= 0.4) and (-1.2 <= w0 <= -0.8) and (-1 <= wa <= 1)):
        return 0.0
    return -inf

def lnprob(paras):
    lp = lnprior(paras)
    if not isfinite(lp):
        return -inf
    return lp + logL(paras)

guess = array([70, 0.3, 0, -1, 0])
print('check 1')
ndim, nwalkers = 5, 100
p0 = random.rand(ndim * nwalkers).reshape((nwalkers, ndim)) * 1e-8 + guess
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=())
pos, prob, state = sampler.run_mcmc(p0, 100)
sampler.reset()
print('check 2')

sampler.run_mcmc(pos, 200)
chain = sampler.flatchain.copy()
savetxt('flat_LCDM_emcee_5D.txt', chain)

'''
Plots
'''
chain = loadtxt('flat_LCDM_emcee_5D.txt',unpack=True,delimiter=' ')

H01 = chain[0,:]
O1 = chain[1,:]
Ok1 = chain[2,:]
w01 = chain[3,:]
wa1 = chain[4,:]

samps = array([H01, O1, Ok1, w01, wa1])
samps = samps.T
"""
samps1 = samps[samps[:,1]<=0.7,:]
samps2 = samps1[0.1<=samps1[:,1],:]
samps3 = samps2[samps2[:,0]<=85,:]
cut_samps = samps3[50<=samps3[:,0],:]
"""
names = ["H0", "O", "Ok", "w0", "wa"]
labels = [r"H_0", r"\Omega_{m_0}", r"\Omega_{k0}", r"w_0", r"w_a"]
#samples = MCSamples(samples=cut_samps,names = names, labels = labels,ranges={'H':(50,85),'m':(0.1,0.7)})
samples1 = MCSamples(samples=samps, names = names, labels = labels, ranges={'H0':(25, 100), 'O':(0.1, 0.7), 'Ok':(-0.5, 0.5), 'w0':(-1.5, -0.5), 'wa':(-1.5, 1.5)})

g = plots.getSubplotPlotter()
#samples.updateSettings({'contours': [0.6827, 0.9545, 0.9973]})
samples1.updateSettings({'contours': [0.6827, 0.9545, 0.9973]})
g.settings.alpha_filled_add=0.4
g.settings.num_plot_contours = 3
g.triangle_plot([samples1], ['H0', 'O', 'Ok', 'w0', 'wa'],filled_compare=False)
#legend_labels=[r'$\rm New\ BAO$',  r'$\rm Old\ BAO$'],
#legend_loc='upper right',ls=['-','--'],line_args=[{'ls':'-','color':'blue'},{'ls':'--','color':'red'}],contour_colors=['blue','red'])
g.export('flat_LCDM_emcee_5D.pdf')

        
print("--- %s seconds ---" % (time.time() - start_time))