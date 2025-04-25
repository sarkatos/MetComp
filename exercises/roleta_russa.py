# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

seed = 321659
N = 100000
def randi(a = 1029,b = 221591,c = 1048576):
	global seed
	a = 1029; b = 221591; c = 1048576
	seed = (seed*a + b)%c
	return float(seed)/c
	
def roleta(n):
  return int(n*randi())
  
# versao do jogo onde a roleta reseta
N = 6
M = 10**4
j = 6*[0]
p = 6*[0]
for f in range(M):
  k = 0
  for i in range(M):
    bala = roleta(N)
    if k == bala:
      j[k] += 1
      break
    k += 1
    if k > 5:
      k = 0
for i in range(len(j)):
  p[i] = j[i]/M
print(j,'contador de eventos')
print(p,'probabilidade')
plt.bar([1,2,3,4,5,6],j)

# versao do jogo onde a roleta nao reseta
N = 6
M = 10**4
j = 6*[0]
p = 6*[0]
for f in range(M):
  k = 0
  bala = roleta(N)
  for i in range(M):
    if k == bala:
      j[k] += 1
      break
    k += 1
    if k > 5:
      k = 0
for i in range(len(j)):
  p[i] = j[i]/M
print(j,'contador de eventos')
print(p,'probabilidade') 
size = []
for i in range(6):
  size.append(i+1)
plt.bar(size,j)

