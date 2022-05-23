import matplotlib.pyplot as plt
from numpy import *
from sympy import *

x = Symbol('X')

y = x**2

z = zeros(9)

xx = arange(-5,5,.1)

for i in range(-5,5):
    z[i]=y.subs(x,i)
print(z)
