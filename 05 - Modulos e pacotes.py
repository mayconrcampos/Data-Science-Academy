import math
from random import randint
# verificando todos os mẽtodos disponiveis no modulo math
dir(math)

# usando um dos métodos

print(math.sqrt(5))

print(math.pow(3, 2))

print(math.pow(randint(1, 20), 2))


import statistics

lista = [3, 45, 6.6, 50, 15.5, 99, 15.9]

print(statistics.mean(lista))
print(statistics.median(lista))
print(statistics.pvariance(lista))


import os

os.getcwd()

print(dir(os))
#print(os.system("neofetch"))

import sys

sys.stdout.write("Olar!")
print(sys.version)


import urllib.request

resposta = urllib.request.urlopen("https://www.google.com")
print(dir(resposta))