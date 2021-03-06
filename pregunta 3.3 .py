import numpy as np

N=100
nn= np.linspace(0,N-1,N)
xn1=np.sin(2*math.pi*0.9*nn)
xn2=np.sin(2*math.pi*0.3*nn)

alfa1=0.5
alfa2=0.5

M=8
num = np.ones(M)
yn1=signal.lfilter(num,1,alfa1*xn1)/M
yn2=signal.lfilter(num,1,alfa2*xn2)/M
xn3 = alfa1*xn1+alfa2*xn2
yn3=signal.lfilter(num,1,xn3)/M

plt.subplot(2,1,1)
plt.plot(nn,yn3,'.')
plt.xlabel('Time [n]')
plt.ylabel('Señal Filtrada')

plt.subplot(2,1,2)
yn3s = yn1 + yn2
plt.plot(nn,yn3s,'.r')
plt.xlabel('Time [n]')
plt.ylabel('Señal Filtrada')