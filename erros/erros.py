from sympy import *
init_printing()
var('x,y')

f = Lambda(x, (x**3 - 3*x + 2)*exp(-x/4) - 1)
i = integrate(f(x), (x, -1, 1))

print(i)