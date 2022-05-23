import matplotlib.pyplot as plt
from sympy import *
import numpy as np
x = Symbol('X')

y = exp(x)

xmin = -5
xmax = 5
h = 1
xx = np.arange(xmin,xmax,h)
n = len(xx)

z = np.zeros(n)

for i in range(n):
    z[i]=y.subs(x,xx[i])
print(z)

plt.plot(xx,z,'r*')
plt.show()