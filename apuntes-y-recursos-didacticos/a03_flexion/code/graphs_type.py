# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10)
 
m = 0.5
b = 2

#~ y1 = -m*x + b
#~ y2 = -m*x - b
#~ y3 = m*x + b
#~ y4 = m*x - b
plt.plot(x,y1,x,y2,x,y3,x,y4)
plt.show()

