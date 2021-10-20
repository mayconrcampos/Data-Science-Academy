from functools import reduce

lista = [12, 45, 26, 33, 88]


def soma(x, y):
    return x + y


print(reduce(soma, lista))


print(reduce(lambda x, y: x * y, lista))

