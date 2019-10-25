# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:59:58 2019

@author: wangjam
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
N=20#Number of measurements 
# sampling from each of the distribution are independent from each other
mu_true, sigma_true = 1, 1 # mean and standard deviation true distribution
mu_m1, sigma_m1 = 1, 1 #model 1(M1)
mu_m2, sigma_m2 = 1.2, 1 #model 2(M2)
mu_m3, sigma_m3 = 1, 2 #model 3(M3)
mu_m4, sigma_m4 = 1.2, 2 #model 4(M4)
#I will be using the posterior ratios to test which of the model is the best give {xk} data samples following the idea from section 2.3 and 3.3 of  skiling and sivia
# let say comparing which model is better model1 or model2 given {xk} willbe given by posterior ratios of model 1 and model2 eqn 4.1
#i.e. [pdf(Model1|{xk})]/[pdf(Model2|{xk})]= [pdf({xk}|Model1)*pdf(Model1)]/[pdf({xk}|Model2)*pdf(Model2)]
#(check eqn--->4.16 for mu and sigma are free paramters) for this question we have fixed sigma and mu which will mean the marginalization of the pdf's for the free paramters will be done with the dirac delta function
#pdf(Model) with given parameter mu and sigma will just make dirac_delta(mu-mu1) and dirac_delta(sigma-sigma_1) say for model 1, hence only replacing the mu and sigma with the current model's
# with the mean and standard deviation of gaussian Models given we can straigth forwardlt follow eqn 2.23 

# 6 posterior pdf ratios : M1/M2,M1/M2,M1/M3,M1/M4,M2/M3,M2/M4 AND M3/M4 
#SO IF THE posterior RATIO IS BIGGER THAN ONE=> THE MODEL ON THE NUMERATOR IS BETTER FOR THE GIVEN DATA AND VICE-VARSA FOR DENOMINATOR (SECTION-4.1)
r12=[]
r13=[]
r14=[]
r23=[]
r24=[]
r34=[]
#appended for each size of N, to see with increasing data how does the ratio change?Giving notion of bayesian analysis
for i in range(1,N):
    xk = np.random.normal(mu_true, sigma_true, i)#data generated 
    s1=0
    s2=0
    s3=0
    s4=0
    for j,jl in enumerate(xk):
        s1+=((jl-mu_m1)**2/(2*sigma_m1**2))
        s2+=((jl-mu_m2)**2/(2*sigma_m2**2))
        s3+=((jl-mu_m3)**2/(2*sigma_m3**2))
        s4+=((jl-mu_m4)**2/(2*sigma_m4**2))
    r12.append((((sigma_m2)**i)*np.exp(-(s1/(2*sigma_m1**2))))/(((sigma_m1)**i)*np.exp(-(s2/(2*sigma_m2**2)))))
    r13.append((((sigma_m3)**i)*np.exp(-(s1/(2*sigma_m1**2))))/(((sigma_m1)**i)*np.exp(-(s3/(2*sigma_m3**2)))))
    r14.append((((sigma_m4)**i)*np.exp(-(s1/(2*sigma_m1**2))))/(((sigma_m1)**i)*np.exp(-(s4/(2*sigma_m4**2)))))
    r23.append((((sigma_m3)**i)*np.exp(-(s2/(2*sigma_m2**2))))/(((sigma_m2)**i)*np.exp(-(s3/(2*sigma_m3**2)))))
    r24.append((((sigma_m4)**i)*np.exp(-(s2/(2*sigma_m2**2))))/(((sigma_m2)**i)*np.exp(-(s4/(2*sigma_m4**2)))))
    r34.append((((sigma_m4)**i)*np.exp(-(s3/(2*sigma_m3**2))))/(((sigma_m3)**i)*np.exp(-(s4/(2*sigma_m4**2)))))

plt.figure(0)
plt.plot(np.arange(1,N),(np.asarray(r12)))
plt.title("X:Increasing number data samples Vs Y: ratio M1/M2")
plt.figure(1)
plt.plot(np.arange(1,N),np.log(np.asarray(r13)))
plt.title("X:Increasing number data samples Vs Y: ratio M1/M3")
plt.figure(2)
plt.plot(np.arange(1,N),np.log(np.asarray(r14)))
plt.title("X:Increasing number data samples Vs Y: ratio M1/M4")
plt.figure(3)
plt.plot(np.arange(1,N),np.log(np.asarray(r23)))
plt.title("X:Increasing number data samples Vs Y: ratio M2/M3")
plt.figure(4)
plt.plot(np.arange(1,N),np.log(np.asarray(r24)))
plt.title("X:Increasing number data samples Vs Y: ratio M2/M4")
plt.figure(5)
plt.plot(np.arange(1,N),(np.asarray(r34)))
plt.title("X:Increasing number data samples Vs Y: ratio M3/M4")
# from the previous plot it's obvious that unit offset in mean is much easier to distinguish than unit offset in sigma.
#####################################################################################################
#for unspecified mean and sigma we have to marginalized for mean and sigma meaning double integral over mean and sigma over 
#the reqd. range to give a sense of confidence.
# making a mesh grid of sigma and mean and and get the Posterioir pdf for each sigma's amd mu's in the range. Similarly for cauchy but on median and width grid
#Comparsion will be done for the range of {sigma,mu} and {width, median}, basically selecting as rectangle to do summation over the calculated 2D posterior pdf
#prior pdf is considered to be constant hence 1/(mu_max-mu_min)*1/(sigma_max-sigma_min)
N_sample=50
xk2 = np.random.normal(mu_true, sigma_true, N_sample)
sigma2=np.linspace(0.1,2,50)
mu2=np.linspace(0.0,2,50)
median2=np.linspace(0.1,2,50)
width2=np.linspace(0.1,2,50)
sig_mesh,mu_mesh=np.meshgrid(sigma2,mu2)#don't need this
width_mesh,median_mesh=np.meshgrid(width2,median2)#don't need this
Gauss=np.zeros(sig_mesh.shape)
Cauchy=np.zeros(width_mesh.shape)
##
for i,il in enumerate(mu2):
    for j,jl in enumerate(sigma2):
        s11=0
        for t,tl in enumerate(xk2):
            s11+=((tl-il)**2/(2*jl**2))
        Gauss[i,j]=(np.exp(-(s11/(2*jl**2))))/(((jl)**N_sample))#posterior for the gaussian with unspecified mu and sigma

for i,il in enumerate(median2):
    for j,jl in enumerate(width2):
        pdf=1
        for t,tl in enumerate(xk2):
            pdf_deno=(1+((tl-il)/(jl))**2)
            pdf*=(1/(np.pi*jl))*pdf_deno
        Cauchy[i,j]=pdf

gauss_post=simps([simps(Gauss[:,j], sigma2) for j,jl in enumerate(sigma2)], mu2)
cauchy_post=simps([simps(Cauchy[:,j], width2) for j,jl in enumerate(width2)], median2)
print("ratio_of_gauss_cauchy",gauss_post/cauchy_post)