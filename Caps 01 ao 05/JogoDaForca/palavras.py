from random import randint

class Palavras:
    def __init__(self):
        self.palavras = ["Axioma", "Azulejo", "Blitz", "Catarro", "Coçar", "Crespo", "Cripta", "Duplex", "Girar", "Gnóstico", "Icterícia", "Jazz", "Intrigante", "Marfim", "Psique", "Indigno", "Vapor", "Vértice", "Anel", "Farinha", "Fósforo", "Bronquite", "Traquinagem", "Computador", "Salgado", "Foligem", "Prestobarba", "Privilégio", "Bunda", "Braço", "Cabeça", "Monitor", "Zorba", "Zebra", "Chantagem", "Trambolho", "Rolha", "Relento", "Oceano", "Tempestade", "Urbano", "América", "Argentina", "Colombia", "Farofa", "Peixe", "Camarão", "copo", "caneca", "mesa", "conector", "tomada", "plug", "pendrive", "livro", "caderno", "mouse", "toalha", "canela", "parede", "canetinha", "lombriga", "protozoário", "berimbau", "brotoeja", "sarna", "caixa", "holofote", "lâmpada", "gato", "cachorro", "vaca", "baleia", "dinossauro", "salsicha"]

        self.sorteada = []
        self.mascarada = []
  
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
    
    
    def geraMascara(self):
        for letra in self.sorteada[-1]:
            self.mascarada.append(" - ")
        
    def zeraMascara(self):
        self.mascarada = list()
    
    def imprimeMascara(self):
        print("Dica: ", end=" >>> ")
        for letra in self.mascarada:
            print(f"{letra}", end=" ")
        
        print(" <<<")
    
    def removeMascara(self, letra, indice):
        self.mascarada[indice] = letra
    
    
    
            


        


        
