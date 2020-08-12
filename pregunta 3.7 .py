from scipy import signal
import matplotlib.pyplot as plt
import math
import numpy as np

n = np.linspace(0,40,41)
k=3
xn = np.cos(2*math.pi*0.0625*n)+np.cos(2*math.pi*0.625*n)

M=4

xnk= np.concatenate((np.zeros(k),xn))
xnk.shape

num = (M, 1)
den=1

yn = signal.lfilter(num,den,xn);
ynk = signal.lfilter(num,den,xnk);
difn = yn - ynk[k:41+k]

plt.subplot(3,1,1)
plt.plot(n,yn,'.')
plt.xlabel('Time [n]')
plt.ylabel('Señal Filtrada')

plt.subplot(3,1,2)
plt.plot(n,ynk[1:42],'.')
plt.xlabel('Time [n]')
plt.ylabel('Señal Filtrada')

plt.subplot(3,1,3)
plt.plot(n,difn,'.')
plt.xlabel('Time [n]')
plt.ylabel('Señal Filtrada')