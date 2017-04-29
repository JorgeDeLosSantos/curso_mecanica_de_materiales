from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

E, I = 29e6, 188
P, L = 5e3, 10
C1, C2, C3, C4 = (-7*P*L**2/128), 0, (-11*P*L**2/128), (P*L**3/384)
#~ x1 = np.linspace(0,L/4)
x1 = np.linspace(0,L)
y1 = (1/(E*I))*((1/8)*P*x1**3 + C1*x1 + C2)
#~ x2 = np.linspace(L/4,L)
x2 = x1
y2 = (1/(E*I))*((-1/24)*P*x2**3 + (1/8)*P*L*x2**2 + C3*x2 + C4)

ax.plot(x1, y1)
ax.plot(x2, y2)
ax.grid()
#~ ax.set_ylim(-40e-6, 1e-6)

plt.savefig("im.png")
plt.show()
