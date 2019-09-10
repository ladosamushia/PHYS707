# -*- coding: utf-8 -*-
"""
Created on Fri Sep 06 13:38:10 2019

@author: Blaine Fry
Phys 707 Warmup
Coin Problem, Poker problem, and Triangle problem in one script
"""
# import relevant libraries
import numpy as np
from numpy import math
from matplotlib import pyplot as plt
import numpy.random as rand

"""
Coin Problem
Find the probability of flipping a coin 100 times and getting
more than 55 or less than 45 heads.
"""

# make a function to run the experiment
def coin_experiment(num_flips):
    N_trials = 10**4 # how many times to run the experiment
    success = 0 # counts how many times the result is < 45 or > 55
    for i in range(N_trials): # loop through the experiment N_trials times
        flips = rand.randint(0,2,size=num_flips) # generate an array of num_flips 1s and 0s
        if sum(flips)/float(num_flips) > .55 or sum(flips)/float(num_flips) < .45: # check number of heads
            success += 1
    return float(success)/float(N_trials) # return decimal value of success rate

print 'probability of getting > 55 or < 45 heads in 100 flips = ' + str(coin_experiment(100))

# make a graph of the results for varying num_flips
# generate the plot
plt.figure(1)
plt.title('Coin Experiment')
plt.xlabel('Number of Coin Flips')
plt.ylabel('P( < 45 or > 55)')
# loop through various numbers of flips
for i in range(1,100):
    plt.plot(i,coin_experiment(i),'b.')
# this gives some very interesting results that I'm not sure how to explain!!!
# (it would be fun to try sometime though)

"""
Poker Problem
Calculate the odds of a given five card hand winning in Poker.
"""

# make the deck of cards!
sealed_deck = [] # empty list to which the deck will be written
suits = ['Clubs','Hearts','Spades','Diamonds']
faces = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
# permute suits and faces together, with the value of the cards stored in a nested list
for i in suits:
    suit_key = i[0]
    value = 1
    for j in faces:
        sealed_deck.append([j+' of '+i,value,suit_key]) # each "card" is of the form ['name',value(1-13),suit]
        value += 1

deck = list(sealed_deck) # define a 'working deck,' so to speak

# make a function that will draw a hand of cards
def draw(cards_in_hand):
    hand = []
    for i in range(cards_in_hand):
        idx = rand.randint(0,len(deck)) # select a random index
        hand.append(deck[idx]) # append the card at that index to the hand
        deck.pop(idx) # remove that card from the deck
    return hand

# make a function to find the ranking of the hand (and the high card)
def evaluate_hand(hand):
    # unpack the hand into single lists
    values = [hand[i][1] for i in range(len(hand))]
    suits = [hand[i][2] for i in range(len(hand))]
    checked_values = []
    # set up booleans
    pair = False
    two_pair = False
    three_of_a_kind = False
    four_of_a_kind = False
    full_house = False
    straight = False
    flush = False
    straight_flush = False
    royal_flush = False
    # check for multiples (there's probably a less sloppy way to do this)
    for i in values:
        if values.count(i) == 2 and pair is True and i not in checked_values:
            two_pair = True
        if values.count(i) == 2 and pair is False:
            pair = True
        if values.count(i) == 3:
            three_of_a_kind = True
        if values.count(i) == 4:
            four_of_a_kind = True
        checked_values.append(i)
    # check for a full house
    if pair is True and three_of_a_kind is True:
        pair = False
        three_of_a_kind = False
        full_house = True
    # check for a straight
    if suits.count(suits[0]) == 5:
        straight = True
    # check for flushes
    flush_products = [] # store result of flush values multiplied together
    for i in range(1,13):
        flush_products.append(math.factorial(i+4)/math.factorial(i))
    flush_products.append(13*12*11*10*1) # royal flush value... duct tape solution
    if np.prod(values) in flush_products:
        flush = True
    if flush is True and straight:
        straight=False
        flush = False
        straight_flush = True
    if np.prod(values) == 13*12*11*10*1 and straight_flush:
        straight_flush = False
        royal_flush = True
    # find the high card for tie-breakers
    high_card = max(values)
    # record hand results
    hand_results = [pair,two_pair,three_of_a_kind,straight,flush,full_house,four_of_a_kind,straight_flush,royal_flush]
    hand_rank = 1
    for i in range(len(hand_results)): # objects in hand_results are in order of rank, so finding the idx in hand_results tells you the rank of the hand
        if hand_results[i]:
            hand_rank = i + 2
    return hand_rank,high_card

results = [] # stores results from experiment below (0=draw,1=win,2=loss)

# create some hands (change hand_1 below to select these)
squat = [['Ace of Clubs', 1, 'C'],['Two of Clubs', 2, 'C'],['Three of Hearts', 3, 'H'],['Four of Hearts', 4, 'H'],['Six of Spades', 6, 'S']]
pair = [['Two of Clubs', 2, 'C'],['Two of Diamonds', 2, 'D'],['Ace of Clubs', 1, 'C'],['Five of Spades', 5, 'S'],['Three of Diamonds', 3, 'D']]
three_of_a_kind = [['Two of Clubs', 2, 'C'],['Two of Diamonds', 2, 'D'],['Two of Hearts', 2, 'H'],['Five of Spades', 5, 'S'],['Three of Diamonds', 3, 'D']]
four_of_a_kind = [['Two of Clubs', 2, 'C'],['Two of Diamonds', 2, 'D'],['Two of Hearts', 2, 'H'],['Two of Spades', 2, 'S'],['Three of Diamonds', 3, 'D']]
royal_flush = [['Ace of Diamonds', 1, 'D'],['Ten of Diamonds', 10, 'D'], ['Jack of Diamonds', 11, 'D'], ['Queen of Diamonds', 12, 'D'], ['King of Diamonds', 13, 'D']]
# and so on...


