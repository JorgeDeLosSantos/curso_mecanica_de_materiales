# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

P = 50e3
L = 5
x1 = np.linspace(0,L/2)
x2 = np.linspace(L/2,L)
V1 = P/2*np.ones_like(x1)
V2 = -P/2*np.ones_like(x2)
M1 = P*x1/2
M2 = -P*x2/2 + P*L/2

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

#~ plt.fill_between(x,V)
ax1.fill_between(x1,V1, color="#1E90FF")
ax1.fill_between(x2,V2, color="#1E90FF")
ax2.fill_between(x1,M1, color="#1E90FF")
ax2.fill_between(x2,M2, color="#1E90FF")
#~ plt.fill_between(x,M)


for ax in (ax1,ax2):
    ax.axhline(0, color="k")
    ax.axvline(0, color="k")
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_visible(False)
    ax.grid(ls=":")
    #~ ax.yaxis.set_visible(False)


plt.savefig("shear_moment_02.pdf", transparent=True)
plt.show()
