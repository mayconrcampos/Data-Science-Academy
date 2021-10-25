import os

# Gravando arquivos

os.system("touch arquivo2.txt")

# Abrindo arquivo no modo append
arquivo = open("arquivo2.txt", "a")

frase = input("Digite uma bela frase que irá ser grava dentro do arquivo2.txt: ")

# escrevendo dentro do arquivo
arquivo.write(frase)

# precisamos fechar o arquivo para depois abrir de novo no modo readable.
arquivo.close()

# Abrindo em modo leitura
arquivo = open("arquivo2.txt", "r")

# agora vamos ler este arquivo
print(arquivo.read())




