# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import loadtxt, mean, std
from numpy.random import normal, poisson, binomial, uniform
import matplotlib.pyplot as plt

"""
Gaussian
"""
a = loadtxt('Joseph_Gauss.dat', unpack=True)
mu = mean(a)
sig = std(a, ddof=1)

mu_sym = []
sig_sym = []

N = 4
for q in range(0, 10**N, 1):
    x = normal(mu, sig, len(a))
    mu_sym.append(mean(x))
    sig_sym.append(std(x, ddof=1))
    
print('Gaussian estimated average = ', mu, '+/-', std(mu_sym, ddof=1))
print('Gaussian estimated standard deviation = ', sig, '+/-', std(sig_sym, ddof=1))

"""
Poisson
"""
a = loadtxt('Joseph_Poisson.dat', unpack=True)
l = mean(a) ##Average rate $\lambda$

l_sym = []

N = 4
for q in range(0, 10**N, 1):
    x = poisson(l, len(a))
    l_sym.append(mean(x))
    
print('Poisson estimated rate = ', l, '+/-', std(l_sym, ddof=1))

"""
Binomial
"""
a = loadtxt('Joseph_binomial.dat', unpack=True)
n = len(a)
p = mean(a)

p_sym = []

N = 4
for q in range(0, 10**N, 1):
    x = binomial(n, p)
    p_sym.append(x/n)
    
print('Binomial estimated probability = ', p, '+/-', std(p_sym, ddof=1))

"""
Uniform
"""
a = loadtxt('Joseph_Uniform.dat', unpack=True)
m = max(a)
k = len(a)
N = m + (m/k) - 1

N_sym = []

n = 4
for q in range(0, 10**n, 1):
    x = uniform(0, N, k)
    m = max(x)
    N_sym.append(m + (m/k) - 1)
    
print('Uniform estimated maximum = ', N, '+/-', std(N_sym, ddof=1))




