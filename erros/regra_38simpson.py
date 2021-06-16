import math

def y(x):
    y = 1/x
    return y

a = 1       # Limite inferior de integracao
b = 7       # Limite superior de integracao
h = (b-a)/3

x0 = a
x3 = b 
x1 = a+h
x2 = x1+h

y0 = y(x0)
y1 = y(x1)
y2 = y(x2)
y3 = y(x3)

integral = (3*h/8)*(y0 + 3*y1 + 3*y2 + y3)

print(integral)