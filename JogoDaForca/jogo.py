from forca import Forca
from palavras import Palavras

class Jogo():
    def __init__(self):
        #super().__init__()
        self.letrasErradas = list()
        self.jogadas = 1
        self.forca = Forca() 
        self.palavra = Palavras()
        


    def jogada(self, chute, jogada):
        acertou = False
        indices = []
        for indice in range(len(jogada)):
            if jogada[indice] == chute.lower():
                acertou = True
                indices.append(indice)
                #self.palavra.retiraMascara(indice)
                      
        if acertou:
            for l in indices:
                print(f"Acertou nos indices: {l}")
                self.forca.imprimeForca2()
    
        else:
            self.letrasErradas.append(chute)
            print(f"Letras Erradas: {self.letrasErradas}")
            print("======================================")
            print(self.forca.imprimeForca())
            #print(self.imprimeMascara())
            print("======================================")
            self.jogadas += 1
    

    def reiniciarJogo(self):
        self.letrasErradas = list()
        self.jogadas = 1
        self.forca.zeraForca()
        self.palavra.zeraMascara()
        
            
            


  