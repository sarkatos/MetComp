# Modelo SIR probablistico (decaimento)
from random import *
from pylab import plot, xlabel, ylabel, show, scatter, legend, savefig
tf, dt, b, tau = input().split()
tf, dt, b, tau = (float(tf), float(dt), float(b), float(tau)) 

# mudar semente muda a historia da infeccao
seed(1243)
T = [];  S = [];  I = [];  R = []

Nstep = int(tf/dt)
s = 1000;  i = 1;  r = 0
s0 = s; s = s - i
for it in range(Nstep):
    for j in range(1,i+1):
        x = random(); y = random()
        if (y < s/s0 and x < b*dt):
            i += 1;  s -= 1
        x = random()
        if (x < dt/tau):
            i -= 1;  r += 1
   
    T.append(it*dt);  S.append(s);  I.append(i), R.append(r)

# sustetivel pelo tempo
#plot(T,S)

# infectados pelo tempo
plot(T,I)

# Removidos pelo tempo
#plot(T,R)
