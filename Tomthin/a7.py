# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:41:29 2019

@author: tomth
"""

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
data=np.loadtxt("Hz.txt")
def h_t(z,h0,O_m,O_l,wa,wo):
  h_t=h0*np.sqrt((O_m*(1+z)**3)+O_l*(1+z)**2+((1-O_l-O_m)*(1+z))**(3*(1+wo))*np.exp(-3*(z/1+z)*wa))
  return h_t
O_m=np.arange(0.1,.5,.01)
H_0=np.arange(50,100,2)
O_l=np.arange(-.1,.1,.02)
Wo=np.arange(-1.2,-0.8,.02)
Wa=np.arange(-1,1,.02)

print(O_m.size)
print(H_0.size)

Loglk=np.zeros((H_0.size,O_m.size,O_l.size,Wo.size,Wa.size))#5D loglikehood cube will be marginalized with with atleast 3 parameters so that we can do the contour plots
for i,h in tqdm(enumerate(H_0)):
  for j,om in enumerate(O_m):
      for k,ol in enumerate(O_l):
          for g,wo in enumerate(Wo):
              for f,wa in enumerate(Wa):
                  h_th=h_t(data[:,0],h,om,ol,wo,wa)
#                  print(i,j,k,g,f)
                  Loglk[i,j,k,g,f]=.5*sum(((data[:,1]-h_th)**2)/((data[:,2])**2))
print("Plotting contours for 2 parameter by marginalizing over 3 parameters-hence 10 possible contour plots")
marginalized_HO_Om_Ol=np.sum(Loglk,axis=(0,1,2))
marginalized_HO_Om_Ol=marginalized_HO_Om_Ol/-np.max(marginalized_HO_Om_Ol)
X0,Y0=np.meshgrid(Wa,Wo)
plt.figure(0)
plt.contourf(X0,Y0,marginalized_HO_Om_Ol)
plt.colorbar()
marginalized_HO_Om_Wo=np.sum(Loglk,axis=(0,1,3))
marginalized_HO_Om_Wo=marginalized_HO_Om_Wo/-np.max(marginalized_HO_Om_Wo)
X1,Y1=np.meshgrid(Wa,O_l)
plt.figure(1)
plt.contourf(X1,Y1,marginalized_HO_Om_Wo)
plt.colorbar()
marginalized_HO_Om_Wa=np.sum(Loglk,axis=(0,1,4))
marginalized_HO_Om_Wa=marginalized_HO_Om_Wa/-np.max(marginalized_HO_Om_Wa)
X2,Y2=np.meshgrid(Wo,O_l)
plt.figure(2)
plt.contourf(X2,Y2,marginalized_HO_Om_Wa)
plt.colorbar()
marginalized_HO_Ol_Wo=np.sum(Loglk,axis=(0,2,3))
marginalized_HO_Ol_Wo=marginalized_HO_Ol_Wo/-np.max(marginalized_HO_Ol_Wo)
X3,Y3=np.meshgrid(Wa,O_m)
plt.figure(3)
plt.contourf(X3,Y3,marginalized_HO_Ol_Wo)
plt.colorbar()
marginalized_HO_Ol_Wa=np.sum(Loglk,axis=(0,2,4))
marginalized_HO_Ol_Wa=marginalized_HO_Ol_Wa/-np.max(marginalized_HO_Ol_Wa)
X4,Y4=np.meshgrid(Wo,O_m)
plt.figure(4)
plt.contourf(X4,Y4,marginalized_HO_Ol_Wa)
plt.colorbar()
marginalized_HO_Wo_Wa=np.sum(Loglk,axis=(0,3,4))
marginalized_HO_Wo_Wa=marginalized_HO_Wo_Wa/-np.max(marginalized_HO_Wo_Wa)
X5,Y5=np.meshgrid(O_l,O_m)
plt.figure(5)
plt.contourf(X5,Y5,marginalized_HO_Wo_Wa)
plt.colorbar()
marginalized_Om_Ol_Wo=np.sum(Loglk,axis=(1,2,3))
marginalized_Om_Ol_Wo=marginalized_Om_Ol_Wo/-np.max(marginalized_Om_Ol_Wo)
X6,Y6=np.meshgrid(Wa,H_0)
plt.figure(6)
plt.contourf(X6,Y6,marginalized_Om_Ol_Wo)
plt.colorbar()
marginalized_Om_Wo_Wa=np.sum(Loglk,axis=(1,3,4))
marginalized_Om_Wo_Wa=marginalized_Om_Wo_Wa/-np.max(marginalized_Om_Wo_Wa)
X7,Y7=np.meshgrid(O_l,H_0)
plt.figure(7)
plt.contourf(X7,Y7,marginalized_Om_Wo_Wa)
plt.colorbar()
marginalized_Ol_Wo_Wa=np.sum(Loglk,axis=(2,3,4))
marginalized_Ol_Wo_Wa=marginalized_Ol_Wo_Wa/-np.max(marginalized_Ol_Wo_Wa)
X8,Y8=np.meshgrid(O_m,H_0)
plt.figure(8)
plt.contourf(X8,Y8,marginalized_Ol_Wo_Wa)
plt.colorbar()
marginalized_Om_Ol_Wa=np.sum(Loglk,axis=(1,2,4))
marginalized_Om_Ol_Wa=marginalized_Om_Ol_Wa/-np.max(marginalized_Om_Ol_Wa)
X9,Y9=np.meshgrid(Wo,H_0)
plt.figure(9)
plt.contourf(X9,Y9,marginalized_Om_Ol_Wa)
plt.colorbar()
