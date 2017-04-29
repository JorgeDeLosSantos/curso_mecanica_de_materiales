# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def _singu(x,a,n):
    if x>a:
        return (x-a)**n
    else:
        return 0
        
def singu(x,a,n):
    return np.array([_singu(s,a,n) for s in x])
        
x = np.linspace(0,10,100)
y1 = 4*singu(x,3,2)
y2 = 2*singu(x,6,3)

plt.plot(x, y1, label="$<x-a>^2$")
#~ plt.plot(x, y2)
plt.grid(ls=":")
plt.legend()
plt.show()
