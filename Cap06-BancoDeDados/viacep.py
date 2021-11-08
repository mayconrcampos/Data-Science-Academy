import requests

cep = input("Digite o cep: ")
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

print(response.status_code)
print(response.json())

endereco = response.json()


print(f"Logradouro: {endereco['logradouro']}")
print(f"Complemento: {endereco['complemento']}")
print(f"Bairro: {endereco['bairro']}")
print(f"Localidade: {endereco['localidade']}")
print(f"UF: {endereco['uf']}")
print(f"IBGE: {endereco['ibge']}")
print(f"DDD: {endereco['ddd']}")