"""
Essas são
as suas missões:
Missão 1
: Implementar um algoritmo para determinar se uma string possui todos os caracteres exclusivos.

Missão 2
:Gerar uma lista de números primos.

Missão 3
:Implementar um algoritmo para mover um robô do canto superior esquerdo para o canto inferior direito de uma grade.

Missão 4
: Implementar o Algoritmo de Ordenação "Selection sort". 

Missão5
: Analisar o Comportamento de Compra de Consumidores
"""

def verificaString(stringue):
    for elemento in stringue:
        if elemento in "?/:;>.<,|\}]^~{[`´+=_-)(*&¨%$#@!\'":
            print("Fudeu!")
        else:
            print(f"{elemento}")


#verificaString("Maycon")



def primo(n):
    conta = 0 
    print(f"{n} é divisível por : ", end=" ")
    for numero in range(1, n + 1):
        if n % numero == 0:
            conta += 1
            print(f"{numero}", end=" - ")
  
            

    if conta == 2:
        print(f"O número {n} é Primo")
    else:
        print(f"O número {n} Não é primo")


while True:
    numero = input("Digite um número inteiro: Ou 0 pra sair. ")
    if numero.isnumeric():
        numero = int(numero)

        if numero > 1:
            primo(numero)
        else:
            print("Você saiu.")
            break

    else:
        print("Número inválido.")
        continue    