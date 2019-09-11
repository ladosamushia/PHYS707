# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:47:38 2019

@author: alecc
"""
Pointsmax = 200
import numpy as np
def generator(N):
    n = 0
    xtotal = 0
    ytotal = 0
    while n < N:
        x = np.random.normal(loc = 0)
        y = np.random.normal(loc = .1)
        n = n+1
        xtotal = xtotal+x
        ytotal = ytotal + y
    xsum = xtotal/N
    ysum = ytotal/N
    if ysum>xsum:
        out = 1
    else:
        out = 0
    return(out)
def itera(N):
    m = 0
    M = 1000
    store = 0
    while m < M:
        m = m+1
        store = store + generator(N)
    return(1-store/M)
counter = 1+np.arange(Pointsmax)
j = np.zeros(Pointsmax)
for i in counter:
    k = itera(i)
    j[i-1] = k
import matplotlib as plot
plot.pyplot.scatter(counter,j)
    
