import numpy as np

print(np.__version__)



# Criando arrays
#print(help(np.array))

# Criar um array
vetor1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(vetor1)

print(type(vetor1))

# usando método de numpy que calcula soma acumulada
print(vetor1.cumsum())

print(vetor1.max()) # verificando maior valor do array

"""Utilizando funções Numpy"""

vetor2 = np.arange(0., 4.8, .8)

print(vetor2)





