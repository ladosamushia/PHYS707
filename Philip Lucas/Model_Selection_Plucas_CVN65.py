#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model Selection homework Data Analysis

Philip Lucas 

Wrote in Spyder3 

"""

#Part 1: 
# this code works well for larger data sets and might lose some relaibility in smaller sets. 
# a future density function to determine validity of sample size can improve this process. 
    
    
import numpy as np
from matplotlib import pyplot as plt

mu_1 = 1.0 # Mean 1
mu_2 = 1.2 # Mean 2
sigma_1 = 1.0 # Standard Deviation 1
sigma_2 = 2.0 # Standard Deviation 2
N_1 = 10000 #sample size (number of data points collected)
N_2 = 10000 #sample size of Models 

Data = np.random.normal(mu_1,sigma_1,N_1) #mock datapoints

A = np.random.normal(mu_1,sigma_1,N_2) # Model A
B = np.random.normal(mu_2,sigma_1,N_2) # Model B
C = np.random.normal(mu_1,sigma_2,N_2) # Model C
D = np.random.normal(mu_2,sigma_2,N_2) # Model D

#the following are list for how the data deviates above or below the expected model
lowa = []
lowb = []
lowc = []
lowd = []
higha = []
highb = []
highc = []
highd = []


#The following tests the model a good model will be 50/50 above and below the slope of 1 
#This collects the data for how often it deviates from a ratio of 1
#This helps test the mean of the model to data. A good mean should be about 1

j = 0

#test A
while j < N_2: 
    if (Data[j],A[j]) < (Data[j],Data[j]):
        LOWA = 1
        lowa.append(LOWA)
    elif (Data[j],A[j]) > (Data[j],Data[j]):
        HIGHA = 1
        higha.append(HIGHA)
    j += 1
j = 0
#test B
while j < N_2: 
    if (Data[j],B[j]) < (Data[j],Data[j]):
        LOWB = 1
        lowb.append(LOWB)
    elif (Data[j],B[j]) > (Data[j],Data[j]):
        HIGHB = 1
        highb.append(HIGHB)
    j += 1
#test C
j = 0
while j < N_2: 
    if (Data[j],C[j]) < (Data[j],Data[j]):
        LOWC = 1
        lowc.append(LOWC)
    elif (Data[j],C[j]) > (Data[j],Data[j]):
        HIGH = 1
        highc.append(HIGH)
    j += 1
#test D
j = 0
while j < N_2: 
    if (Data[j],D[j]) < (Data[j],Data[j]):
        LOWD = 1
        lowd.append(LOWD)
    elif (Data[j],D[j]) > (Data[j],Data[j]):
        HIGHD = 1
        highd.append(HIGHD)
    j += 1
j = 0

#Testing how circular the data to model is. A good fit sould be circular a bad fit should be elliptical

AA = ((np.max(Data)-np.min(Data))/(np.max(A)-np.min(A)))
BB = ((np.max(Data)-np.min(Data))/(np.max(B)-np.min(B)))
CC = ((np.max(Data)-np.min(Data))/(np.max(C)-np.min(C)))
DD = ((np.max(Data)-np.min(Data))/(np.max(D)-np.min(D)))
if  AA > 1:
    AA = ((np.max(Data)-np.min(Data))/(np.max(A)-np.min(A)))**-1
if BB > 1: 
    BB = ((np.max(Data)-np.min(Data))/(np.max(B)-np.min(B)))**-1
if CC > 1: 
    CC = ((np.max(Data)-np.min(Data))/(np.max(C)-np.min(C)))**-1
if DD > 1:
    DD = ((np.max(Data)-np.min(Data))/(np.max(D)-np.min(D)))**-1


#The following finds the percent confidence in the standard deviation and the means "XM" calculates mean confidence
#The XS computes the standard deviation confidence

AM = (1-np.abs(np.sum(lowa)/(np.sum(lowa + higha)) - np.sum(higha)/(np.sum(lowa + higha))))
BM = (1-np.abs(np.sum(lowb)/(np.sum(lowb + highb)) - np.sum(highb)/(np.sum(lowb + highb))))
CM = (1-np.abs(np.sum(lowc)/(np.sum(lowc + highc)) - np.sum(highc)/(np.sum(lowc + highc))))
DM = (1-np.abs(np.sum(lowd)/(np.sum(lowd + highd)) - np.sum(highd)/(np.sum(lowd + highd))))


#determining the overall confidence of the model with percent averages



percentA = (AM+AA)/2
percentB = (BM+BB)/2
percentC = (CM+CC)/2
percentD = (DM+DD)/2


print("")
if percentA > percentB and percentA > percentC and percentA > percentD:
    print ("Model A is best")
elif percentB > percentC and percentB>percentD: 
    print("Model B is best")
elif percentC > percentD:
    print("Model C is best")
else:
    print("Model D is best")
print("")
print("Confidence in model A:",percentA*100,"%")
print("Confidence in model A Mean:",AM*100,"%")
print("Confidence in model A Sigma:",AA*100,"%")
print("")
print("Confidence in model B:",percentB*100,"%")
print("Confidence in model B Mean:",BM*100,"%")
print("Confidence in model B Sigma:",BB*100,"%")
print("")
print("Confidence in model C:",percentC*100,"%")
print("Confidence in model C Mean:",CM*100,"%")
print("Confidence in model C Sigma:",CC*100,"%")
print("")
print("Confidence in model D:",percentD*100,"%")
print("Confidence in model D Mean:",DM*100,"%")
print("Confidence in model D Sigma:",DD*100,"%")


plt.figure(1)
plt.axis('equal')
plt.title('Model A', fontsize=20)
plt.plot(Data,A, '.')
plt.plot(A,A,'.')
plt.plot(Data,Data,'.')
plt.figure(2)
plt.axis('equal')
plt.title('Model B', fontsize=20)
plt.plot(Data,B,'.')
plt.plot(B,B,'.')
plt.plot(Data,Data,'.')
plt.figure(3)
plt.axis('equal')
plt.title('Model C', fontsize=20)
plt.plot(Data,C, '.')
plt.plot(C,C,'.')
plt.plot(Data,Data,'.')
plt.figure(4)
plt.axis('equal')
plt.title('Model D', fontsize=20)
plt.plot(Data,D,'.')
plt.plot(D,D,'.')
plt.plot(Data,Data,'.')

#%% Part 2

#this code doesn't give a numerical confidence but it does produce a good graphical choice in determining if gaussian ver 
#cauchy is a better pick of the two. It does nothing to compare cauchy's to eachother. That will require further work. 
import scipy
from scipy import stats
N_3 = 1000
#Data2 = np.random.normal(1,1,N_3) #mock datapoints
Data2 = stats.cauchy.rvs(loc=0, scale=0, size=N_3)
#Data2 = np.random.standard_cauchy(N_3)

#Models
X = np.random.normal(1,1,N_3)
Y = stats.cauchy.rvs(loc=0, scale=3, size=N_3)
Z = np.random.standard_cauchy(N_3)


plt.figure(5)
plt.axis('equal')
plt.title('Model X', fontsize=20)
plt.plot(Data2,X, 'r.')
plt.plot(X,X,'b.')

plt.figure(6)
plt.axis('equal')
plt.title('Model Y', fontsize=20)
plt.plot(Data2,Y, 'r.')
plt.plot(Y,Y,'b.')

plt.figure(7)
plt.axis('equal')
plt.title('Model Z', fontsize=20)
plt.plot(Data2,Z, 'r.')
plt.plot(Z,Z,'b.')

