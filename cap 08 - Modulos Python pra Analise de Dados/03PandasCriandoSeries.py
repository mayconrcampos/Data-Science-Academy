import pandas as pd
from pandas import Series
from pandas.core import indexing

print(pd.__version__)


"""CRIANDO SÉRIES"""

# Criando uma série sem especificar os índices
obj = Series([67, 78, -56, 13])

print(obj)
print(type(obj))

print(obj.values)
print(obj.index)


# Criando uma série e especificando os indices
obj2 = Series([67, 78, -66, 34], index=["a", "b", "c", "d"])
print(obj2)
print(obj2.values)
print(obj2.index)

# retornar tudo o que for maior que 3
print(obj2[obj2 > 3])


# imprimindo valor na posição b
print(obj2["b"])

# Verificar se indice se encontra dentro do objeto
indice = "d" in obj2
print(indice)


# Criando uma série de dados passando um dicionário como parâmetro
dicio = {
    "futebol":5200,
    "Tenis":120,
    "Natação":690,
    "Volley":1550
}

obj3 = Series(dicio)

print(obj3)
print(type(obj3))

"""MANIPULANDO SÉRIES"""

esportes = ["futebol", "Tenis", "Natação", "Basketball"]

# Criando uma série usando uma lista como indice
obj4 = Series(dicio, index=esportes)
print(obj4)

print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())

# concatenando séries
print(obj3 + obj4)

obj4.name = "População"
obj4.index.name = "esporte"

print(obj4)


