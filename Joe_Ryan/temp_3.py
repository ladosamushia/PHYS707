# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

from numpy.random import normal, standard_cauchy
from numpy import prod, pi, exp, sqrt, log, mean, linspace, array, histogram
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

g = []
g2 = []

def f(x, N, m, s):
    d = (2*pi*(s**2))**(N/2)
    num = exp((-1/2)*sum((1/(s**2))*(x - m)**2))
    return num/d   



Ia1 = []
Na1 = []
Ia2 = []
Na2 = []
Ia3 = []
Na3 = []
"""
for case in range(0, 3, 1):
    print(case)
    if case == 0:
        m2 = 1.2
        s2 = 1
    if case == 1:
        m2 = 1
        s2 = 2
    if case == 2:
        m2 = 1.2
        s2 = 2
        
    for N in range(1, 200, 1):
        if case == 0:
            Na1.append(N)
        if case == 1:
            Na2.append(N)
        if case == 2:
            Na3.append(N)
            
        for p in pr:
            x = normal(1, 1, N)
            g.append(log(f(x, N, m1, s1)/f(x, N, m2, s2)))
            g2.append(log(f(x, N, m2, s2)/f(x, N, m1, s1)))
    
        y, bins = histogram(g, 200, density=True)
        #y2, bins2 = histogram(g2, 250, density=True)
        bin_w = bins[1] - bins[0]
        #bin_w2 = bins2[1] - bins2[0]
        
        b = []
        for p in range(0, 199, 1):
            b.append(abs(bins[p]))
        qmin = b.index(min(b))
        
        if case == 0:
            Ia1.append(bin_w*(sum(y[0:qmin])))
        if case == 1:
            Ia2.append(bin_w*(sum(y[0:qmin])))
        if case == 2:
            Ia3.append(bin_w*(sum(y[0:qmin])))
    
plt.plot(Na1, Ia1, label='m2 = 1.2, s2 = 1')
plt.plot(Na2, Ia2, label='m2 = 1, s2 = 2')
plt.plot(Na3, Ia3, label='m2 = 1.2, s2 = 2')
plt.legend(loc = 'upper right')
plt.xlabel('N')
plt.ylabel('Contamination integral')
plt.savefig('Model_comparison.pdf')

'''
See the plot for the dependence on N. From the plot, we can see that 
it is easier to distinguish a unit offset in sigma (at fixed mean) than to 
distinguish a unit offset mean (at fixed sigma). This makes intuitive sense; 
one would expect narrower distributions to be easier to distinguish.
''' 


def C(x, m, s):
    A = ((x-m)/s)**2
    B = pi*s
    return prod(1/(B*(1 + A)))

g = []
g2 = []

Ia = []
Na = []

for N in range(1, 200, 1):
        Na.append(N)
        print(N)
        for p in pr:
            x = normal(1, 1, N)
            g.append(log(f(x, N, m1, s1)/C(x, m1, s1)))
    
        y, bins = histogram(g, 200, density=True)
        #y2, bins2 = histogram(g2, 200, density=True)
        bin_w = bins[1] - bins[0]
        #bin_w2 = bins2[1] - bins2[0]
        
        b = []
        for p in range(0, 199, 1):
            b.append(abs(bins[p]))
        qmin = b.index(min(b))
        
        Ia.append(bin_w*(sum(y[0:qmin])))
        
plt.plot(Na, Ia, label='Gaussian = True')
plt.legend(loc = 'upper right')
plt.xlabel('N')
plt.ylabel('Contamination integral')
plt.savefig('Model_comparison_2.pdf')
"""
def C(x, m, s):
    A = ((x-m)/s)**2
    B = pi*s
    return prod(1/(B*(1 + A)))

N = 10
n = 10**4
pr = range(0, n, 1)
m1 = 0.
s1 = 1.
"""
for p in pr:
    x = normal(m1, s1, N)
    g.append(log(f(x, N, m1, s1)/f(x, N, m2, s2)))
    x = normal(m2, s2, N)
    g2.append(log(f(x, N, m1, s1)/f(x, N, m2, s2)))
"""  

for p in pr:
    x = normal(m1, s1, N)
    if f(x, N, m1, s1) != 0:
        g.append(log(f(x, N, m1, s1)/C(x, m1, s1)))
    x = standard_cauchy(N)
    if f(x, N, m1, s1) != 0:
        g2.append(log((f(x, N, m1, s1)/C(x, m1, s1))))

y, bins, _ = plt.hist(g, 200, histtype=u'step', density=True)
y2, bins2, _ = plt.hist(g2, 200, histtype=u'step', density=True)
bin_w = bins[1] - bins[0]
#bin_w2 = bins2[1] - bins2[0]
plt.show()