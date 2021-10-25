texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, Big Data."

print(texto)

import os
arquivo = open("08arquivo.txt", "w")

for palavra in texto.split():
    arquivo.write(palavra+" ")

arquivo.close()


arquivo = open("08arquivo.txt", "r")

print(arquivo.read())

arquivo.close()