from forca import Forca
from palavras import Palavras
from os import system


forca = Forca() 
palavra = Palavras()

class Jogo():
    def __init__(self):
        self.letrasErradas = list()
        self.jogadas = 0
        self.historicoDePalavrasSorteadas = []
        self.palavraDaVez = ""
        self.acertou = False

        
    def jogada(self):

        if self.jogadas == 0:
            self.palavraDaVez = palavra.sorteio()
            self.historicoDePalavrasSorteadas.append(self.palavraDaVez)
            palavra.geraMascara()
            self.jogadas += 1
        
        while True:
            
            letra = input("Digite a letra: ").lower()
            system("clear")
            print("-="*30)

            if len(letra) > 0 and len(letra) < 2:
                
                letra = letra.lower().strip()
                
                print(f"Você digitou: {letra}")
                

                #print("Palavra Sorteada: ", self.palavraDaVez)

                for index in range(0, len(self.palavraDaVez)):
                    if self.palavraDaVez[index] == letra:
                        palavra.removeMascara(letra, index)

                        

                        self.acertou = True

                
                if self.acertou:
                    if self.venceu():
                        return False

                    print("Você já tentou, mas estão erradas: ", self.letrasErradas)

                    print("Acertou!")
                    palavra.imprimeMascara()
                    forca.imprimeForca2()
                    self.acertou = False
                    print("-="*30)

                elif self.acertou == False:
                    if self.perdeu():
                        return False

                    print("Errou!")

                    self.jogadas += 1

                    #print("DEBUG ",self.jogadas)

                    self.letrasErradas.append(letra)

                    print("Você já tentou, mas estão erradas: ", self.letrasErradas)

                    palavra.imprimeMascara()
                    forca.imprimeForca()
                    print("-="*30)
                    


            else:
                print("Jogada Inválida. Digite somente uma letra.")

        
                      

    def reiniciarJogo(self):
        self.letrasErradas = list()
        self.jogadas = 0
        forca.zeraForca()
        palavra.zeraMascara()
    
                
    def sorteadasHistorico(self):
        print(f"Histórico de Palavras Sorteadas: {self.historicoDePalavrasSorteadas}")
    
    def venceu(self):
        if " - " not in palavra.mascarada:
            print("Parabéns! Você Venceu! A palavra secreta era ", self.palavraDaVez)
            self.reiniciarJogo()
            return True
    
    def perdeu(self):
        if self.jogadas == 6:
            print("Você perdeu! A palavra secreta era ", self.palavraDaVez)
            self.reiniciarJogo()
            return True
    
   
    def historico(self):
        return self.historicoDePalavrasSorteadas
            
    #def imprimeTentativas(self):
    #    for item in self.letrasErradas:
    #        print("Tentativas: ", item, end=" ")

    
            
