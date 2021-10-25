class Placar:
    def __init__(self):
        self.vitorias = 0
        self.derrotas = 0
    

    def setVitoria(self):
        self.vitorias += 1
    

    def setDerrota(self):
        self.derrotas += 1
        
    
    def getVitoria(self):
        return self.vitorias
    

    def getDerrotas(self):
        return self.derrotas
    

    def zeraPlacar(self):
        self.vitorias = 0
        self.derrotas = 0
    

    