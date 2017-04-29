# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

P = 10e3
L = 5
x = np.linspace(0,L)
k = 5*P/2 
m0 = 2*P
V1 = P/2*x + k 
M1 = P/4*x**2 + k*x + m0
V2 = -P/2*x - k
M2 = -P/4*x**2 - k*x - m0
V3 = -P/2*x + 2*k
M3 = -P/4*x**2 + 2*k*x + m0

fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

#~ plt.fill_between(x,V)
ax1.fill_between(x,V1, facecolor="#1E90FF")
ax4.fill_between(x,M1, color="#1E90FF")
ax2.fill_between(x,V2, color="#FF2A00")
ax5.fill_between(x,M2, color="#FF2A00")
ax3.fill_between(x,V3, color="#27E851")
ax6.fill_between(x,M3, color="#27E851")
#~ plt.fill_between(x,M)

for ax in (ax1,ax2,ax3): ax.set_ylim(-60e3,60e3),ax.axis('off')
for ax in (ax4,ax5,ax6): ax.set_ylim(-220e3,220e3),ax.axis('off')

plt.savefig("dshape_02.pdf", transparent=True)
plt.show()
