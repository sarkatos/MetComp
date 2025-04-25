# copiado de um youtube - outra forma de implemmentar AC
# Esta versão não tem condições periódicas de borda
import matplotlib.pyplot as plt
import numpy as np

# neibourhoods
inp = np.zeros([8,3])
for i in range(8):
    inp[i,:] = [int(x) for x in np.binary_repr(7-i,width=3)]
#print(inp)

# size
cols = 100
rows = int(cols/2) + 1

# c. i.
ac = np.zeros([rows, cols+2])
ac[0, int(cols/2)+1] = 1
#print(ac)

def AC(rule):
  out = [int(x) for x in np.binary_repr(rule,width=8)]
  for i in range(rows-1):
      for j in range(cols):
          for k in range(8):
              if np.array_equal(inp[k,:], ac[i, j:j+3]):
                ac[i+1,j+1] = out[k]

  plt.figure(rule)
# esta funcao do plt faz a magica da figura (pode ser usada no programa implementado por vcs)
  plt.imshow(ac[:, 1:cols+1], cmap='Greys', interpolation = 'nearest')
  plt.title("AC Rule"+str(rule))
  plt.show
  return

# roda todas as regras do range
for rule in range(20,40):
    AC(rule)

