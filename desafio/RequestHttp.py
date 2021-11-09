import requests

print(requests.__version__)

resposta = requests.get("https://viacep.com.br/ws/01001000/json/")
print(resposta.status_code)
print(resposta.text)

resposta = dict(resposta.text)

print(resposta)