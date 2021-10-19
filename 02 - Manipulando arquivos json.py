# Vamos ver como se manipula arquivos json


dicionario = {
    "nome" : "Guido Van Rossum",
    "Linguagem" : "Python",
    "similar" : [
        "c", 
        "Modula-3",
        "lisp"
    ],
    "users" : 1000000
}

for chave, valor in dicionario.items():
    print(f"Chave {chave} | Valor {valor}")


# importando módulo json

import json

# Convertendo dicionário para um objeto json
print(json.dumps(dicionario))


# criando um arquivo json
with open("dados.json", "w") as arquivo:
    arquivo.write(json.dumps(dicionario))

# Leitura de um arquivo json
with open("dados.json", "r") as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

for c, v in data.items():
    print(c, v)

print(data['nome'], data['Linguagem'])



