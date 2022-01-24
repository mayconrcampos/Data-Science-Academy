from random import randint
import os

dezenas = []

for i in range(1, 61):
    if i < 10:
        dezenas.append(f"0{i}")
    else:
        dezenas.append(str(i))



while True:
    print("-=-=-=-=-= Bem Vindos ao Gerador de Dezenas para a MEGA SENA -=-=-=-=-=-=")
    num = input("Digite o número de jogos que você quer fazer: => ")
    os.system("clear")

    while not num.isnumeric():
        num = input("Digite o número de jogos que você quer fazer: =>  ")

    if num.isdecimal() and int(num) > 0:
        num = int(num)

        jogos = []

        print(f"Você escolheu gerar {num} jogos.")
        for n in range(0, num):
            jogos.append(list())
            
            while len(jogos[n]) < 6:
                jogada = dezenas[randint(0, 59)]
                if jogada not in jogos[n]: 
                    jogos[n].append(jogada)
                    
        conta = 1
        for jogo in jogos:
            print(f"Jogo Nº: ({conta}) : ", end=" ")
            tamanho = 1
            for dezena in sorted(jogo):
                if tamanho == 6:
                    print(dezena, end=" ")
                else:
                    tamanho += 1
                    print(dezena, end=" - ")

            conta += 1
            print("\n")
            
        print("-=-=-=--=-=-= Boa Sorte Felo da Pota -=-=-=-=-=-=-=")
        print("\n\n\n\n\n")

    else:
        print("Você saiu")
        break




