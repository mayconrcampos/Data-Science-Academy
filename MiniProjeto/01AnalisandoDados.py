import re
import time
import sqlite3
import pycountry
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from sklearn.feature_extraction.text import CountVectorizer
import warnings

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid")


# conecta ao DB
conn = sqlite3.connect("imdb.db")

# Extrai a lista de tabelas
tabelas = pd.read_sql_query("SELECT NAME AS 'Table_Name' FROM sqlite_master WHERE type = 'table'", conn)

print(type(tabelas))

# Visualiza resultado
print(tabelas.head())

# Convertendo dataframe em uma lista
tabelas = tabelas["Table_Name"].values.tolist()

for tabela in tabelas:
    consulta = "PRAGMA TABLE_INFO({})".format(tabela)
    resultado = pd.read_sql_query(consulta, conn)
    print("Esquema da Tabela: ", tabela)
    print(resultado)
    print("-"*70)
    print("\n")


"""
Vamos responder as perguntas de negócio:

1 - Quais são as categorias de filmes mais comuns no IMDB?
"""

# Criando consulta SQL
consulta1 = """SELECT type, count(*) AS COUNT FROM titles GROUP BY type"""

# Extrai resultado
resultado1 = pd.read_sql_query(consulta1, conn)

# Visualizando resultado
print("R:. 1. Categorias Filmes mais comuns no IMDB")
print(resultado1)

# Calculando percentual para cada tipo, criando coluna percentual
resultado1['percentual'] = (resultado1['COUNT'] / resultado1['COUNT'].sum()) * 100

# Visualizando percentual
print("\n\nPercentual de cada tipo")
print(resultado1)


# Criando um gráfico com apenas 4 categorias:
# Criamos um dicionário vazio
others = {}

# Filtra percentual em 5% e soma o total
others['COUNT'] = resultado1[resultado1['percentual'] < 5]['COUNT'].sum()

# Grava o percentual
others['percentual'] = resultado1[resultado1['percentual'] < 5]['percentual'].sum()

# Ajusta o nome
others['type'] = "others"

# Visualiza
print(others)

# Filtra o dataframe de resultado
resultado1 = resultado1[resultado1['percentual'] > 5]

# Append com dataframe de outras categorias
resultado1 = resultado1.append(others, ignore_index=True)

# Ordena o resultado
resultado1 = resultado1.sort_values(by= "COUNT", ascending=False)

# Visualiza
print("\n\nSomente resultados acima de 5%")
print(resultado1.head())

# Ajusta os labels
labels = [str(resultado1['type'][i]) + ' ' +'['+str(round(resultado1['percentual'][i], 2)) + ' % ' + ' ] ' for i in resultado1.index]

# Plot
# Mapa de cores
#cs = cm.get_cmap("PuBuGn")

# Cria a figura
figura = plt.figure()

# Pie Plot = Pizza
plt.pie(resultado1['COUNT'], labeldistance=1, radius=2, wedgeprops=dict(width=0.8))
plt.legend(labels = labels, loc = 'center', prop = {'size': 12})
plt.title("Distribuição de Títulos", loc="Center", fontdict= {"fontsize": 20, "fontweight": 20})
plt.show()


"""2- Qual o Número de Títulos por Gênero?
Abaixo vamos calcular o número de filmes por gênero e entregar o resultado em valor percentual
"""

# Cria a consulta SQL
consulta2 = """SELECT genres, count(*) FROM titles WHERE type='movie' GROUP BY genres"""


# Resultado
resultado2 = pd.read_sql_query(consulta2, conn)

# Visualizando resultado
print("\n\nR:. 2. Número de títulos por gênero")
print(resultado2)

# Convertendo strings todas para minusculo
resultado2['genres'] = resultado2['genres'].str.lower().values

# remove valores NA ausentes
temp = resultado2['genres'].dropna()

"""Usamos o CountVectorizer para converter a coluna de gêneros em um vetor one-hot encoded para contar o número de filmes em cada gênero."""

# Vamos criar um vetor usando expressão regular para filtrar strings

padrao = '(?u)\\b[\\w-]+\\b'
vetor = CountVectorizer(token_pattern=padrao, analyzer='word').fit(temp)








