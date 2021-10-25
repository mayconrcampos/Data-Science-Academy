# Automatizando o processo de gravação

# usuario digita nome do arquivo
nomeArquivo = input("Qual nome do arquivo? ")

# nomeArquivo recebe concatenaçao de string pra acrescentar o formato do arquivo.
nomeArquivo = nomeArquivo + ".txt"

# arquivo é aberto em modo escrita
arquivo = open(nomeArquivo, "w")

# usuario digita o texto que irá ser gravado dentro do arquivo
texto = input("Digite o texto a ser gravado em seu arquivo: ")

# python grava o texto dentro do arquivo
arquivo.write(texto)

#python fecha arquivo
arquivo.close()

# python abre arquivo, mas em modo leitura
arquivo = open(nomeArquivo, "r")

# print do texto 
print(arquivo.read())

# fechamento do arquivo.
arquivo.close()