#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:50:46 2020

@author: willeala
"""

#Paketit

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#Alustetaan taulukot

f = np.zeros(17)
A = np.zeros(17)

#Virhepalkit

ferror = 1
Aerror = 0.01

#Luetaan tiedosto kahteen taulukkoon

file = open('RLCdata.txt', 'r')

for i in range(17):
    rivi = file.readline()
    osat = rivi.split()
    f[i] = (osat[0])        #taajuudet
    A[i] = (osat[1])        #amplitudit
file.close()

#print(f)
#print(A)


#Tehtävänannon arvot

V = 4
R = 240
C = 6.8*10**(-6)

#Sovitus pienimmän neliösumman menetelmällä

def func(param, f, A):
    return A - 1000*(2*np.pi*V*f)/(np.sqrt((param[0]*4*np.pi**2*f**2 - 1/C)**2 + R**2*4*np.pi**2*f**2))

f0 = np.array([0, 0])
Afit = leastsq(func, f0, args=(f, A))[0]

fsovitus = np.linspace(0, 600, 1000)
Asovitus = 1000*(2*np.pi*V*fsovitus)/(np.sqrt((Afit[0]*4*np.pi**2*fsovitus**2 - 1/C)**2 + R**2*4*np.pi**2*fsovitus**2))
    
#print(Afit[0])

#Plotataan

plt.style.use('ggplot')
plt.xticks(np.arange(0, 600, 50))

plt.title('Virran amplitudi vaihtojännitteen taajuuden funktiona')
plt.xlabel('Taajuus (Hz)')
plt.ylabel('Amplitudi (mA)')
plt.errorbar(f, A, Aerror, ferror, 'k.-', label='Data')
plt.plot(fsovitus, Asovitus, label='Sovitus')
plt.legend()
plt.savefig('Amplitudi.png')

plt.show()