import datetime

data = datetime.datetime.now()

print(data)

tempo = datetime.time(7, 43, 28)
print(tempo)

print(f"Hora: {data.hour}")
print(f"Minuto: {data.minute}")
print(f"Segundo: {data.second}")
print(f"Milissegundo: {data.microsecond}")

hoje = datetime.datetime.today()

print(hoje)

# descobrindo intervalo de dias entre datas

dia1 = datetime.date(2019, 4, 28)
print(dia1)

dia2 = dia1.replace(year=2021, month=10, day=18)
print(dia2)

print(f"Diferença: {dia2 - dia1}")