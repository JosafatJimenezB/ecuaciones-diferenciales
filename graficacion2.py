from scipy import linalg as al
import numpy as np

a = np.matrix([[2,3],[-5,4]])
print(a)

b = al.inv(a)
print(b)

c = a + b
print(c)
