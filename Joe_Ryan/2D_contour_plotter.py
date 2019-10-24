# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import loadtxt, reshape

xstep1, ystep1 = loadtxt('flat-LCDM_steps.dat', unpack=True)
xstep = int(xstep1)
ystep = int(ystep1)

z2 = loadtxt('flat_LCDM_chi2_H(z)only.dat', unpack=True)
y2 = loadtxt('flat_LCDM_Omega_m0.dat', unpack=True)
x2 = loadtxt('flat_LCDM_H0.dat', unpack=True)
zmin = z2.tolist().index(min(z2))   
xmin2 = x2[zmin]
ymin2 = y2[zmin]
c2 = z2[zmin]
print(c2, xmin2, ymin2)

hlab = 1*'$\hspace{0.25}({\\rm km} \hspace{0.25} {\\rm s}^{-1} \hspace{0.25} {\\rm Mpc}^{-1})$'
plt.figure(figsize=(5.5,5.5))
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
x2_2D_mcase3 = reshape(x2, (xstep, ystep))
y2_2D_mcase3 = reshape(y2, (xstep, ystep))
z2_2D_mcase3 = reshape(z2, (xstep, ystep))
plt.contour(x2_2D_mcase3, y2_2D_mcase3, z2_2D_mcase3, [c2, c2 + 2.3, c2 + 6.17, c2 + 11.8],
            colors='black', linestyles='solid')
plt.plot([xmin2, xmin2], [ymin2, ymin2], marker='.', color='red') #Best fit parameters

plt.ylabel('$\Omega_{m0}$', size='22')
plt.xlabel('$H_0$' + hlab, size='22')
plt.ylim(0.10, 0.625)
plt.xlim(55, 80)
plt.tight_layout()
plt.savefig("flat_LCDM_Omega_m0_H0_Hz.pdf")
plt.show()