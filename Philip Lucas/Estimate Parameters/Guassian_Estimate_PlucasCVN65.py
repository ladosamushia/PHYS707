# -*- coding: utf-8 -*-
"""
Philip Lucas
Warmup Homework 3
Guassian Data
"""
import numpy as np
import matplotlib.pyplot as plt
# change Data .txt location to work for you.
Data = np.loadtxt("Phillip_Gauss.txt")
datalist = [] #data extracted from file
difference = [] #mu-mu estimate
datamean = []
datastd = []
i = 0 
x = len(Data)#length of data list
N = list(range(1,x+1)) #N for means and standard deviations standard notation
m=0
U = 10000
for i in range(0,x):
    g = Data[i] #pulling data 
    datalist.append(g) #putting data in a list
mu_guess = np.sum(datalist)/x #anaylitical mean of data
for i in range(0,x):
    h = (Data[i] - mu_guess)**2 # determining (mu-mu_guess)**2 for Standard Deviation calculation
    difference.append(h) #putting h in a list
sigma_guess = np.sqrt((1.0/(x-1.0))*np.sum(difference)) #analytical standard deviation of data Verified in Excel
K = list(np.linspace(0.0, 100.0, num=U))
while m <= U: # Testing sigma_guess and mean_guess with a random normal gaussian distribution
    distribution1 = np.random.normal(mu_guess, sigma_guess, m)
    mean_fit = np.mean(distribution1)
    stdev = np.std(distribution1)
    m+=1
l = 0    
while l <= 1000:    # iterates through to find mu and sigma values for error analysis 
    n = 0    
    while n <= 100:
        distribution2 = np.random.normal(mu_guess, sigma_guess, n)
        mean_fit2 = np.mean(distribution2)
        stdev2 = np.std(distribution2)
        n+=1
    datamean.append(mean_fit2)
    datastd.append(stdev2)
    l+=1       
muerror = np.std(datamean) + np.std(datastd) #standard deviations of my data for error bars
stderror = np.std(datastd)#standard deviation of my standard deviations
print""
print"Values:"
print""
print "Mu estimate:",round(mu_guess,1),"+/-",round(muerror,1)
print "Mu range:", round((mu_guess - muerror),1), 'to', round((mu_guess + muerror),1)
print "Standard Deviation estimate:", round(sigma_guess,2),"+/-", round(stderror,2)
print "Standard Deviation range:", round((sigma_guess - stderror),2), 'to', round((sigma_guess + stderror),2)
print "Variance range:", round((sigma_guess - stderror)**2,2), 'to', round((sigma_guess + stderror)**2,2)
print""
print "***Note values use 'round' for reasonable tabulation***"  
#plt.figure(1) # to check that data actually came from Gaussian distributions and to show seperation Verified in Excel
#plt.plot(K,np.sort(distribution1), color = 'g' )# plotting noise from low to high to make gaussian high to low shape
#plt.plot(N,np.sort(datalist), color = 'r' )
#plt.figure(2)
#plt.hist(datamean)
#plt.xlim(0,4)
#plt.figure(3)
#plt.hist(datastd)
#plt.xlim(0,4)
#plt.figure(4)
#plt.scatter(datamean,datastd,marker='.')
plt.figure(5)# how well does my model encapsulate the data
error = muerror
y = np.sort(distribution1)
plt.plot(N, np.sort(datalist), color = 'black' )
plt.fill_between(K, y-error, y+error,color = 'green')
plt.xlabel('Data Point order')
plt.ylabel('Data point value')
plt.title("Ordered Guassian Noise comparison")
