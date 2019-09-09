# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:56:19 2019

@author: alecc
"""
lx=1
ly=1
import random as rd
import numpy as np
def pointmake(): #make random point
    point = np.array([rd.uniform(0,lx),rd.uniform(0,ly)])
    return(point)

def sign(a,b,c):#tests for if obtuse
    return np.sign(c**2+b**2-a**2)
i = 0
ob = 0
while i < 1000000:
    point1 = pointmake()
    point2 = pointmake()
    point3 = pointmake()
    side1 = np.linalg.norm(point2 - point3) #length of each side
    side2 = np.linalg.norm(point1 - point3)
    side3 = np.linalg.norm(point2 - point1)
    i=i+1
    if side1 >= side2 and side1 >= side3:#check if side1 is longest
        if 0 >= sign(side1,side2,side3):
            ob = ob + 1
    if side2 >= side1 and side2 >= side3:
        if 0 >= sign(side2,side1,side3):
            ob = ob + 1
    if side3 >= side2 and side3 >= side1:
        if 0 >= sign(side3,side2,side1):
            ob = ob + 1
print(ob/(i))
"""
Does depend on ratio, not on l unless l causes floating point issues 

"""       