# -*- coding: utf-8 -*-

from numpy import append, savetxt, loadtxt, arange, array
import sys

n = sys.argv[1]
syscount = 0

for p in range(0, 3, 1):
    syscount += 1
    if str(syscount) == n:
        break

l = ['temp_Px_',
     'temp_Py_',
     'temp_Nb_']
 
l2 = ['Px_2.dat',
     'Py_2.dat',
     'Nb.dat']

x = array([])
    
for N in range(1, (10**4)+1, 1):
    a = loadtxt(l[p] + str(N) + '.dat', unpack=True)
    x = append(x, a)
    del a
        
savetxt(l2[p], x)