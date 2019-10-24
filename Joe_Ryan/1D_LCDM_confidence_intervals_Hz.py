# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:18:39 2018

@author: Owner
"""

from numpy import dstack, split, loadtxt, exp, trapz, arange
from scipy.interpolate import interp1d
from scipy.integrate import quad
import matplotlib.pyplot as plt

case = 1
upper = True

if case == 1:
    xinc = 1/10000
if case == 2:
    xinc = 1/1000

Oml = 61
H0l = 3501
b1 = 0.6827
b2 = 0.9545
m = 'H(z)only'
Linc = 1/100

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
   
L = interp1d(x, y, kind='cubic')

candL1 = []
candr1 = []
candp1 = []

candL2 = []
candr2 = []
candp2 = []

xmax = x[y.index(max(y))]

if upper == True:
    xlim = max(x)
    k = 1
if upper == False:
    xlim = min(x)
    k = -1
z = arange(xmax, xlim, k*xinc)

for r in z:
    LCO1tot, error = quad(lambda m: L(m), xmax, xlim)
    LCO1, error = quad(lambda m: L(m), xmax, r)
    LCO = abs(LCO1/LCO1tot)
    print(LCO, r)
    if abs((LCO - b1)/b1) < Linc:
        candL1.append(LCO)
        candr1.append(r)
        candp1.append(abs((LCO - b1)/b1))
    if abs((LCO - b2)/b2) < Linc:
        candL2.append(LCO)
        candr2.append(r)
        candp2.append(abs((LCO - b2)/b2))
    if LCO >= b2 + 0.01:
        break

pmin = candp1.index(min(candp1))   
Lmin = candL1[pmin]
rmin = candr1[pmin]

print('1-sigma')   
print(Lmin)
print('>>', rmin)
print(min(candp1))

pmin = candp2.index(min(candp2))   
Lmin = candL2[pmin]
rmin = candr2[pmin]

print('2-sigma')
print(Lmin)
print('>>', rmin)
print(min(candp2))

print('Best-fit')
print(xmax, min(x), max(x), 'upper =', upper)
print(m)

if case == 1:
    print('H0 marginalized')
else:
    print('O_m0 marginalized')

plt.figure(figsize=(5.5,5.5))
xnew = arange(min(x), max(x)-xinc, xinc)
plt.plot(xnew, L(xnew)/max(L(xnew)))
plt.ylim(0, 1)
plt.xlim(min(xnew), max(xnew))
plt.xlabel(xlab, size='18')
plt.ylabel('$\mathcal{L}$(' + xlab + ')/$\mathcal{L}_{max}$', size='18')
plt.tight_layout()
plt.savefig('flat_LCDM_' + xlab2 + '_1D.pdf')
plt.show()