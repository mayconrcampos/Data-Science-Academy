from random import randint

class Palavras:
    def __init__(self):
        self.palavras = ["Axioma", "Azulejo", "Blitz", "Catarro", "Coçar", "Crespo", "Cripta", "Duplex", "Girar", "Gnóstico", "Icterícia", "Jazz", "Intrigante", "Marfim", "Psique", "Indigno", "Vapor", "Vértice", "Anel", "Farinha", "Fósforo", "Bronquite", "Traquinagem", "Computador", "Salgado", "Foligem", "Prestobarba", "Privilégio", "Bunda", "Braço", "Cabeça", "Monitor", "Zorba", "Zebra", "Chantagem", "Trambolho", "Rolha", "Relento", "Oceano", "Tempestade", "Urbano", "América", "Argentina", "Colombia", "Farofa", "Peixe", "Camarão"]
        self.sorteada = []
  
    

    def sorteio(self):
        self.sorteada.append(self.palavras[randint(0, len(self.palavras))].lower())
        return self.sorteada[0]
    
    def getSorteada(self):
        self.sorteada[0]
    
    def sorteadasHistorico(self):
        return self.sorteada
    
    def mascara(self):
        mascara = ""
        




        
