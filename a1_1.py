# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 02:36:13 2019

@author: wangjam
"""
from numpy.random import choice

sample=[0,1]
N=5000
N_sample=100
i=0

p_count=0
while (i<N):
    c_h=0#rep by 1
    j=0
    while(j<N_sample):
        x=choice(sample)
        if (x==1):
            c_h+=1
        j+=1
    if (c_h<45) or (c_h>55) :
        p_count+=1
    i+=1
print("probability of getting heads more than 55 or less than 45 in 100 sample of coin toss",p_count/N)