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
        else:
            self.conta = 0
            print("Game over")



