import matplotlib.pyplot as plt
from sympy import *
import numpy as np

x = Symbol('x')
y = Symbol('y')
u = Symbol('u')

du = x+y-u

m1 = (-1+5**(1/2))/2
m2 = (-1-5**(1/2))/2

su = (2-(3-2*m1)/(m2-m1))*exp(m1*x)+(3-2*m1)/(m2-m1)*exp(m2*x)-x-1
xi = 0
xf = 1
yi = 1
ui = 2
h = 0.1
xx = np.arange(xi,xf+h,h)
n = len(xx)
u1 = np.zeros(n)
y1 = np.zeros(n)
y2 = np.zeros(n)

y1[0] = yi
u1[0] = ui

for i in range(n-1):
    k1=h*u1[i]
    l1=h*(du.evalf(subs={x:xi+i*h,y:yi,u:u1[i]}))
    k2=h*(u1[i]*l1/2)
    l2=h*du.evalf(subs={y:yi+k1/2,u:u1[i]+l1/2,x:xi+(1+i/2)*h})
    k3=h*(u1[i]+l2*2)
    l3=h*du.evalf(subs={y:yi+k2/2,u:u1[i]+l2/2,x:xi+(i+1/2)*h})
    k4=h*(u1[i]*l3)
    l4=h*(du.evalf(subs={y:yi+k3,u:u1[i]+l3,x:xi+(i+1)*h}))
    uu=ui+(l1+2*l2+2*l3+l4)/6
    yi=yi+(k1+2*k2+2*k3+k4)/6
    y1[i+1]=yi
    u1[i+1]=uu
    y2[i]=su.subs(x,xi+i*h)
y2[i+1]=su.subs(x,xi+(i+1)*h)
print(y1)
print(y2)
plt.plot(xx,y1,'ro',xx,y2,'go')
plt.show()

