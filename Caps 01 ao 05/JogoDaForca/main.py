from jogo import Jogo
from os import system

jogo = Jogo()

def main():
    while True:

        print("---- Jogo da Forca ------")
        print("1. Novo Jogo")
        print("2. Histórico de Palavras jogadas")
        print("3. Sair")

        opcao = input("Opção 1-2-3 : ")
        system("clear")

        if opcao == "1":
            jogo.jogada() 

        elif opcao == "2":
            jogo.historico()

        elif opcao == "3":
            print("Fim do joguinho.")
            break   

        
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

    