# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 2019
@author: Philip Lucas
Due Mon Sep 9 2019
Triangle in a Box
"""
import numpy as np


#box side sizes
x = 1
y = 1
z = 1

#counting list for triangles made randomly
Obtuse = []
Acute = []
Right = []

i=0

number = 1000000.0  #number of tirals

R = 2 # dimension of univerise 


while i < number:
    
    #points of triangle with box scaling
    
    p1 = np.random.rand(R, 1)
    p2 = np.random.rand(R, 1) 
    p3 = np.random.rand(R, 1)
    
    #seperation vectors X axis
    
    r1x = x*(p1[0] - p2[0])
    r2x = x*(p1[0] - p3[0])
    r3x = x*(p3[0] - p2[0])
    
    #seperation vectors y axis
    
    r1y = y*(p1[1] - p2[1])
    r2y = y*(p1[1] - p3[1])
    r3y = y*(p3[1] - p2[1])
    
    #seperation vectors X axis
    if R >= 3: 
        r1z = z*(p1[2] - p2[2])
        r2z = z*(p1[2] - p3[2])
        r3z = z*(p3[2] - p2[2])
    
    if R < 3:
        
        "For 2-D" # comment out for 3D
        
        r1L = np.sqrt(r1x**2 + r1y**2) #side r1 length 2D
        r2L = np.sqrt(r2x**2 + r2y**2) #side r2 length 2D
        r3L = np.sqrt(r3x**2 + r3y**2) #side r1 length 2D
    
    if R >= 3:
        "For 3-D" #uncomment out for 3D
        
        r1L = np.sqrt(r1x**2 + r1y**2 + r1z**2) #side r1 length 3D
        r2L = np.sqrt(r2x**2 + r2y**2 + r2z**2) #side r2 length 3D
        r3L = np.sqrt(r3x**2 + r3y**2 + r3z**2) #side r1 length 3D

    "Theta of the side farthest from the longest side"
    
    #if statements determine which side is "c" for law of cosines
    
    if r1L >= r2L and r1L > r3L:
        c = r1L
        a = r2L
        b = r3L
        
    elif r2L > r1L and r2L >= r3L:
        c = r2L
        a = r1L
        b = r3L
        
    elif r3L >= r1L and r3L > r2L:
        c = r3L
        a = r1L
        b = r2L 
        
    arg = ((c**2 - a**2 -b**2)/(-2*a*b))
    Theta = np.arccos( arg )
    Thetadegree = np.rad2deg(Theta)
    if Thetadegree < 90 :
        acute = 1
        Acute.append(acute)
        #print "acute"
    elif Thetadegree > 90:
        obtuse = 1
        Obtuse.append(obtuse)
        #print "obtuse"
#    elif Thetadegree == 90:
#        right = 1
#        Right.append(right)
        #print "right"
    i+=1
print R, "-Dimension" 
print "Percent Obtuse triangles in",number,"trials is", float(np.sum(Obtuse)/number)*100, "%"
print "Percent Acute triangles in",number,"trials is", float(np.sum(Acute)/number)*100, "%"
print "Percent Right triangles in",number,"trials is", float(np.sum(Right)/number)*100, "%"