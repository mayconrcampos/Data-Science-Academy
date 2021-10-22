class Animal:
    def __init__(self):
        print("Animal criado")
    
    def identifica(self):
        print("Animal")
    

    def comer(self):
        print("Animal comendo")


class Cachorro(Animal):
    def __init__(self):
        print("Objeto cachorro criado")
    
    def identifica(self):
        print("Cachorro")
    
    def comer(self):
        print("Cachorro comendo")
    

    def latir(self):
        print("Cachorro latindo")



animal = Animal()
animal.identifica()
animal.comer()

catioro = Cachorro()
catioro.comer()
catioro.identifica()
catioro.latir()