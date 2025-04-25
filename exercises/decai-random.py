## Titulo

# problema de decaimento (ou de sobrevida) => dp = dt/tau
from random import *
from pylab import plot, xlabel, ylabel, show, scatter, legend, savefig

#@title Parametros de entrada
N_nucleos = 1000 #@param {type:"number"}
lam = 0.0174 #@param {type:"slider", min:0.0001, max:0.1, step:0.0001}
tf = 51 #@param {type:"slider", min:1, max:101, step:10}
dt= 1 #@param {type:"slider", min:0.01, max:1, step:0.01}

x = seed()
X = [];  Y = [];  Z = []

p = lam*dt;  Nstep = int(tf/dt)
Nt=N_nucleos
for it in range(Nstep):
    decay = 0
    for j in range(1,Nt+1):
        x = random()
        if (x < p):
            decay += 1
    Nt += -decay
    X.append(it*dt);  Y.append(Nt);  Z.append(decay)
plot(X,Y)
