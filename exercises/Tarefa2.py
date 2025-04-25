import numpy as np
import matplotlib.pyplot as plt
import time 
inicio = time.time()
# U_x= x**4-2*x**2

# E = U(x(t)) + 0.5* v**2 

# F = - gradiente da energia potêncial

# F = (-4*x**3) + 4*x

# a = F/m ; Como massa é 1kg -> a = F

# Definindo as contantes do problema
m = 1 # massa
tm = 10  # tempo da simulação
posicoes = [-1] #posição inicial
velocidades = [1] # velocidade inicial
tempos = [0] # tempo inicial
U0 = posicoes[0]**4-2*posicoes[0]**2
E0 = U0 + 0.5*(velocidades[0]**2)
erros_verlet = []
erros_RK2 = []
erros_RK4 = []
# intervalo de tempo [0,10]

def aceleracao(x):
  return (-4*x**3) + 4*x

def verlet(dt):
  # variáveis que resetam: 
  #----------------------------------------------------
  posicoes = [-1] #posição inicial
  velocidades = [1] # velocidade inicial
  tempos = [0] # tempo inicial
  energias = [E0]
  #----------------------------------------------------
  i = 0
  while tempos[-1] <= tm:
    # aceleração
    a = aceleracao(posicoes[i]) 
    # velocidade 
    v_next = velocidades[i] + a*dt/2
    # posição
    x_next = posicoes[i] + v_next*dt
    a = ((-4*x_next**3) + 4*x_next)
    v_next = v_next + a*dt/2
    U = x_next**4-2*x_next**2
    E = U + 0.5*(v_next**2)
    energias.append(E)
    velocidades.append(v_next)
    posicoes.append(x_next)
    tempos.append(tempos[i]+dt)
    i = i + 1
  return energias

def RK2(dt):
   # variáveis que resetam: 
  #----------------------------------------------------
  posicoes = [-1] #posição inicial
  velocidades = [1] # velocidade inicial
  tempos = [0] # tempo inicial
  energias = [E0]
  x = posicoes[0]
  v = velocidades[0]
  #----------------------------------------------------
  i = 0
  while tempos[-1] <= tm:
    tempos.append(tempos[i]+dt)
    xi = x + v*dt/2
    vi = v + aceleracao(x)*dt/2
    x = x + vi*dt
    v = v + aceleracao(xi)*dt
    U = x**4-2*x**2
    E = U + 0.5*(v**2)
    energias.append(E)
    i = i + 1
  return energias

def RK4(dt):
   # variáveis que resetam: 
  #----------------------------------------------------
  posicoes = [-1] #posição inicial
  velocidades = [1] # velocidade inicial
  tempos = [0] # tempo inicial
  energias = [E0]
  x = posicoes[0]
  v = velocidades[0]
  #----------------------------------------------------
  i = 0
  while tempos[-1] <= tm:
    tempos.append(tempos[i]+dt)
    a1 = aceleracao(x) ; v1 = v
    x2 = x + v1*dt/2
    v2 = v + a1*dt/2 ; a2 = aceleracao(x2)
    x3 = x + v2*dt/2
    v3 = v + a2*dt/2 ; a3 = aceleracao(x3)
    x4 = x + v3*dt
    v4 = v + a3*dt ; a4 = aceleracao(x4)
    x = x + (v1 + 2*v2 + 2*v3 + v4)*dt/6
    v = v + (a1 + 2*a2 + 2*a3 + a4)*dt/6
    U = x**4-2*x**2
    E = U + 0.5*(v**2)
    energias.append(E)
    i = i + 1
  return energias

def calcula_erro(lista):
  soma = 0
  for i in range(len(lista)):
    aux = (lista[i]-E0)**2
    soma = soma + aux
  erro = np.sqrt((soma)/len(lista))
  return erro

dt = 0.1
dts = []
for i in range(8):
  
  dts.append(dt)
  energias_verlet = verlet(dt)
  energias_RK2 = RK2(dt)
  energias_RK4 = RK4(dt)
  erros_verlet.append(calcula_erro(energias_verlet))
  erros_RK2.append(calcula_erro(energias_RK2))
  erros_RK4.append(calcula_erro(energias_RK4))
  dt = dt/2

# plot padrão
plt.plot(dts, erros_verlet,label='Verlet',color='blue', marker = 'o')
plt.plot(dts, erros_RK2,label='RK2',color='red', marker = '*')
plt.plot(dts, erros_RK4,label='RK4',color='green', marker = '^')
plt.xlabel("dt's")
plt.ylabel('Erro médio')
plt.legend()
plt.grid(True)
plt.show()

# plot semilog X
plt.semilogx(dts, erros_verlet,label='Verlet',color='blue', marker = 'o')
plt.semilogx(dts, erros_RK2,label='RK2',color='red', marker = '*')
plt.semilogx(dts, erros_RK4,label='RK4',color='green', marker = '^')
plt.xlabel("dt's")
plt.ylabel('Erro médio')
plt.legend()
plt.grid(True)
plt.show()

# plot semilog Y
plt.semilogy(dts, erros_verlet,label='Verlet',color='blue', marker = 'o')
plt.semilogy(dts, erros_RK2,label='RK2',color='red', marker = '*')
plt.semilogy(dts, erros_RK4,label='RK4',color='green', marker = '^')
plt.xlabel("dt's")
plt.ylabel('Erro médio')
plt.legend()
plt.grid(True)
plt.show()

meio = time.time()
print('tempo até aqui = ', meio-inicio)

erros_verlet = []
erros_RK2 = []
erros_RK4 = []

dt = 0.1
dts = []
for i in range(18):
  
  dts.append(dt)
  energias_verlet = verlet(dt)
  energias_RK2 = RK2(dt)
  energias_RK4 = RK4(dt)
  erros_verlet.append(calcula_erro(energias_verlet))
  erros_RK2.append(calcula_erro(energias_RK2))
  erros_RK4.append(calcula_erro(energias_RK4))
  dt = dt/2

# plot loglog
plt.loglog(dts, erros_verlet,label='Verlet',color='blue', marker = 'o')
plt.loglog(dts, erros_RK2,label='RK2',color='red', marker = '*')
plt.loglog(dts, erros_RK4,label='RK4',color='green', marker = '^')
plt.xlabel("dt's")
plt.ylabel('Erro médio')
plt.legend()
plt.grid(True)
plt.show()

fim = time.time()
print('tempo de execução = ', fim-inicio)