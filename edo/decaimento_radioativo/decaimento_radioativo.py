from math import exp,log
import numpy as np
from matplotlib import pyplot as plt

# Valores iniciais
t_mv = 87                       # Tempo de meia-vida do isotopo
y0 = 0.002                      # Atividade inicial

a = 0                           # Dia inicial
b = 60                          # Dia final
m = 20                          # Numero de subintervalos
h = (b-a)/m                     # Passo
x = np.linspace(a, b, m)

def funcao(x, y):
    k = -log(1/2)/t_mv
    f = -y0*k*exp(-k*x)         # Derivada da funcao de decaimento radioativo
    return f
    
# Metodo de Euler
def euler():
    y = np.zeros([m])
    y[0] = y0
    for i in range(0, m-1):
        y[i+1] = y[i] + h*funcao(x[i], y[i])
    return y

# Metodo de Euler Modificado
def euler_modificado():
    y = np.zeros([m])
    y[0] = y0
    for i in range(0, m-1):
        f = funcao(x[i], y[i])
        y[i+1] = y[i] + h*funcao(x[i] + 0.5*h, y[i] + 0.5*h*f)
    return y

# Metodo de Euler Melhorado
def euler_melhorado():
    y = np.zeros([m])
    y[0] = y0
    for i in range(0, m-1):
        f = funcao(x[i], y[i])
        ff = funcao(x[i] + h, y[i] + h*f)
        y[i+1] = y[i] + 0.5*h*(f + ff)
    return y

# Metodo de Runge-Kutta de 4a ordem
def runge_kutta():
    y = np.zeros([m])
    y[0] = y0
    for i in range(0, m-1):
        k1 = funcao(x[i], y[i])
        k2 = funcao(x[i] + 0.5*h, y[i] + 0.5*h*k1)
        k3 = funcao(x[i] + 0.5*h, y[i] + 0.5*h*k2)
        k4 = funcao(x[i] + h, y[i] + h*k3)
        y[i+1] = y[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    return y

# Solucao analitica
def analitica():
    y = np.zeros([m])
    for i in range(0, m):
        k = -log(1/2)/t_mv
        y[i] = y0*exp(-k*x[i])
    return y

y_e = euler()
y_emod = euler_modificado()
y_emel = euler_melhorado()
y_rk = runge_kutta()
y_a = analitica()

# Tabela de resultados
print("Decaimento Radioativo\nx\t Euler\t\t Euler Mod\t Euler Mel\t Runge-Kutta\t Analitica")
for i in range(m):
	print(format(x[i],'.1f'),"\t",format(y_e[i],'.7f'),"\t",format(y_emod[i],'.7f'),"\t",format(y_emel[i],'.7f'),"\t",format(y_rk[i],'.7f'),"\t",format(y_a[i],'.7f'))

# Plot das curvas
plt.plot(x, y_e, label="Euler")
plt.plot(x, y_emod, label="Euler Modificado")
plt.plot(x, y_emel, label="Euler Melhorado")
plt.plot(x, y_rk, label="Runge Kutta")
plt.plot(x, y_a, label="Analitica")
plt.title("Decaimento Radioativo")
plt.xlabel("Tempo (dias)")
plt.ylabel("Atividade da fonte (Ci)")
plt.legend()
plt.show()