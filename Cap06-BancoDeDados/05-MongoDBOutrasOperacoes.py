from datetime import datetime
from pymongo import MongoClient

# Criando conexão com DB
conn = MongoClient()

# Listando DBs disponíveis
print("Listando DataBases: ", conn.list_database_names())

# Definindo o objeto db escolhendo cadastrodb

db = conn.cadastrodb

# Listando as coleções disponíveis
print("Listando Tabelas (Collections da Database escolhida): ", db.list_collection_names())

# Criando uma collection (tabela)
'''db.create_collection("nomes")'''

# listando coleções disponíveis
print("Listando novamente Collections da Database escolhida: ", db.list_collection_names())

# inserindo um documento na coleção criada
doc1 = {
    "nomes":["Maycon", "Ariana", "Otávio", "Benjamin"]
}

'''db.nomes.insert_one(doc1)'''


doc2 = {
    "nomes":[
        "Chico",
        "Giovani Foguetinho",
        "Bruninho Homem Bomba",
        "Davi",
        "Mauricio"
    ]
}

'''db.nomes.insert_one(doc2)'''
# atribuindo coleção a uma variavel
colecao = db.nomes

# iterando sobre a coleção com o método find()

for post in colecao.find():
    print(post['nomes'])

# conectando em outra coleção

print(colecao.estimated_document_count())