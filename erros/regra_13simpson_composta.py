import math

def y(x):
    y = 1 / (1 + x**2)
    return y

a = 0       # Limite inferior de integracao
b = 1       # Limite superior de integracao
h = 0.25    #(b-a)/m
m = (b-a)/h # Numero de subintervalos, tem que ser mult de 2
m = int(m)

soma = 0    # soma de c*y
veti = []   # Guarda i
vetx = []   # Pontos
vety = []   # Valores da funcao nos pontos xi
vetc = []   # Coeficientes
x = a

for i in range(0, m+1):
    if i == 0 or i == m:
        c = 1
    elif i%2 == 0:
        c = 2
    else:
        c = 4
    soma += c*y(x)
    vetx.append(x)
    vety.append(y(x))
    vetc.append(c)
    veti.append(i)
    x = x + h

integral = (h/3)*soma

print(integral)
print("i\t", veti,"\nx\t", vetx,"\ny\t", vety,"\nc\t", vetc)