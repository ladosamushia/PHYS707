# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:46:20 2019

@author: Joe Ryan
"""
from numpy import arccos, pi, random, sqrt

l = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #Side lengths of box in d dimensions.
L = 10**6 #Number of trials.
d = len(l) #Number of dimensions.

ac = []
ob = []
theta = []

for p in range(0, L, 1):
    q = []
    for i in range(0, 3, 1):
        q.append(random.rand(1, d))
    #The above loop creates a list of three arrays (one for each
    #point of the triangle); each array contains the coordinates 
    #q_1, ..., q_d of the point represented by the array.
    
    a2 = []
    b2 = []
    c2 = []
    for p in range(0, d, 1):
        lqa = l[p]*(q[0][0][p] - q[1][0][p])
        lqb = l[p]*(q[0][0][p] - q[2][0][p])
        lqc = l[p]*(q[1][0][p] - q[2][0][p])
        
        a2.append(lqa**2)
        b2.append(lqb**2)
        c2.append(lqc**2)
        
    a = sqrt(sum(a2))
    b = sqrt(sum(b2))
    c = sqrt(sum(c2))
    #Lines 25-39 implement the generalized form of the Pythagorean theorem
    #in d dimensions: r_ij = [(q_i1 - q_j1)^2 + ... + (q_id - q_jd)^2]^(1/2)
    #for each side length a, b, c. The second index on q labels the
    #coordinate (e.g. x = 1, y = 2, z = 3 in 3 dimensions);
    #the indices i and j label the points themselves.
    
    A = (180/pi)*arccos((c**2 + b**2 - a**2)/(2*b*c)) #Angles in degrees,
    B = (180/pi)*arccos((c**2 + a**2 - b**2)/(2*a*c)) #from the law of
    C = (180/pi)*arccos((a**2 + b**2 - c**2)/(2*a*b)) #cosines.
    
    theta = [A, B, C] #List of angles.
    ac1 = sum(1 for i in theta if i <= 90) #Count number of acute angles.
    ob1 = sum(1 for i in theta if i >= 90) #Count number of obtuse angles.
    
    if ac1 == 3: #Acute triangle condition.
        ac.append(ac1)
    elif ac1 < 3: #Obtuse triangle condition.
        ob.append(ob1)
    
#Number of acute triangles divided by number of trials = P(acute).
print('P(acute) = ', len(ac)/L)
#Number of obtuse triangles divided by number of trials = P(obtuse).
print('P(obtuse) = ', len(ob)/L)

if all(elem == l[0] for elem in l):
    print(str(d) + '-dimensional box with equal side lengths.')
else:
    print(str(d) + '-dimensional box with unequal side lengths.')
    print('l =', l)

