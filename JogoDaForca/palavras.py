from random import randint

class Palavras:
    def __init__(self):
        self.palavras = ["Axioma", "Azulejo", "Blitz", "Catarro", "Coçar", "Crespo", "Cripta", "Duplex", "Girar", "Gnóstico", "Icterícia", "Jazz", "Intrigante", "Marfim", "Psique", "Indigno", "Vapor", "Vértice", "Anel", "Farinha", "Fósforo", "Bronquite", "Traquinagem", "Computador", "Salgado", "Foligem", "Prestobarba", "Privilégio", "Bunda", "Braço", "Cabeça", "Monitor", "Zorba", "Zebra", "Chantagem", "Trambolho", "Rolha", "Relento", "Oceano", "Tempestade", "Urbano", "América", "Argentina", "Colombia", "Farofa", "Peixe", "Camarão"]

        self.sorteada = []
        self.mascarada = ""
  
    def sorteio(self):
        existe = False
        for palavra in self.sorteada:
            if self.palavras[randint(0, len(self.palavras) - 1)].lower() == palavra:
                existe = True
                break

        if not existe:  
            self.sorteada.append(self.palavras[randint(0, len(self.palavras) - 1)].lower())
            return self.sorteada[-1]
        else:
            self.sorteio()
    

    def getSorteada(self):
        self.sorteada[-1]
    
    def sorteadasHistorico(self):
        print(f"Histórico: {self.sorteada}")
    
    def geraMascara(self):
        for letra in self.sorteada[-1]:
            self.mascarada += " - "
        
    def zeraMascara(self):
        self.mascarada = ""
    
    def imprimeMascara(self):
        print(f"Dica: {self.mascarada}")
    

    def retiraMascara(self, l):
        for indice in range(0, len(self.sorteada[-1]) - 1):
            print(l, self.sorteada[-1][indice])
            #if l == self.sorteada[-1][indice]:
            #    self.mascarada[indice].replace(self.mascarada[indice], l)
            #    print(f"pacaba {l} - {self.mascarada}")


        


        
