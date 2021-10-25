from jogo import Jogo

jogo = Jogo()


while True:

    print("---- Jogo da Forca ------")
    print("1. Novo Jogo")
    print("2. Histórico de Palavras jogadas")
    print("3. Sair")

    opcao = input("Opção 1-2-3 : ")

    if opcao == "1":
        jogo.jogada() 
    elif opcao == "2":
        print(jogo.historico())

    elif opcao == "3":
        print("Fim do joguinho.")
        break   
                
    
    else:
        print("Opção inválida.")




    