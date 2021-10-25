import csv
from os import WIFCONTINUED, error


# Gerando arquivo CSV e escrevendo dentro dele
"""
with open("numeros.csv", "w") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(("primeira", "segunda", "terceira"))
    writer.writerow((22, 55, 66))
    writer.writerow((22, 11, 33))
"""

# Fazendo a leitura de arquivos CSV

with open("numeros.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(f"Número de colunas: {len(x)}")
        print(x)

# Gerando uma lista com dados do arquivo CSV

with open("numeros.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

for coisa in dados:
    for item in coisa:
        if item.isnumeric():
            print(item)
        else:
            print("Não é numérico e tals", item)