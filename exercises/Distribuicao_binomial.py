from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np

seed = 321659
N = 100
def randi(a = 1029,b = 221591,c = 1048576):
	global seed
	a = 1029; b = 221591; c = 1048576
	seed = (seed*a + b)%c
	return float(seed)/c
	
def binom ( p ) :
  x = 0
  if randi () < p :
    x = 1
  return x
p = 1
count = 0
for t in range (1 , N ) :
  count += binom (p)
  
def moeda():
  return int(2*randi()) 
    
hist = (N)*[0]
print(hist,'esse aqui')
M = 1000
for i in range(M):
	s = 0
	for j in range(N):
		s += moeda()
	hist[s] += 1
print(len(hist))
print(hist)
print(np.sum(np.array(hist)))
plt.plot(hist)
plt.show()
