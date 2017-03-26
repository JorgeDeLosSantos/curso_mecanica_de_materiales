# -*- coding: utf-8 -*-
"""
tau = Tc/J
phi = TL/JG
"""
import numpy as np

ID = np.array([0,0,0.04])
OD = np.array([0.036,0.06,0.06])
G = np.array([27e9,39e9,39e9])
T = np.array([800,1600,0])
L = np.array([0.4,0.375,0.25])
J = np.pi/2*((OD/2)**4-(ID/2)**4)

TS = []
for k in range(len(T)):
    _ts = sum(T[0:k+1])
    TS.append(_ts)

TS = np.array(TS)
phi = (TS*L)/(J*G)
tau = (TS*OD)/J

print tau
print sum(phi)*(180/np.pi)


