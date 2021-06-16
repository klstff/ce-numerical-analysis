import math

def y(x):
    y = 5*(x**2) + 3
    return y

a = 5       # Limite inferior de integracao
b = 9       # Limite superior de integracao
h = (b-a)/2

x0 = a
x2 = b 
x1 = a+h

y0 = y(x0)
y1 = y(x1)
y2 = y(x2)

integral = (h/3)*(y0 + 4*y1 + y2)

print(integral)