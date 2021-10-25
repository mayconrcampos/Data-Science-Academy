tp = 2, 3, 4

#for i in tp:
#    print(i, end=" -> ")



#lista = [1, 5, 6, 8, 7]
#for num in lista:
#    if num % 2 == 0:
#        print(num)


for i in range(1, 11):
    print(f"Tabuada de {i}")
    for n in range(1, 11):
        print(f"{i} x {n} = {i * n}")   



matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for linha in matriz:
    for coluna in linha:
        print(coluna, end="  ")
    print("\n")


dicio = {"nome" : "Maycon", "idade" : 39}

for chave, valor in dicio.items():
    print(chave, valor)