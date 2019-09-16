# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:01:59 2019

@author: jwryan
"""

from random import shuffle
from numpy import arange
from itertools import groupby
from operator import itemgetter

a1 = [[1, 's'], [10, 's'], [11, 's'], [12, 's'], [13, 's']] #My hand.

b1 = ['c', 's', 'h', 'd']
b2 = arange(1, 14, 1)
a = []

for x in b2: #This loop creates the deck.
    for y in range(0, 4, 1):
        a.append([(x), b1[y]])  

for z in range(0, 5, 1): #This loop removes my hand from the deck.
    a.remove(a1[z])
    
gcount = 0
Mywin = 0
Oppwin = 0
gnumber = 10**6

for games in range(0, gnumber, 1):
    gcount += 1
    print(gcount/gnumber) #Progress bar
    Myscore = [0]
    Oppscore = [0]
    
    shuffle(a) #Shuffles deck.
    
    a2 = [a[0], a[1], a[2], a[3], a[4]]
    #^This line chooses the first five cards of the shuffled deck;
    #this is my opponent's hand
    
    a11 = []
    a12 = []
    a21 = []
    a22 = []
    
    for z in range(0, 5, 1):
        a11.append(a1[z][0]) #List of values of the cards in my hand.
        a12.append(a1[z][1]) #List of suits of the cards in my hand.
        a21.append(a2[z][0]) #List of values of cards in my opponent's hand.
        a22.append(a2[z][1]) #List of suits of cards in my opponent's hand.
    
    #The following lines look for winning card combinations in both hands.
    ##HIGH CARD CRITERIA
    Value = 1
    if max(a11) > max(a21):
        Myscore.append(Value)
        Oppscore.append(0)
    if max(a21) > max(a11):
        Oppscore.append(Value)
        Myscore.append(0)
    
    ##ONE PAIR CRITERIA
    Value = 2
    pp1 = set([i for i in a11 if a11.count(i)==2])
    pp2 = set([i for i in a21 if a21.count(i)==2])
    if len(pp1) == 1:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(pp2) == 1:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##TWO PAIR CRITERIA
    Value = 3
    pp1 = set([i for i in a11 if a11.count(i)==2])
    pp2 = set([i for i in a21 if a21.count(i)==2])
    if len(pp1) == 2:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(pp2) == 2:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##THREE OF A KIND CRITERIA
    Value = 4
    pp1 = set([i for i in a11 if a11.count(i)==3])
    pp2 = set([i for i in a21 if a21.count(i)==3])
    if len(pp1) == 1:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(pp2) == 1:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##STRAIGHT CRITERIA
    Value = 5
    for k, g in groupby(enumerate(sorted(a11)), lambda ix : ix[0] - ix[1]):
        s1 = list(map(itemgetter(1), g))
    for k, g in groupby(enumerate(sorted(a21)), lambda ix : ix[0] - ix[1]):
        s2 = list(map(itemgetter(1), g))
    if len(s1) == 5:
        Myscore.append(Value)
        Oppscore.append(0)
    if len(s2) == 5:
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##FLUSH CRITERIA
    Value = 6
    if all(elem == a12[0] for elem in a12):
        Myscore.append(Value)
        Oppscore.append(0)
    if all(elem == a22[0] for elem in a22):
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##FULL HOUSE CRITERIA
    Value = 7
    p1 = set([i for i in a11 if a11.count(i)==2])
    p2 = set([i for i in a21 if a21.count(i)==2])
    pp1 = set([i for i in a11 if a11.count(i)==3])
    pp2 = set([i for i in a21 if a21.count(i)==3])
    if (len(p1) == 1 and len(pp1) == 1):
        Myscore.append(Value)
        Oppscore.append(0)
    if (len(p2) == 1 and len(pp2) == 1):
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##THREE OF A KIND CRITERIA
    Value = 8
    pp1 = set([i for i in a11 if a11.count(i)==4])
    pp2 = set([i for i in a21 if a21.count(i)==4])
    if (len(pp1) == 1 and len(pp2) != 1):
        Myscore.append(Value)
        Oppscore.append(0)
    if (len(pp2) == 1 and len(pp1) != 1):
        Oppscore.append(Value)
        Myscore.append(0)
        
    ##STRAIGHT FLUSH CRITERIA
    Value = 9
    for k, g in groupby(enumerate(sorted(a11)), lambda ix : abs(ix[0] - ix[1])):
        s1 = list(map(itemgetter(1), g))
    for k, g in groupby(enumerate(sorted(a21)), lambda ix : abs(ix[0] - ix[1])):
        s2 = list(map(itemgetter(1), g))
    if ((len(s1) == 5) and (all(elem == a12[0] for elem in a12))):
            Myscore.append(Value)
            Oppscore.append(0)
    if ((len(s2) == 5) and (all(elem == a22[0] for elem in a22))):
            Oppscore.append(Value)
            Myscore.append(0)
    
    ##ROYAL FLUSH CRITERIA
    Value = 10
    RF = [1, 10, 11, 12, 13]
    if ((all(elem in a11 for elem in RF)) and all(elem == a12[0] for elem in a12)):
        Myscore.append(Value)
        Oppscore.append(0)
    if ((all(elem in a21 for elem in RF)) and all(elem == a22[0] for elem in a22)):
        Oppscore.append(Value)
        Myscore.append(0)
    
    if max(Myscore) > max(Oppscore):
        Mywin += 1
    if max(Oppscore) > max(Myscore):
        Oppwin += 1
              
print('P(W) = ', Mywin/gcount)
print('P(L) = ', Oppwin/gcount)
print('P(D) = ', (gcount-(Mywin+Oppwin))/gcount)


