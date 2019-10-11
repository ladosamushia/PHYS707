# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:18:19 2019

@author: wangjam
"""

import numpy as np
import matplotlib.pyplot as plt
poisson=np.loadtxt("Z:/Modelling/data/Tomthin_Poisson.txt")
gauss=np.loadtxt("Z:/Modelling/data/Tomthin_Gauss.txt")
uniform=np.loadtxt("Z:/Modelling/data/Tomthin_Uniform.txt")
binomial=np.loadtxt("Z:/Modelling/data/Tomthin_binomial.txt")
mean_poisson=poisson.sum()/poisson.size
error_mean_poisson=np.sqrt(mean_poisson/poisson.size)#possible deviation in mean i.e variance should pop up
#plt.hist(poisson)
mean_gauss=gauss.sum()/gauss.size
sigma_gauss=0
for il,i in enumerate(gauss):
    sigma_gauss+=(i-mean_gauss)**2
sigma_gauss=np.sqrt(sigma_gauss/gauss.size)
error_mean_gauss=sigma_gauss
error_sigma_gauss=1/(np.sqrt(2*(gauss.size-1)))#https://web.eecs.umich.edu/~fessler/papers/files/tr/stderr.pdf
#plt.hist(gauss)
probabilty_of_success=binomial.sum()/(binomial.size)*2
error_probabilty_of_success=np.sqrt(probabilty_of_success*(1-probabilty_of_success)/(binomial.size))#possible deviation in mean i.e variance should pop up
#plt.hist(binomial)
a_uniform=min(uniform)
b_uniform=max(uniform)#if this was the lmax meant by question not clear??
lmax=(a_uniform+b_uniform)/2#area under CDF of uniform distribtuion
error_lmax=np.sqrt(1/12)*(b_uniform-a_uniform)
#plt.hist(uniform)