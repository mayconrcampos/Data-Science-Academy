class Forca:
    def __init__(self):
        self.conta = 0
        self.forca = [
        """
            +---+
            |   |
            O   |
                |
                |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
            |   |
                |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
            |   |
           /    |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
            |   |
           / \  |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
           /|   |
           / \  |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        =========
        GAME OVER!
        """
        ]
    
    def imprimeForca(self):
        if self.conta < 7:
            print(self.forca[self.conta])
            self.conta += 1
            #print(self.conta)
    
    def imprimeForca2(self):
        if self.conta == 0:
            print(self.forca[0])
        else:
            print(self.forca[self.conta - 1])
    
    def zeraForca(self):
        self.conta = 0
            



