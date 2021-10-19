from os import WIFSTOPPED, read
from urllib.request import urlopen
import json

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode("utf-8")
data = json.loads(response)[0]

print(data)

print(f"Título: {data['title']}")
print(f"Descrição: {data['description']}")
print(f"URL: {data['url']}")
print(f"Data Upload: {data['upload_date']}")


# Copiando estes dados para dentro de um arquivo


with open("filme.json", "w") as arquivo_in:
    arquivo_in.write(json.dumps(data))

with open("filme.json", "r") as arquivo:
    texto = arquivo.read()
    with open("filme_out.json", "w") as arquivo_out:
        arquivo_out.write(texto)


print(arquivo_out)

# Método dois

open("filme_out.json", "w").write(open("filme.json", "r").read())