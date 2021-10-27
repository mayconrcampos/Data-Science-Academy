from datetime import datetime
from pymongo import MongoClient

# Criando conexão com DB
conn = MongoClient("localhost", 27017)

# Verificando tipo
print(type(conn))

#  Uma única instância do MongoDB suporta vários Bancos de dados

# Vamos criar o banco de dados cadastrodb
db = conn.cadastrodb

# Verificando tipo
print(type(db))

# uma coleção é um grupo de documentos armazenados no MongoDB
# São as tabelas dos bancos relacionais
collection = db.cadastrodb

# Verificando tipo
print(type(collection))

""" 
Uma nota importante sobre collections no MongoDB é que eles são criados posteriormente. Ou seja, nenhum dos comandos acima executou efetivamente qualquer operação no servidor MongoDB. Coleções e bancos de dados são criados quando o primeiro documento é inserido.
"""

"""
Dados no MongoDB são representados e armazenados usando documentos JSON. Com o PyMongo usamos dicionários para representar documentos.
"""

post1 = {
    "código":"ID-7823764",
    "prod_name":"Geladeira",
    "marcas": ["Brastemp", "Consul", "Electrolux"],
    "data_cadastro": datetime.utcnow()
}

# Verificando tipo
print(type(post1))

# Inserindo o dicionário no DB
collection = db.posts

post_id = collection.insert_one(post1)

# Verificando a chave da inserção
print(post_id.inserted_id)

# quando um documento é inserido, uma chave especial _id é adicionada automaticamente se o documento ainda não contém uma chave _id
print(post_id)


# inserindo segundo documento

post2 = {
    "código":"ID-4378634",
    "prod_name":"Televisor",
    "marcas": ["Samsung", "Panasonic", "Sony"],
    "data_cadastro": datetime.utcnow()
}

collection = db.posts
post_id = collection.insert_one(post2).inserted_id

print(post_id)

# buscando valores
for post in collection.find():
    print(post['prod_name'])


# verificando nome do DB
print(db.name)

# Listando as coleções disponíveis
print(db.list_collection_names())