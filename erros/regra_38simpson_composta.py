import math

def y(x):
    y = math.log(x**3 + math.sqrt(math.e**x + 1))
    return y

a = 1       # Limite inferior de integracao
b = 4       # Limite superior de integracao
m = 6       # Numero de subintervalos, tem que ser mult de 3
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
    elif i%3 == 0:
        c = 2
    else:
        c = 3
    soma += c*y(x)
    vetx.append(x)
    vety.append(y(x))
    vetc.append(c)
    veti.append(i)
    x = x + h

integral = (3*h/8)*soma

print(integral)
print("i\t", veti,"\nx\t", vetx,"\ny\t", vety,"\nc\t", vetc)