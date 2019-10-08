# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
from numpy import arange, reshape, sqrt

a = []
N2 = 10**3

muarr = []
Narr = []
sig = []
chi2 = []

for x in range(1, N2+1, 1): #Number of trials.
    for m in arange(0, 1, 0.01): #Coin's expectation value ranges from
                                 #0 to 1 in steps of 0.01.
        muarr.append(m) #This list stores the expectation value.
        Narr.append(x)  #This list stores the number of trials.
        H0 = 0.5
        sig = sqrt((H0*(1-H0))/x) #Sivia and Skilling, p. 23
        chi2.append(((m - 0.5)**2)/(sig**2)) #chi^2 is a function of both
                                             #m, the expectation value, and
                                             #N, the number of trials.
    
zmin = chi2.index(min(chi2))
xmin1 = Narr[zmin]
ymin1 = muarr[zmin]
c1 = chi2[zmin]
#These lines find the minimum chi^2 and the best-fitting values of
#m and N (which correspond to the minimum value of chi^2).

ystep = 100 #Number of steps in the m loop.
xstep = N2  #Number of trials.
x1_2d = reshape(Narr, (xstep, ystep))
y1_2d = reshape(muarr, (xstep, ystep))
z1_2d = reshape(chi2, (xstep, ystep))
plt.plot([0.0, 1000], [0.5, 0.5]) #Expectation value of a fair coin: m = 0.5
plt.xlim(0, 1000)
plt.contour(x1_2d, y1_2d, z1_2d, [c1, c1 + 1, c1 + 2, c1 + 3, c1 + 4, c1 + 5],
            colors='black', linestyles='solid')
#The contours demarcate regions of the m-N parameter space corresponding to
#"surprising" combinations of m and N.
plt.plot([xmin1, xmin1], [ymin1, ymin1], marker='.', color='red')
plt.xlabel('N')
plt.ylabel('$\mu$')