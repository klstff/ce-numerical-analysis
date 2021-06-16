import math

def y(x):
    y = (x**3) * math.log(x)
    return y

a = 1   # Limite inferior de integracao
b = 3   # Limite superior de integracao
m = 4   # Numero de subintervalos
h = (b-a)/m

soma = 0    # soma de c*y
veti = []   # Guarda i
vetx = []   # Pontos
vety = []   # Valores da funcao nos pontos xi
vetc = []   # Coeficientes
x = a

for i in range(0, m+1):
    if i == 0 or i == m:
        c = 1
    else:
        c = 2
    soma += c*y(x)
    vetx.append(x)
    vety.append(y(x))
    vetc.append(c)
    veti.append(i)
    x = x + h

integral = (h/2)*soma

print(integral)
print("i\t", veti,"\nx\t", vetx,"\ny\t", vety,"\nc\t", vetc)