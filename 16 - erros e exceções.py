 

try:
    conta = 10 / 0

    print(conta)
except ZeroDivisionError:
    print("Divisão por zero, não pode!")


def divide(num1, num2):
    print(f"{num1} / {num2} = {num1 / num2}")


while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    if num1.isnumeric() and num2.isnumeric():
        num1 = int(num1)
        num2 = int(num2)

        try:
            divide(num1, num2)

            denovo = input("Deseja continuar? sim ou nao")
            if denovo == "sim":
                continue
            else:
                print("Então tchau.")
                break

        except ZeroDivisionError as e:
            print(f"{e} - Não é possível dividir por zero. Tente novamente.")

        except TypeError:
            print("Número inválido. Tente novamente")
            

    else:
        print("Digite novamente")