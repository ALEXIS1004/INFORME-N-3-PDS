
# Laboratorio N° 3: Problema 3.9
# Estabilidad de un sistema SDLIT
# Determinar si el sistema descrito es estable o no
# -----------------------------------------------------------

from scipy import signal
import matplotlib.pyplot as plt
import math
import numpy as np
N=200
n = np.linspace(0,N-1,N)
#Cálculo del h[n] del Promedio Móvil
#Variamos M para determinar si es estable
M=10
imp=signal.unit_impulse(N)

#DEFINIMOS numera para y[n]=x[4-n]
numera = np.concatenate((np.zeros(4),np.ones(1),np.zeros(N-5)))
denomi=1;
hn=signal.lfilter(numera,denomi,imp)/M

# Gráfica de la respuesta impulsional
plt.subplot(2,1,1)
plt.plot(n,hn,'.')
plt.xlabel('Time [n]')
plt.ylabel('Señal Filtrada M=10')

#DEFINIMOS numera para y[n] = 1/4y[n - 1] + x[n], n ≥ 0, y[-1] = 0
numera = np.ones(1)
denomi=np.array([1, -1/4])
hn=signal.lfilter(numera,denomi,imp)/M

plt.subplot(2,1,2)
plt.plot(n,hn,'.')
plt.xlabel('Time [n]')
plt.ylabel('Señal Filtrada M=12')

# Cálculo del valor de S
S = sum(abs(hn))
print('Valor de S = ')
print(S)
print('--> sistema discreto estable')