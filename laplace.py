import sympy as sp
import numpy as np
t=sp.Symbol('t',positive=True)
s=sp.Symbol('s',positive=True)
#dy=sp.cos(2*t)
dy=sp.exp(2*t**2)
ds=sp.laplace_transform(dy,t,s,noconds=True)
sp.pprint(ds)
y=sp.inverse_laplace_transform(ds,s,t,noconds=True)
y=sp.simplify(y)
sp.pprint(y)
