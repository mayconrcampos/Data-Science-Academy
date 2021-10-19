from modulo import soma
from random import randint

#soma = modulo.soma(5, 10)
#print(soma)

for i in range(0, 1000):
    n1 = randint(1, 150)
    n2 = randint(1, 150)
    print(f"{n1} + {n2} = ", end=" ")
    print(soma(n1, n2))
    print("\n")