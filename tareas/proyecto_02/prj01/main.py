# -*- coding: utf-8 -*-
"""
tau = Tc/J
phi = TL/JG
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def sifu(x,a,n):
    return np.piecewise(a, [a > x, a <= x], [0, lambda a:(x-a)**n])
    
E,I = 200e9, (2.53e6)/(1000**4)
#~ P = np.array([3e3,3e3])
#~ a = np.array([0.75,1.25])
P = np.array([10e3,5e3,8e3,20e3])
a = np.array([1,1.5,3,4])
MA = np.sum(P*a)
RA = np.sum(P)

xx = np.linspace(0,4,1000)
V,M,m,y = [],[],[],[]
for x in xx:
    V += [((RA)*x**0 - np.sum((P)*sifu(x,a,0)))]
    M += [(-(MA)*x**0 + (RA)*x**1 - np.sum((P)*sifu(x,a,1)))]
    m += [(1/(E*I))*(-(MA)*x + (RA/2)*x**2 - np.sum((P/2)*sifu(x,a,2)))]
    y += [(1/(E*I))*(-(MA/2)*x**2 + (RA/6)*x**3 - np.sum((P/6)*sifu(x,a,3)))]

#~ plt.axis('auto')
ax = plt.gca()
plt.fill_between(xx, V)
plt.fill_between(xx, M)
ax2 = ax.twinx()
ax2.plot(xx, y, "y--")
plt.show()
