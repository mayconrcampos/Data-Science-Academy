from palavras import Palavras
from forca import Forca
from jogo import Jogo

jogo = Jogo()
palavra = Palavras()

while True:
    print("---- Jogo da Forca ------")
    print("1. Novo Jogo")
    print("2. Sair")

    opcao = input("Opção 1-2 : ")

    if opcao == "1":
        palavraSorteada = palavra.sorteio()

        tentativa = 0
        while True:

            letra = input("Digite a letra: ")

            if not len(letra) > 1:
                jogo.jogada(letra, palavra.getSorteada())

                
                

    else:
        pass

    