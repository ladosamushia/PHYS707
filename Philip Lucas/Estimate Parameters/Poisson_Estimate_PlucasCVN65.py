# -*- coding: utf-8 -*-
"""

Philip Lucas
Warmup Homework 3
Poisson Data

The limit as "N" number of data points goes to infinity of a poisson distribution, the distribution 
goes toward a guassian distrubiton. So I am recycling the method I used to solve the guassian noise problem. 

"""
import numpy as np
# change Data .txt location to work for you.
Data = np.loadtxt("Phillip_Poisson.txt")
datalist = [] #data extracted from file
datamean = []
datastd = []
i = 0 
x = len(Data)#length of data list
N = list(range(1,x+1)) #N for means and standard deviations standard notation
U = 10000
l = 0
for i in range(0,x):
    g = Data[i] #pulling data 
    datalist.append(g) #putting data in a list
lambdaguess = np.sum(datalist)/x #anaylitical mean of data  
while l <= 1000:    # iterates through to find Lambda values for error analysis 
    n = 0    
    while n <= 100:
        distribution2 = np.random.poisson(lambdaguess)
        mean_fit2 = np.mean(distribution2)
        stdev2 = np.std(distribution2)
        n+=1
    datamean.append(mean_fit2)
    l+=1       
muerror = np.std(datamean) #standard deviations of my data for error bars
print""
print"Values:"
print""
print "Lambda estimate:",round(lambdaguess,1),"+/-",round(muerror,1)
print "Lambda range:", round((lambdaguess - muerror),1), 'to', round((lambdaguess + muerror),1)
print""
print "***Note values use 'round' for reasonable tabulation***"  

