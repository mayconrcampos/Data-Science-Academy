import os

# Vamos criar e ler um arquivo totalmente pelo python.


# Criando arquivo.txt
os.system("touch arquivo.txt")

# listando diretório
os.system("ls")

#abrindo arquivo na memória
arq = open("arquivo.txt", "r")

# Lê o arquivo inteiro
print(arq.read())

# Contando o número de caracteres
print(arq.tell())

# retorna para o início do arquivo
print(arq.seek(0, 0))

# Lendo os primeiros 10 caracteres do arquivo
print(arq.read(10))

arq.seek(0, 0)
minhaString = arq.read(10)

for i in minhaString:
    print(i, end=" ")
