class Livro:
    def __init__(self, titulo, autor, paginas):
        print("Livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    
    def __str__(self):
        # esse método é chamado assim que usamos a função print pra imprimir o objeto
        return f"Título: {self.titulo}, autor: {self.autor}, páginas: {self.paginas}"
    
    def __len__(self):
        return self.paginas
    
    def len(self):
        return print(f"Páginas do livro com método comum: {self.paginas}")


livro1 = Livro("Os Lusíadas", "Luis de Camões", 8816)

print(livro1)

print(str(livro1))

livro1.len()
print(len(livro1))