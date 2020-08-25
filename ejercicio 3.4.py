
# Laboratorio N° 3: Ejercicio 3.4
# Estabilidad de un sistema SDLIT
# Determinar si el sistema discreto Promedio Móvil es estable
# -----------------------------------------------------------
# Parámetros del sistema discreto Promedio Móvil
# Para M = 5, numera = [1 1 1 1 1] y denomina = [1];
from scipy import signal
import matplotlib.pyplot as plt
import math
import numpy as np
N=200
n = np.linspace(0,N-1,N)
#Cálculo del h[n] del Promedio Móvil
M=5
imp=signal.unit_impulse(N)
numera = np.ones(M)
denomi=1;
hn=signal.lfilter(numera,denomi,imp)/M

# Evaluacion si h[n] es acotada
suma = 0
for k in range(1,N):
    suma = suma + abs(hn[k])

# Gráfica de la respuesta impulsional
plt.plot(n,hn,'.')
plt.xlabel('Tiempo n');
plt.ylabel('Amplitud h[n]');
plt.title('Respuesta impulsional del sistema discreto Promedio Móvil')


# Cálculo del valor de S
S = sum(abs(hn))
print('Valor de S = ')
print(S)
print('--> sistema discreto estable')