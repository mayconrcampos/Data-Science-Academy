class Numeros:
    def __init__(self):
        self.numero1 = None
        self.numero2 = None

    def setNumero01(self, num):
        self.numero1 = num
    
    def getNumero01(self):
        return self.numero1
    

    def setNumero02(self, num):
        self.numero2 = num
    

    def getNumero02(self):
        return self.numero2
    

class Calculadora:
    @staticmethod
    def soma(n: Numeros):
        print(f"{n.getNumero01()} + {n.getNumero02()} = {n.getNumero02() + n.getNumero01()}")
    
    @staticmethod
    def subtrai(n: Numeros):
        print(f"{n.getNumero01()} - {n.getNumero02()} = {n.getNumero01() - n.getNumero02()}")
    
    @staticmethod
    def multiplica(n: Numeros):
        print(f"{n.getNumero01()} x {n.getNumero02()} = {n.getNumero01() * n.getNumero02()}")
    

    @staticmethod
    def divide(n: Numeros):
        try:
            print(f"{n.getNumero01()} / {n.getNumero02()} = {n.getNumero01() / n.getNumero02()}")
        except ZeroDivisionError as erro:
            print(f"{erro} - Não é possível dividir nenhum número por ZERO. Tente novamente.")
    


def paraounao():
    n = input("Deseja continuar? S ou N")
    if n in "sS":
        return True
    else:
        return False       
        
        

Numeros = Numeros()
while True:
    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o segundo número: ")
    if n1.isnumeric() and n2.isnumeric():

        Numeros.setNumero01(int(n1))
        Numeros.setNumero02(int(n2))

        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")

        opcao = input("Digite a opção, ou 0 pra sair.")

        if opcao == "0":
            print("Você saiu da aplicação.")
            break
        elif opcao == "1":
            Calculadora.soma(Numeros)
            s = paraounao()
            if not s:
                break
            
        elif opcao == "2":
            Calculadora.subtrai(Numeros)
        elif opcao == "3":
            Calculadora.multiplica(Numeros)
        elif opcao == "4":
            Calculadora.divide(Numeros)
        else:
            print("Opção inválida, tente novamente.")
    
    else:
        print("Números inválidos. Tente novamente.")