# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:20:30 2019

@author: wangjam
"""
from numpy import arange 
from numpy.random import normal
from numpy import mean

N=1000 #no. of Expt.
max_sample=5000#number of maximum samples form the PDF
l=arange(1,max_sample,1)
mu1=0
sigma1=1
mu2=.1
sigma2=1

for j,jl in enumerate(l):
    p_count=0
    i=0
    while (i<=N):
        s1=normal(mu1, sigma1, jl)
        s2=normal(mu2, sigma2, jl)
        if (mean(s1)>mean(s2)):
            p_count+=1
        i+=1
    print(j)
    if(p_count/N)<.01:
        print("At least this much sampling is needed for this inference to be wrong: ",jl)
        break# no further calculation needed after maximum number of sampling is found