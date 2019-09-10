#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 3 2019
@author: Philip Lucas
Due Mon Sep 9 2019
Coin Flipping 
"""

import random
import numpy as np

i = 0 #iterative variable for number of sets of 

number = 1000.0 #number of sets of coinflips

Fair = [] #number of times the coinflips satisify critera 

while i < number: #limits number of flips
    
    flips = 0 # inital number of flips per set
    
    heads = 0 # inital number of heads for a flip set
    
    fair = 0 #number of flips sets satisfying the criteria 
    
    while flips < 100: #limits flips to 100
        
        coin = random.randint(0,1) # flips the coin
        
        flips += 1 # ads a flip to the number of flips during that set
        
        if coin == 1: # criteria for heads
            
            heads += 1 #adds a heads flip to count for the given set
            
    if heads > 55.0 or heads < 45.0: #criteria for coinflips
        
        fair = 1 #criteria counter
        
        Fair.append(fair) #makes criteria list of counter
        
    i+= 1 
#print("heads =", heads, "tails =", 100-heads)
print "Percent in range", 100*(np.sum(Fair)/(number)) ,"%"
