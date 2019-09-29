# -*- coding: utf-8 -*-
"""
@author: Philip Lucas
Warmup Homework 3
Binomial Data
"""
###################################################################################
import numpy as np
# change Data .txt location to work for you.
Data = np.loadtxt("Phillip_binomial.txt")
datalist = [] #data extracted from file
success = []
h = [] #mu-mu estimate
i = 0 
j = 0
x = len(Data)#length of data list
N = x
for i in range(0,x):
    g = Data[i] #pulling data 
    datalist.append(g) #putting data in a list
success_guess = np.sum(datalist)/x #anaylitical mean of data
k=0
trial = 10000
while k < trial:
    while j <= N:
        s = np.sum(np.random.binomial(x,success_guess,N))/(x*N*1.0)
        j += 1
        h.append(s)
    d = np.mean(h)
    success.append(d)
    k+=1
mean = np.mean(success)
un =  np.abs((success_guess-mean)/success_guess)
print "Estimate of percent success from data",success_guess
print "trial percentage",mean
print "Percent uncertanty", np.round(un*100.0, 3),"%"
print"Percent success range:" ,round(success_guess-un,3),"to",round(success_guess+un,3)
