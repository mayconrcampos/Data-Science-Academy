# abrindo um dataset de uma única linha

f = open("salarios.csv", "r")

data = f.read()

rows = data.split("\n")


# adicionando linhas separadas

full_data = []
for i in rows:
    full_data.append(i.split(","))


arq = open("salarios.txt", "a")

for coluna in full_data:
    arq.writelines(coluna)
    arq.writelines("\n")
 

arq.close()



arq = open("salarios.txt", "r")

print(arq.read())

arq.close()



