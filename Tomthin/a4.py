# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 00:40:17 2019

@author: wangjam
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
p=.5
trials=100 
n_flips=np.arange(1,trials+1,1)
Z1=np.zeros((trials+1, trials+1))
Z2=np.zeros((trials+1, trials+1))
Z3=np.zeros((trials+1, trials+1))
for jl,j in enumerate(n_flips):
    success=np.arange(0,j+1,1)
    for il,k in enumerate(success):
       Z1[il,jl]=binom.cdf(k,j,p)#Probability(x<=k) given the hypothesis that the coin is fair(p=.5)and we have achieve k sucess in j trials
       Z2[il,jl]=1-binom.cdf(k,j,p)#Probability(x>=k) given the hypothesis that the coin is fair(p=.5) and we have achieve k sucess in j trials
       Z3[il,jl]=Z2[il,jl]*Z1[il,jl]#Probability(x<=k)*Probability(x>=k) assuming the hypothesis is correct this probabilty will max out., hence giving out the coordinates where coin can be said to be fair.
plt.figure(0)
plt.imshow(Z3)
plt.xlabel("Number of trials")
plt.ylabel("Number of Success")
plt.colorbar()
plt.show
