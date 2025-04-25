from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np

seed = 321659
N = 100000
def randi(a = 1029,b = 221591,c = 1048576):
	global seed
	a = 1029; b = 221591; c = 1048576
	seed = (seed*a + b)%c
	return float(seed)/c
	
def roleta():
  return int(37*randi())

def dado():  
  return int(6*randi()) + 1

def moeda():
  return 2*int(2*randi()) - 1

walk = 0
for t in range (1 , N ) :
  walk += moeda ()
  
#pesquisa de voto
p = 1
def binom ( p ) :
  x = 0
  if randi () < p :
    x = 1
  return x

count = 0
for t in range (1 , N ) :
  count += binom (p)
  
  
# plotando as probabilidades
def lancar_dados(N):
	'''
	Retorna um array com N lancamentos de dado
	'''
	lancamentos = []
	for i in range(N):
		lancamentos.append(dado())
	return np.array(lancamentos)
'''
a = lancar_dados(1000)
fig, ax = plt.subplots(figsize =(10, 7)) 
ax.hist(a, bins = [1,2,3,4,5,6,7]) 
plt.show()
'''

# algoritmo da caixa
caixad = []
caixae = []
tempo = []
box = [ -1]* N ; Nd = 0
for j in range (1 , t +1) :
  i = int ( N * random () )
  box [ i ] = - box [ i ]
  Nd += box [ i ]
  caixad.append(Nd)
  caixae.append(N-Nd)
  tempo.append(j)
  
plt.plot(tempo,caixad, label='Particulas na direita')
plt.plot(tempo,caixae, label='Particulas na esquerda')  
plt.legend()
plt.show()

