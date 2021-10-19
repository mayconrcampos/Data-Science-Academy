import os

def soma():
    n1 = num1()
    n2 = num2()

    if n1 and n2:
        print(f"{n1} + {n2} = {n1+n2}")
    else:
        print("Conta inválida. Digite somente números acima de zero.")

def subtracao():
    n1 = num1()
    n2 = num2()

    if n1 and n2:
        print(f"{n1} - {n2} = {n1-n2}")
    else:
        print("Conta inválida. Digite somente números acima de zero.")

def multiplicacao():
    n1 = num1()
    n2 = num2()

    if n1 and n2:
        print(f"{n1} x {n2} = {n1*n2}")
    else:
        print("Conta inválida. Digite somente números acima de zero.")

def divisao():
    n1 = num1()
    n2 = num2()

    if n1 and n2:
        print(f"{n1} / {n2} = {n1/n2:.2f}")
    else:
        print("Conta inválida. Digite somente números acima de zero.")

def num1():
    n = input("Digite o primeiro número: ")
    if n.isnumeric() and int(n) > 0:
        return int(n)
    else:
        return False

def num2():
    n = input("Digite o segundo número: ")
    if n.isnumeric() and int(n) > 0:
        return int(n)
    else:
        return False


while True:
    print("Selecione o número da operação:");
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

    opcao = input("Digite sua opção: 1-2-3-4 ou 0 pra Sair: ")
    os.system("clear")

    if opcao == "1":
        soma()
    elif opcao == "2":
        subtracao()
    elif opcao == "3":
        multiplicacao()
    elif opcao == "4":
        divisao()
    elif opcao == "0":
        print("Você saiu do programa.")
        break
    else:
        print("Você digitou uma opção inválida.")
