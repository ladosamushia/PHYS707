# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 2019
@author: Philip Lucas
Due Mon Sep 9 2019
Poker
"""
import numpy as np
import random
#Basic readout infomation
#[0] entries are faces 1=hearts 2=diamonds 3=spades and 4=clubs
#[1] entries are card values 14=ace 13=king 12=queen and 11=jack
# All other entries match card number
#Assumptions:
#No Wild Cards
#No Two Card Draw
#line 160-190 handles draw cases
number = 1000000.0 #number of trials 
Hearts = 4
Diamonds = 3
Spades = 2
Clubs = 3
Ace = 14
King = 13
Queen = 12
Jack = 11 
P1 = [Clubs,7] #Building Players cards
P2 = [Hearts, 4]
P3 = [Diamonds, 4]
P4 = [Diamonds, 5]
P5 = [Diamonds, 6]
Lose =[] #Stat list
Win =[]
Draw =[]
i = 0 
acceptableriskwin = 3/4 
while i < number:
    cpoint = 0 #Computer points
    ppoint = 0 #player points
    lose = 0 
    win = 0
    draw = 0
#    P1 = [random.randint(1,4),random.randint(2,14)]     # if you want the player to have random cards 
#    P2 = [random.randint(1,4),random.randint(2,14)] 
#    P3 = [random.randint(1,4),random.randint(2,14)] 
#    P4 = [random.randint(1,4),random.randint(2,14)] 
#    P5 = [random.randint(1,4),random.randint(2,14)] 
    C1 =[random.randint(1,4),random.randint(2,14)]     #Building Computer cards
    C2 =[random.randint(1,4),random.randint(2,14)]
    C3 =[random.randint(1,4),random.randint(2,14)]
    C4 =[random.randint(1,4),random.randint(2,14)]
    C5 =[random.randint(1,4),random.randint(2,14)] 
    if P2 == P1: #If statements prevent the computer from drawing a player card at the same time or the same card more than once 
        P2 =[random.randint(1,4),random.randint(2,14)]
    if P3 == P1 or P3 == P2:
        P3 =[random.randint(1,4),random.randint(2,14)] 
    if P4 == P1 or P4 == P2 or P4 == P3:
        P4 =[random.randint(1,4),random.randint(2,14)] 
    if P5 == P1 or P5 == P2 or P5 == P3 or P5 == P4:
        P5 =[random.randint(1,4),random.randint(2,14)] 
    if C1 == P1 or C1 == P2 or C1 == P3 or C1 == P4 or C1 == P5:
        C1 =[random.randint(1,4),random.randint(2,14)]
    if C2 == C1 or C2 == P1 or C2 == P2 or C2 == P3 or C2 == P4 or C2 == P5:
        C2 =[random.randint(1,4),random.randint(2,14)]
    if C3 == C2 or C3 == C1 or C3 == P1 or C3 == P2 or C3 == P3 or C3 == P4 or C3 == P5:
        C3 =[random.randint(1,4),random.randint(2,14)]
    if C4 == C3 or C4 == C2 or C4 == C1 or C4 == P1 or C4 == P2 or C4 == P3 or C4 == P4 or C4 == P5:
        C4 =[random.randint(1,4),random.randint(2,14)]
    if C5 == C4 or C5 == C3 or C5 == C2 or C5 == C1 or C5 == P1 or C5 == P2 or C5 == P3 or C5 == P4 or C5 == P5:
        C5 =[random.randint(1,4),random.randint(2,14)]
    i+= 1
    LP = list([P1[1], P2[1], P3[1], P4[1], P5[1]])#cards as a list for player
    LPsorted = list.sort(LP) 
    LP2 = list([P1[0], P2[0], P3[0], P4[1], P5[0]])
    LPsorted2 = list.sort(LP2)
    if LP[0] == LP[3]:    #Checking for 4 of a kind
        ppoint += 100000 + P1[1]
    elif LP[1] == LP[4]:
        ppoint += 100000 + P5[1]
    else: #Checking for a full house 
        if LP[0] == LP[2] and LP[3] == LP[4]:
            ppoint +=10000 + LP[2] 
        elif  LP[0] == LP[1] and LP[2] == LP[4]:
            ppoint +=10000 + LP[2] 
        else: #check for a straights all types
            if LP[1] == LP[0] + 1 and LP[2] == LP[1] +1 and LP[3] == LP[2] +1 and LP[4] == LP[3] +1 or LP[4] == LP[3] + 9 : # +9 allows ace low
                ppoint += 1000 + P5[1] 
                if P1[0] == P2[0] and P2[0] == P3[0] and P3[0] == P4[0] and P4[0] == P5[0]:#looking for a straight flush 
                    ppoint += 1000000
                    if P1[1] + P2[1] + P3[1] + P4[1] + P5[1] == 60: # looking for a royal flush 
                        ppoint += 10000000 
            else:# checking for a flush 
                if P1[0] == P2[0] and P1[0] == P3[0] and P1[0] == P4[0] and P4[0] == P5[0]:
                    ppoint += 2000 +LP[4]
                else:# Checking for 3 of a kind 
                    if LP[0] == LP[2] or LP[1] == LP[4]: 
                        ppoint += 100 + LP[2]
                    else: # double pair 
                        if LP[0] == LP[1] and LP[2] == LP[3]:
                            ppoint += 20 + LP[3]
                        elif LP[0] == LP[1] and LP[3] == LP[4]:
                            ppoint += 20 + LP[4]
                        elif LP[1] == LP[2] and LP[3] == LP[4]:
                            ppoint += 20 + LP[4]
                        else: #Pair
                            if LP[0] == LP[1] or LP[1] == LP[2] or LP[2] == LP[3] or LP[3] == LP[4]: #Check for pairs
                                ppoint += 20 #no high card can break 20 points 
                                if LP[0] == LP[1] or LP[1] == LP[2]:
                                    ppoint += LP[1]
                                elif  LP[2] == LP[3] or LP[3] == LP[4]:
                                    ppoint += LP[3]
                            else: #Checking high card
                                ppoint += LP[4]
    LC = list([C1[1], C2[1], C3[1], C4[1], C5[1]]) #computer hand, everything repeats replacing "p" with "c" for varibles for computer
    LCsorted = list.sort(LC)
    LC2 = list([C1[0], C2[0], C3[0], C4[1], C5[0]])
    LCsorted2 = list.sort(LC2)
    if LC[0] == LC[3]:     #Checking for 4 of a kind 
        cpoint += 100000 + C1[1]
    elif LC[1] == LC[4]:
        cpoint += 100000 + C5[1]
    else: #Checking for a full house 
        if LC[0] == LC[2] and LC[3] == LC[4]:
            cpoint +=10000 + LC[2] 
        elif  LC[0] == LC[1] and LC[2] == LC[4]:
            cpoint +=10000 + LC[2] 
        else: #check for a straights all types
            if LC[1] == LC[0] + 1 and LC[2] == LC[1] +1 and LC[3] == LC[2] +1 and LC[4] == LC[3] +1 or LC[4] == LC[3] + 9 : # +9 allows ace low
                cpoint += 1000 + C5[1] 
                if C1[0] == C2[0] and C2[0] == C3[0] and C3[0] == C4[0] and C4[0] == C5[0]:#looking for a straight flush 
                    cpoint += 1000000
                    if C1[1] + C2[1] + C3[1] + C4[1] + C5[1] == 60: # looking for a royal flush 
                        cpoint += 10000000
            else:# checking for a flush 
                if C1[0] == C2[0] and C1[0] == C3[0] and C1[0] == C4[0] and C4[0] == C5[0]:
                    cpoint += 2000 +LC[4]
                else:# Checking for 3 of a kind 
                    if LC[0] == LC[2] or LC[1] == LC[4]: 
                        cpoint += 100 + LC[2]
                    else: # double pair 
                        if LC[0] == LC[1] and LC[2] == LC[3] or LC[0] == LC[1] and LC[3] == LC[4]:
                            cpoint += 20 + LC[3]
                        elif LC[1] == LC[2] and LC[3] == LC[4]:
                            cpoint += 20 + LC[3]
                        else:
                            if LC[0] == LC[1] or LC[1] == LC[2] or LC[2] == LC[3] or LC[3] == LC[4]: #Check for pairs
                                cpoint += 20 #no high card can break 20 points 
                                if LC[0] == LC[1] or LC[1] == LC[2]:
                                    cpoint += LC[1]
                                elif LC[2] == LC[3] or LC[3] == LC[4]:
                                    cpoint += LC[3]
                            else: #Checking high card
                                cpoint += LC[4]
            if ppoint < cpoint:         #point counting
                lose = 1
                Lose.append(lose)
            if ppoint > cpoint:
                win = 1
                Win.append(win)
#            if ppoint == cpoint: #if you want  draws to exist
#                draw = 1 
#                Draw.append(draw)
            if ppoint == cpoint: #if you want draws not to exist H D S C high
                if LC2[4] > LP2[4]:
                    lose = 1
                    Lose.append(lose)
                elif LP2[4] > LC2[4]:
                    win = 1
                    Win.append(lose)
                elif LC2[4] == LP2[4]:
                    if LC2[3] > LP2[3]:
                        lose = 1
                        Lose.append(lose)
                    elif LP2[3] > LC2[3]:
                        win = 1
                        Win.append(lose)
                    elif  LC2[3] == LP2[3]:
                        if LC2[2] > LP2[2]:
                            lose = 1
                            Lose.append(lose)
                        elif LP2[2] > LC2[2]:
                            win = 1
                            Win.append(lose)
                        elif  LC2[2] == LP2[2]:
                            if LC2[1] > LP2[1]:
                                lose = 1
                                Lose.append(lose)
                            elif LP2[1] > LC2[1]:
                                win = 1
                                Win.append(lose)
                               
print "Percent Chance to Win! :", (float(np.sum(Win))/number)*100.0 , "%"
print "Percent Chance to Draw! :", (float(np.sum(Draw))/number)*100.0 , "%"
print "Percent Chance to not Lose! :", (float(np.sum(Win)+np.sum(Draw))/number)*100.0 , "%"
print "Percent Chance to Lose! :", (float(np.sum(Lose))/number)*100.0 , "%"