


class Livro:
    def __init__(self):
        self._titulo = ""
        self._isbn = ""
    
    def setTitulo(self, titulo):
        self._titulo = titulo
    
    
    def getTitulo(self):
        return self._titulo
    
    
    def setISBN(self, isbn):
        self._isbn = isbn
    
    def getISBN(self):
        return self._isbn

    def imprime(self):
        print(f"Título : {self.getTitulo()} - ISBN: {self.getISBN()}")



livro = Livro()
livro.setTitulo("O monge e o Executivo")
livro.setISBN("8327469827364")

livro.imprime()

