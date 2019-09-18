# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 03:01:03 2019

@author: wangjam
"""
# use only the first five and last condition for winning, else considered draw 
#Royal flush,Straight flush,Four of a kind, Full house, Flush,High Card,respectively
from numpy.random import choice
from numpy.random import shuffle
import numpy as np

def game_func(x):
    result=0
    x1=[]
    x2=[]
    for i,il in enumerate(x):
        x1.append(il[0])    
        x2.append(il[1])
    x2.sort(reverse=True)
#    print((abs(x2[0]-x2[1])))
    if ((x1[0]==x1[1]) and (x1[1]==x1[2]) and (x1[2]==x1[3]) and (x1[3]==x1[4])):#Royal flush or straigth flush case or flush
        if ((x2[0]==13) and (x2[1]==12) and (x2[2]==11) and (x2[3]==10) and (x2[4]==9)):#'A' is rep by 13 and so on.
            result=1#Royal flush case
        elif ((x2[0]==x2[1]+1) and (x2[1]==x2[2]+1) and (x2[2]==x2[3]+1) and (x2[3]==x2[4]+1)) :
            result=2#Straight flush case
        else:
            result=5#Flush
    elif (((x2[0]==x2[1]) and (x2[1]==x2[2]) and (x2[2]==x2[3])) or ((x2[1]==x2[2]) and (x2[2]==x2[3]) and (x2[3]==x2[4]))):
        result=3#Four of a kind
    elif (((x2[0]==x2[1]) and (x2[1]==x2[2]) and (x2[3]==x2[4])) or ((x2[1]==x2[2]) and (x2[2]==x2[3]) and (x2[1]==x2[4])) or ((x2[2]==x2[3]) and (x2[3]==x2[4]) and (x2[1]==x2[2]))):
        result=4#Full house
    else:
        result=x2[0]#max value for High card
    
    return result
sample=[]
suit=np.arange(1,5,1)# spades, hearts, diamonds and clubs resp.
card=np.arange(1,14,1)#high to low card respectively

for i,il in enumerate(suit):
    for j,jl in enumerate(card):
        sample.append([il,jl])
N=1000#no. of games
j=0
p_count1=0
p_count2=0
#shuffle(sample)#shuffled befor the games
while (j<N):
    print(j)
    res1=0
    res2=0
    player1=[]
    player2=[]
    shuffle(sample)
    current_sample=sample#shuffled before each the games
    card_dist=(np.arange(0,52,1)).tolist()#card selection in each game
    i=0
    while(i<10):
        ch=choice(card_dist)
        if (i<=4):
            player1.append(current_sample[ch])
        else:
            player2.append(current_sample[ch])
        card_dist.remove(ch)
        i+=1
    #card distribution done
    res1=game_func(player1)
    res2=game_func(player2)
    print(res2,res1)
    if (res1>res2):
        p_count1+=1
    elif (res1<res2):
        p_count2+=1
    j+=1
print("Probability that player1 will win : ",p_count1/N)
print("Probability that player2 will win : ",p_count2/N)    
print("Probability that game will be draw : ",1-(p_count2/N)-(p_count1/N))