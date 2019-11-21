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

'''
MCMC method
'''
O1 = []
H1 = []
chi2Hz = []

def logL(paras):
    H0, O = paras[0], paras[1]
    def E(z, O): #Expansion parameter
        return (O*((1 + z)**3) + (1 - O - (1 - O))*((1 + z)**2) + (1 - O))**(1/2)
    
    def H(H0, z, O): #Hubble parameter
        return H0*E(z, O)
        
    def chi2h(H0, O):
        return sum(((1/sigHobs)*(H(H0, z_obs, O) - Hz_obs))**2)
    
    Larg = (-1/2)*chi2h(H0, O)
    return Larg

def lnprior(paras):
    H0, O = paras[0], paras[1]
    if ((50 <= H0 <= 85) and (0 <= O <= 1)):
        return 0.0
    return -inf

def lnprob(paras):
    lp = lnprior(paras)
    if not isfinite(lp):
        return -inf
    return lp + logL(paras)

guess = array([70, 0.3])
print('check 1')
ndim, nwalkers = 2, 100
p0 = random.rand(ndim * nwalkers).reshape((nwalkers, ndim)) * 1e-8 + guess
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=())
pos, prob, state = sampler.run_mcmc(p0, 100)
sampler.reset()
print('check 2')

sampler.run_mcmc(pos, 20000)
chain = sampler.flatchain.copy()
savetxt('flat_LCDM_emcee.txt', chain)

'''
Grid method
'''
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

print('check 3')  
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

'''
2D to 1D
'''
for case in range(1, 3, 1):
    print('case = ', case)
    Oml = 61
    H0l = 3501
    b1 = 0.6827
    b2 = 0.9545
    m = 'H(z)only'
    
    Ml = Oml*H0l
    x0 = loadtxt('flat_LCDM_Omega_m0.dat', unpack=True)
    y0 = loadtxt('flat_LCDM_H0.dat', unpack=True)
    zz = loadtxt('flat_LCDM_chi2_' + m + '.dat', unpack=True)
    z0 = exp(-zz/2)
    del zz
    
    if case == 1:
        """
        H_0 marginalized
        """
        
        xlab = '$\Omega_{m0}$'
        xlab2 = 'Om'
        Il = H0l
        x1 = x0
        y1 = y0
        z1 = z0
        del x0, y0, z0
        
    if case == 2:
        """
        Omega_m0 marginalized
        """
        
        xlab = '$H_0$'
        xlab2 = 'H0'
        Il = Oml
        y1 = dstack(split(x0, Oml)).flatten()
        del x0
        x1 = dstack(split(y0, Oml)).flatten()
        del y0
        z1 = dstack(split(z0, Oml)).flatten()
        del z0
           
    z2 = []
    y2 = []
    x = []
    y = []
    
    c = 0
    for q in range(0, Ml, 1):
        c += 1
        z2.append(z1[q])
        y2.append(y1[q])
        
        if c == Il:
            y.append(abs(trapz(z2, y2)))
            x.append(x1[q])
            
            z2 = []
            y2 = []
            c = 0
            
    del y1, x1, z1
    
    savetxt('flat_LCDM_L(' + xlab2 + ').dat', y)
    savetxt('flat_LCDM_' + xlab2 + '_1D.dat', x)

'''
Plots
'''
chain1 = loadtxt('flat_LCDM_emcee.txt',unpack=True,delimiter=' ')

OH1 = chain1[0,:]
OM1 = chain1[1,:]

samps = array([OH1,OM1])
samps = samps.T
samps1 = samps[samps[:,1]<=0.7,:]
samps2 = samps1[0.1<=samps1[:,1],:]
samps3 = samps2[samps2[:,0]<=85,:]
cut_samps = samps3[50<=samps3[:,0],:]
names = ["H","m"]
labels = [r"H_0",r"\Omega_{m_0}"]
samples = MCSamples(samples=cut_samps,names = names, labels = labels,ranges={'H':(50,85),'m':(0.1,0.7)})
samples1 = MCSamples(samples=samps,names = names, labels = labels,ranges={'H':(50,85),'m':(0.1,0.7)})

'''
1D likelihoods
'''
z1 = loadtxt('flat_LCDM_L(H0).dat', unpack=True)
print('check 4')
x1 = loadtxt('flat_LCDM_H0_1D.dat', unpack=True)

g = plots.getSinglePlotter(width_inch=4)
g.plot_1d(samples, 'H', ls=['solid'])
plt.plot(x1, z1/max(z1), linestyle=':', color='blue')
g.export('flat_LCDM_L(H0)_1D_MCMC_vs_grid_my_data.pdf')

z1 = loadtxt('flat_LCDM_L(Om).dat', unpack=True)
print('check 5')
x1 = loadtxt('flat_LCDM_Om_1D.dat', unpack=True)

g = plots.getSinglePlotter(width_inch=4)
g.plot_1d(samples, 'm', ls=['solid'])
plt.plot(x1, z1/max(z1), linestyle=':', color='blue')
g.export('flat_LCDM_L(Om)_1D_MCMC_vs_grid_my_data.pdf')

'''
2D contours
'''
xstep1, ystep1 = loadtxt('flat-LCDM_steps.dat', unpack=True)
xstep = int(xstep1)
ystep = int(ystep1)
print('check 6')

z2 = loadtxt('flat_LCDM_chi2_H(z)only.dat', unpack=True)
y2 = loadtxt('flat_LCDM_Omega_m0.dat', unpack=True)
x2 = loadtxt('flat_LCDM_H0.dat', unpack=True)
zmin = z2.tolist().index(min(z2))   
xmin2 = x2[zmin]
ymin2 = y2[zmin]
c2 = z2[zmin]
print(c2, xmin2, ymin2, "2D best fit points with grid")

g = plots.getSinglePlotter(width_inch=4, ratio=1)
samples.updateSettings({'contours': [0.6827, 0.9545, 0.9973]})
g.settings.num_plot_contours = 3
g.plot_2d([samples],['H','m'],filled_compare=False,
    line_args=[{'ls':'solid','color':'k'}])
x2_2D_mcase3 = reshape(x2, (xstep, ystep))
y2_2D_mcase3 = reshape(y2, (xstep, ystep))
z2_2D_mcase3 = reshape(z2, (xstep, ystep))
plt.contour(x2_2D_mcase3, y2_2D_mcase3, z2_2D_mcase3, [c2, c2 + 2.3, c2 + 6.17, c2 + 11.8],
            colors='blue', linestyles=':')
plt.plot([xmin2, xmin2], [ymin2, ymin2], marker='+', color='blue') #Best fit parameters
g.export('flat_LCDM_H0_Om_2D_MCMC_vs_grid_my_data.pdf')
        
print("--- %s seconds ---" % (time.time() - start_time))