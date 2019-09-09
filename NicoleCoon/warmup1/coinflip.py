# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:58:31 2019

@author: alecc
"""
import numpy as np


def flipper(coins):
    sets = 0
    setsmax = 100000 #number of sets tested
    inrange = 0 
    while sets <= setsmax:
        sets = sets + 1    
        x = np.random.binomial(coins, .5)#generates random fipped result
        if (coins*.45) <= x <= (coins*.55): #discrepancy test
            inrange = inrange + 1
        outrange = sets - 1 - inrange
    return(outrange/(sets-1))
print(flipper(100))
    

