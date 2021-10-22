

class Jogo:
    def __init__(self):
        self.letrasErradas = []
        self.jogadas = 1


    def jogada(self, chute, jogada):
        acertou = False
        indices = []
        for indice in range(len(jogada)):
            if jogada[indice] == chute.lower():
                acertou = True
                indices.append(indice)
                      
        if acertou:
            for l in indices:
                print(f"Acertou nos indices: {l}")
            print(f"Indices {indices}")
        else:
            print("Errou tudo")



