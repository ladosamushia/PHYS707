#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:37:22 2019

@author: phil
"""

import numpy as np
import matplotlib.pyplot as plt
# change Data .txt location to work for you.
Data = np.loadtxt("Phillip_Uniform.txt")
datalist = [] #data extracted from file
difference = [] 
datamean = []
datastd = []
i = 0 
x = len(Data)#length of data list
N = list(range(1,x+1))
m=0
U = 10000
for i in range(0,x):
    g = Data[i] #pulling data 
    datalist.append(g) #putting data in a list
max_guess = np.mean(datalist)*2, #I trust the mean more than the max to be more accurate
K = list(np.linspace(0.0, 100.0, num=U))
l = 0    
while l <= 1000:    # iterates through to maxes of uniform distributions using my max guess 
    n = 0    
    while n <= 100:
        distribution2 = np.random.uniform(0,max_guess)
        max_fit2 = np.max(distribution2)
        n+=1
    datamean.append(max_fit2)
    l+=1       
maxerror = np.std(datamean)

print""
print"Values:"
print""
print"Max estimate:",max_guess,"+/-",(maxerror/max_guess)*100,"%"
print""
print"***Note values use 'round' for reasonable tabulation***"  
