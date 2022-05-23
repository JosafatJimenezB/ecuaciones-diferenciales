from scipy import linalg as al
import numpy as np

def suma1 (x,y):
    return x+y

def resta1(x,y):
    return x-y

def multi(x,y):
    return x*y


a = np.matrix([[2,3],[-5,4]])
a1 = np.matrix([[7,-1],[-3,5]])


print('resultado de la suma es: ')
print(suma1(a,a1))
print('resultado de la resta es: ')
print(resta1(a,a1))


b = al.inv(a)
print(b)

c = a + b
print(c)
