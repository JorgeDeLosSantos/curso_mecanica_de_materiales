# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

P = 50e3
L = 5
x = np.linspace(0,L/2)
V1 = P/2*np.ones_like(x)
M1 = P*x/2
V2 = -P/2*np.ones_like(x)
M2 = -P*x/2

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

#~ plt.fill_between(x,V)
ax1.fill_between(x,V1, color="#1E90FF")
ax3.fill_between(x,M1, color="#1E90FF")
ax2.fill_between(x,V2, color="#FF2A00")
ax4.fill_between(x,M2, color="#FF2A00")
#~ plt.fill_between(x,M)

plt.savefig("dshape_01.pdf", transparent=True)
plt.show()
