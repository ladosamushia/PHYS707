#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Confidence in Coin flips

@author: Philip Lucas

Referenced Blaine Fry with his permission for trial loops 

Code also test binomial data from warmup. If you want to test new data change
loadtxt to new data or comment out lines 18 to 40 and re-define lines 57-59

Made on Spyder3 (ChromeOS Linux Dev: Debian)
"""
import numpy as np
import numpy.random as rand
from matplotlib import pyplot as plt
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
trial = 1000#number of trials to test mean of dataset
while k < trial:
    while j <= N:
        s = np.sum(np.random.binomial(x,success_guess,N))/(x*N*1.0)
        j += 1
        h.append(s)
    d = np.mean(h)
    success.append(d)
    k+=1
mean = np.mean(success)
def coin_flip(Nsides,Nflips):
    return rand.randint(0,Nsides,size=Nflips)
def count_value(array,value):
    running_count = 0
    for i in range(len(array)):
        if array[i] == value:
            running_count += 1
    return running_count
Ntrials = 1000 #number of trials about pfair
results = []
for i in range(1,Ntrials+1):
    experiment = coin_flip(2,i)
    results.append(float(count_value(experiment,1))/i)
t = np.arange(0.00001, Ntrials, 1)
#test if fair 
n = x #Ntrials #number of flips for test
N = x #number of trials for test
p = mean #proability
pfair = 0.5 # what you define as a fair model 
percentallowed = np.abs(pfair - (1.5/np.sqrt(N) + pfair ))
test = mean #np.sum((np.random.binomial(n, p, N)))/(n*N)
if test >= -1.5/np.sqrt(N) + pfair and test <= 1.5/np.sqrt(N) + pfair:
    print("Might be Fair")
    print((np.abs(test-pfair)*100),"% away from fair mean")
    print((np.abs(-1.5/np.sqrt(N))*100),"% max expected from a fair mean")
elif np.abs((test - (-1.5/np.sqrt(N) + pfair))) <= percentallowed or np.abs((test - (1.5/np.sqrt(N) + pfair))) <= percentallowed:
    print("Maybe fair")
    print((np.abs(test-pfair)*100),"% away from fair mean")
    print((np.abs(-1.5/np.sqrt(N))*100),"% max expected from a fair mean")
elif test < -1.5/np.sqrt(N) + pfair:
    print ("Probabily isn't fair")
    print((np.abs(test-pfair)*100),"% away from fair mean")
    print((np.abs(-1.5/np.sqrt(Ntrials))*100),"% max expected from a fair mean")
    g = test+percentallowed
    if test+percentallowed > 1:
        g = 1
    h = test-percentallowed
    if test-percentallowed < 0:
        h = 0
    print("Likely Probability:", h,"to", g)
elif test > 1.5/np.sqrt(N) + pfair:
    print ("Probabily isn't fair")
    print((np.abs(test-pfair)*100),"% away from fair mean")
    print((np.abs(1.5/np.sqrt(N))*100),"% max expected from a fair mean")
    g = test+percentallowed
    if test+percentallowed > 1:
        g = 1
    h = test-percentallowed
    if test-percentallowed < 0:
        h = 0
    print("Likely Probability:", h,"to", g)
z = 1
print("Number of trials:",x)
if p < pfair: 
    while 1.5/np.sqrt(z) +p >= -1.5/np.sqrt(z) +pfair :
        z += 1
        if 1.5/np.sqrt(z) +p <= -1.5/np.sqrt(z) +pfair :
            print ("Recommended minnimum number of trials:",z)
            break
elif p > pfair: 
    t = 1
    while 1.5/np.sqrt(z) +pfair >= -1.5/np.sqrt(z) +p :
        z += 1
        if 1.5/np.sqrt(z) +pfair <= -1.5/np.sqrt(z) +p:
            print ("Recommended minimum number of trial:",z)
            break
if p > pfair:
    hh = 1.5/np.sqrt(z) +pfair
else:
    hh = 1.5/np.sqrt(z) +p
# then, generate the plot related bits
plt.figure(1)
plt.title('Coin Experiment')
plt.ylim(0,1)
plt.ylabel(r'$\mu$')
plt.xlabel('Number of Flips')
plt.grid()
for i in range(1,1+len(results)):
    plt.plot(i,results[i-1],'b.',alpha=0.5, markersize=0.9)
    plt.plot(i, 1/i**2)
#plt.plot(t+1,  1.5/np.sqrt(t) + pfair, 'purple')
#plt.plot(t+1, -1.5/np.sqrt(t) + pfair, 'purple')
plt.fill_between(t+1, 1.5/np.sqrt(t) +0.5, -1.5/np.sqrt(t) +0.5 ,color = 'purple', alpha=0.25)
plt.plot(np.linspace(1,Ntrials+1,num=Ntrials),np.ones(Ntrials)*0.5,'purple')
plt.plot([N], [test], marker='o', markersize=3, color="red")
plt.plot([z], [hh], marker='^', markersize=7, color="black")
q = percentallowed
r = percentallowed
if test + q  >=1:
    q = 0
if test + r  <=0:
    r = 0
plt.errorbar([N], [test], yerr=[[q], [r]],color="black",fmt='.')
#plt.plot(t+1,  1.5/np.sqrt(t) + p, 'blue')
#plt.plot(t+1, -1.5/np.sqrt(t) + p, 'blue')
plt.fill_between(t+1, 1.5/np.sqrt(t) +p, -1.5/np.sqrt(t) +p ,color = 'blue', alpha=0.125)
#additional analysis for plotting makes the tighter plots fitted to a standard devation of a 1000 trials at select points 
fiveN = np.random.binomial(5,0.5,5000)
fiveNmean = np.mean(fiveN)/5
fiveNSTD = np.std(fiveN)/5
plt.errorbar([5], [fiveNmean], yerr=[[fiveNSTD], [fiveNSTD]],color="b",fmt='o')
tenN = np.random.binomial(10,0.5,5000)
tenNmean = np.mean(tenN)/10
tenNSTD = np.std(tenN)/10
plt.errorbar([10], [tenNmean], yerr=[[tenNSTD], [tenNSTD]],color="b",fmt='o')
fiftyN = np.random.binomial(50,0.5,5000)
fiftyNmean = np.mean(fiftyN)/50
fiftyNSTD = np.std(fiftyN)/50
plt.errorbar([50], [fiftyNmean], yerr=[[fiftyNSTD], [fiftyNSTD]],color="b",fmt='o')
onehN = np.random.binomial(100,0.5,5000)
onehNmean = np.mean(onehN)/100
onehNSTD = np.std(onehN)/100
plt.errorbar([100], [onehNmean], yerr=[[onehNSTD], [onehNSTD]],color="b",fmt='o')
twohN = np.random.binomial(200,0.5,5000)
twohNmean = np.mean(twohN)/200
twohNSTD = np.std(twohN)/200
plt.errorbar([200], [twohNmean], yerr=[[twohNSTD], [twohNSTD]],color="b",fmt='o')
fourhN = np.random.binomial(400,0.5,5000)
fourhNmean = np.mean(fourhN)/400
fourhNSTD = np.std(fourhN)/400
plt.errorbar([400], [fourhNmean], yerr=[[fourhNSTD], [fourhNSTD]],color="b",fmt='o')
sixhN = np.random.binomial(600,0.5,5000)
sixhNmean = np.mean(sixhN)/600
sixhNSTD = np.std(sixhN)/600
plt.errorbar([600], [sixhNmean], yerr=[[sixhNSTD], [sixhNSTD]],color="b",fmt='o')
plt.fill_between(t+1, 1/np.sqrt(4*t) +pfair, -1/np.sqrt(4*t) +pfair ,color = 'g', alpha=0.5)
plt.fill_between(t+1, 1/np.sqrt(4*t) +p, -1/np.sqrt(4*t) +p ,color = 'r', alpha=0.5)
