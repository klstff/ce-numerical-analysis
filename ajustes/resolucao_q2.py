import numpy as np
import math

def resolve_sistema_3x3(matriz):
    tamanho = len(matriz)

    for i in range(0, tamanho): 
        for j in range(i, tamanho):
            matriz[j,:] = matriz[j,:] / matriz[j, j]
        for j in range(i+1, tamanho):
            matriz[j,:] = -matriz[i,:] * matriz[j, i] + matriz[j,:]
   
    for i in range(1, tamanho):
        for j in range(1, tamanho):
            matriz[tamanho-i-j,:] = matriz[tamanho-i-j,:] - matriz[tamanho-i,:] * matriz[tamanho-i-j, tamanho-i]
    
    coeficientes = matriz[:, tamanho]
    return coeficientes


def ajuste_polinomial(R, I, n):
    somax = somax2 = somax3 = somax4 = somay = somaxy = somax2y = 0
    for i in range(0, n):
        somax += R[i]
        somax2 += R[i]**2
        somax3 += R[i]**3
        somax4 += R[i]**4
        somay += I[i]
        somaxy += R[i]*I[i]
        somax2y += (R[i]**2)*I[i]

    matriz = np.matrix([[n,      somax,  somax2,  somay],
                        [somax,  somax2, somax3,  somaxy],
                        [somax2, somax3, somax4,  somax2y]], dtype=float)

    coeficientes = resolve_sistema_3x3(matriz)
    b0 = float(coeficientes[0])
    b1 = float(coeficientes[1])
    b2 = float(coeficientes[2])

    print("\nEquacao Polinomial:\ny = {:.1f} + {:.1f}x + {:.1f}x^2".format(b0, b1, b2))


def ajuste_logaritmico(R, I, n):
    for i in range(0, n):
        if R[i] > 0:
            R[i] = math.log(R[i])

    a, b = calcula_coeficientes(R, I, n)

    print("\nEquacao Logaritmica:\ny = {:.1f}ln(x) + {:.1f}".format(a, b))


def ajuste_exponencial(R, I, n):
    for i in range(0, n):
        if I[i] > 0:
            I[i] = math.log(I[i])

    a, b = calcula_coeficientes(R, I, n)
    b = math.exp(b)

    print("\nEquacao Exponencial:\ny = {:.1f}e^{:.1f}x".format(b, a))


def ajuste_potencial(R, I, n):
    for i in range(0, n):
        if R[i] > 0 and I[i] > 0:
            R[i] = math.log(R[i])
            I[i] = math.log(I[i])

    a, b = calcula_coeficientes(R, I, n)
    b = math.exp(b)

    print("\nEquacao Potencial:\ny = {:.1f}x^{:.1f}".format(b, a))


def calcula_coeficientes(R, I, n):
    somax = somax2 = somay = somaxy = 0
    n = len(R)
    for i in range(0, n):
        somax += R[i]
        somax2 += R[i]**2
        somay += I[i]
        somaxy += R[i]*I[i]

    a = (n * somaxy - somax * somay) / (n * somax2 - somax**2)
    b = (somax * somaxy - somay * somax2) / (somax**2 - n * somax2)

    return a, b


R = [1, 1.1, 1.25, 1.5, 2, 2.2, 3.5, 5, 6, 6.5, 7, 8, 8.75, 9.5, 10]
I = [10, 9, 8.9, 7, 6, 5.5, 4, 2, 1.5, 1.1, 1.05, 1, 1, 1.1, 0.95]
n = len(R)

ajuste_polinomial(R, I, n)
ajuste_logaritmico(R, I, n)
ajuste_exponencial(R, I, n)
ajuste_potencial(R, I, n)
print("\nOs graficos mostram que o ajuste logaritmico e o que melhor se adapta aos pontos.")