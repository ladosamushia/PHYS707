# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 01:33:58 2019

@author: wangjam
"""
from numpy.random import choice
import numpy as np

N=10000
x = np.linspace(0, 1, 10000)
X=[]
i=0
d=2#dimension 
j=0
p_count=0
while(j<d):
    X.append(x)
    j+=1
X[1]*=100#scaling the second dimension by 8 or it can be with  number
while(i<N):
    x1=0
    x2=0
    x3=0
    d1=0
    d2=0
    d3=0
    for c,cl in enumerate(X):
        x1=choice(cl)
        x2=choice(cl)
        x3=choice(cl)
        d1+=(abs(x1-x2))**2
        d2+=(abs(x2-x3))**2
        d3+=(abs(x3-x1))**2
    #checking obtuse conition
    if (d1+d2<d3) or (d1+d3<d2) or (d3+d2<d1):
        p_count+=1
    
    i+=1
print("here is the probability : ", p_count/N)