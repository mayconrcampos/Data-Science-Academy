lista = [2, 6, 9, 1, 20, 33, 66, 99]
lista1 = [9, 2, 11, 66, 99, 88, 77, 33]

print([numero[0] > numero[1] for numero in zip(lista, lista1)])


for indice, numero in enumerate(lista1):
    print(f"Indice: {indice} - Valor: {numero}")
