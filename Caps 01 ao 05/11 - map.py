"""
Algumas funções orientadas à expressão, em Python:

- map (função, sequência)
- reduce (Função, sequencia)
- filter (função, sequencia)
- lambda
- list comprehension
"""

# map recebe dois argumentos, uma função e uma sequencia

# o primeiro argumento é uma função, o segundo uma lista.


def fahrenheit(temp):
    return ((float(9) / 5) * temp + 32)


def celsius(temp):
    return (float(5) / 9) * (temp - 32)

temperaturas = [0, 35, 41, 19, 25, 80, 100]

# utilizando map para aplicar uma função a cada temperatura da lista
convertidasF = list(map(fahrenheit, temperaturas))

print(convertidasF)

convertidasC = list(map(celsius, convertidasF))

print(convertidasC)


# utilizando lambda

listacomLambda = list(map(lambda x: (float(5) / 9) * (x - 32), temperaturas))

print(listacomLambda)

# somando elementos entre listas

lista1 = [2, 5, 87, 54, 3]
lista2 = [5, 9, 11, 6, 66]

soma = list(map(lambda x, y: x + y, lista1, lista2))

print(soma)