for i in range(100000): 
    deck = list(sealed_deck) # shuffle the deck between each trial
    hand_1 = pair
    rank_1,high_card_1 = evaluate_hand(hand_1)
    hand_2 = draw(5) # hand 2 is randomly drawn from the deck
    rank_2,high_card_2 = evaluate_hand(hand_2)
    if rank_1 > rank_2: # compare the hands to determine a winner
        results.append(1)
    elif rank_1 == rank_2 and high_card_1 > high_card_2:
        results.append(1)
    elif rank_1 < rank_2:
        results.append(2)
    elif rank_1 == rank_2 and high_card_1 < high_card_2:
        results.append(2)
    else:
        results.append(0)

# print the results
print '\nHand 1 ' + str(hand_1)
print 'Wins = ' + str(results.count(1)) + ' | percentage = ' + str(100*float(results.count(1))/float(100000)) + '%'
print "Losses = " + str(results.count(2)) + ' | percentage = ' + str(100*float(results.count(2))/float(100000)) + '%'
print "Ties = " + str(results.count(0)) + ' | percentage = ' + str(100*float(results.count(0))/float(100000)) + '%'

"""
Triangle Problem
Randomly generate a triangle in a space with certain parameters and find
how many are obtuse!
"""

# make a function that uses the law of cosines to compute the angle opposite the largest side (sqrt(first argument))
def law_of_cosines(longest_squared,length2_squared,length3_squared):
    return np.arccos((length2_squared+length3_squared-longest_squared)/(2*np.sqrt(length2_squared)*np.sqrt(length3_squared)))

# define a function that checks for acuteness
def is_it_acute(point1,point2,point3):
    # find the side lengths
    # side length A: point2 - point 1
    A_squared = (point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2
    # side length B: point3 - point 2
    B_squared = (point3[0]-point2[0])**2 + (point3[1]-point2[1])**2 + (point3[2]-point2[2])**2
    # side length C: point1 - point 3
    C_squared = (point1[0]-point3[0])**2 + (point1[1]-point3[1])**2 + (point1[2]-point3[2])**2
    # Use Law of Cosines to find the angle opposite the longest side
    if A_squared > B_squared and A_squared > C_squared:
        theta = law_of_cosines(A_squared,B_squared,C_squared)
    if B_squared > A_squared and B_squared > C_squared:
        theta = law_of_cosines(B_squared,A_squared,C_squared)
    if C_squared > B_squared and C_squared > A_squared:
        theta = law_of_cosines(C_squared,B_squared,A_squared)
    if theta > np.pi/2:
        return False
    else:
        return True

# define a function that runs the triangle experiment
def triangle_experiment(l_1,l_2,l_3): # for 2D, l_3 = 0
    # set up the experiment
    N_trials = 10**4 # number of iterations to run the experiment through
    acute_count = 0 # keeps a running total of how many triangles are acute
    obtuse_count = 0 # ditto for obtuse
    # loop through individual trials N_trials times
    for i in range(N_trials):
        # generate three random points in the rectangular box
        p1 = [l_1*rand.rand(),l_2*rand.rand(),l_3*rand.rand()]
        p2 = [l_1*rand.rand(),l_2*rand.rand(),l_3*rand.rand()]
        p3 = [l_1*rand.rand(),l_2*rand.rand(),l_3*rand.rand()]
        if is_it_acute(p1,p2,p3):
            acute_count += 1
        else:
            obtuse_count += 1
    return acute_count,obtuse_count


# run the experiment for triangles generated in a 2D square region
acute_square,obtuse_square = triangle_experiment(1.,1.,0.)
# print the results
print('\nSquare: percent acute = ' + str(100*float(acute_square)/float(10**4)) + '%')
print('Square: percent obtuse = ' + str(100*float(obtuse_square)/float(10**4)) + '%')
# note: changing l_1 and l_2 but fixing l_1 = l_2 doesn't change the results, i.e.
# there is no dependence on L for squares

# now, investigate the dependence on l_2/l_1 in 2D
plt.figure(2) # make a figure to plot the upcoming results
plt.title('% Obtuse (Blue) for Varying Aspect Ratios')
plt.xlabel('Aspect Ratio (l_2/l_1)')
plt.ylabel('Percent')
# set up a loop for various aspect ratios
for i in range(1,200):
    acute,obtuse = triangle_experiment(float(i),20.,0.)
    plt.plot(i/20.,obtuse/10000.,'b.')
    plt.plot(i/20.,acute/10000.,'r.')

# Test dependence on dimensionality by setting l_3 != 0
acute_3D,obtuse_3D = triangle_experiment(1.,1.,1.)
# print the results
print('3D: percent acute = ' + str(100*float(acute_3D)/float(10**4)) + '%')
print('3D: percent obtuse = ' + str(100*float(obtuse_3D)/float(10**4)) + '%')
# roughly 55% are obtuse now... so dimensionality does make a difference!

print '\nDone!'
