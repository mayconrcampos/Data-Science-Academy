from pandas import DataFrame

"""Dataframes representam uma estrutura tabular semelhante a estrutura de uma planilha excel, contendo uma coleção de colunas em que cada uma pode ser um diferente tipo de valor (numero, string, etc). Os dataframes possuem index e linhas e esta estrutura é muito semelhante a um dataframe em R. Os dados de um datafrane são armazenados em um ou mais blocos bidimensionais, ao invés de listas, dicionários ou alguma outra estrutura de array."""

data = {
    "Estado": ["Santa Catarina", "Paraná", "Rio Grande do Sul", "São Paulo", "Mato Grosso", "Mato Grosso do Sul"],
    "Ano": [2002, 2003, 2004, 2005, 2006, 2007],
    "População": [6.2, 3.5, 4.1, 5.5, 6.2, 7.5]
}

frame = DataFrame(data)

print(frame)
print(type(frame))

# Reordenando as colunas pelo nome
print(DataFrame(data, columns=["Ano", "Estado", "População"]))

frame2 = DataFrame(data, columns=["Ano", "Estado", "População", "Débito"], index=["um", "dois", "três", "quatro", "cinco", "seis"])
print(frame2)

# imprimindo apenas a coluna Estado
print(frame2['Estado'])
print(type(frame2))

print(frame2.index)

# Atribuindo valores à nova coluna
frame2['Débito']["um"] = "10000"
frame2['Débito']["dois"] = "5000"
frame2['Débito']["três"] = "15000"
frame2['Débito']["quatro"] = "70000"
frame2['Débito']["cinco"] = "18000"
frame2['Débito']["seis"] = "108000"


print(frame2)

"""Podemos criar mais uma coluna e preenche-la utilizando a biblioteca Numpy"""
import numpy as np

frame3 = DataFrame(data, columns=["Ano", "Estado", "População", "Débito"], index=["um", "dois", "três", "quatro", "cinco", "seis"])
print(frame3)

print(frame3.values)

# Resumo do DataFrame
print(frame3.describe())

frame3['Débito'] = np.arange(6.)


print(frame3)

# fazendo slice com os indices
print(frame3['dois': "quatro"])

"""Localizandon Registros Dentro do Dataframe"""

print(frame3.loc["três"])
print(frame3.iloc[3])
