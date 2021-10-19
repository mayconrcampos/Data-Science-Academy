

var = True

while True:
    n = int(input("Digite o numero: "))
    if n == 1:
        var = False
        print("Acabou")
        break
    else:
        print(f"Número digitado: {n}")


numero = 1
conta = 0
while numero < 50:
    print(numero)
    numero += 1
    if(numero == 48):
        numero = 1
        conta += 1
        if(conta == 3):
            print("acabou")
            break