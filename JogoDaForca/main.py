from palavras import Palavras
from forca import Forca
from jogo import Jogo
from os import system

jogo = Jogo()
palavra = Palavras()
forca = Forca()

while True:
    print("---- Jogo da Forca ------")
    print("1. Novo Jogo")
    print("2. Histórico de Palavras jogadas")
    print("3. Sair")

    opcao = input("Opção 1-2-3 : ")

    if opcao == "1":
        palavraSorteada = palavra.sorteio()

        tentativa = 1

        while True:
            
            letra = input("Digite a letra: ").lower()
            system("clear")


            if len(letra) > 0 and len(letra) < 2:

                print(f"Letra digitada: {letra}")

                jogo.jogada(letra, palavraSorteada)
                
                print(f"Palavra Sorteada da lista: {palavraSorteada} - tentativa: {tentativa}")
                
                tentativa += 1
                if jogo.jogadas == 7:
                    print("Você perdeu.")
                    jogo.reiniciarJogo()
                    break
            else:
                print("Jogada Inválida. Digite somente uma letra.")
    elif opcao == "2":
        palavra.sorteadasHistorico()
    
    elif opcao == "3":
        print("Fim do joguinho.")
        break   
                

    else:
        pass

    