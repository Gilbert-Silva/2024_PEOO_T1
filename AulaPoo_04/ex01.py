class Triangulo:               # entidade
    def __init__(self):        # construtor
        self.__b = 1           # atibutos - atributos de uma instância (objeto)
        self.__h = 1
    def set_base(self, valor):
        if valor > 0: self.__b = valor
        else: raise ValueError("A base não pode ser negativa")
    def get_base(self):
        return self.__b    
    def set_altura(self, valor):
        if valor > 0: self.__h = valor
        else: raise ValueError("A altura não pode ser negativa")
    def get_altura(self):
        return self.__h    
    def calc_area(self):       # método de cálculo - método de instância
        return self.__b * self.__h / 2

class UI:       # interface com o usuário - prints e inputs são feitos aqui!

    @staticmethod 
    def main(): # método da classe
      op = 0
      while op != 2:
          op = UI.menu()
          if op == 1: UI.area_triangulo()

    @staticmethod
    def menu():
        print("1 - Calcular área do triângulo")
        print("2 - Fim")
        return int(input("Escolha a opção: "))

    @staticmethod
    def area_triangulo():
        #y = Triangulo()
        #print(y)
        #y.set_base(10)
        x = Triangulo()  # x é uma variável local do método area_triangulo
        print(x)
        # versão sem encapsulamento
        #x.b = float(input("Informe o valor da base: "))    # set
        #x.h = float(input("Informe o valor da altura: "))
        #print(f"O triângulo tem base = {x.b}")             # get
        #print(f"O triângulo tem altura = {x.h}")
        # versão com encapsulamento
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        print(f"O triângulo tem base = {x.get_base()}") 
        print(f"O triângulo tem altura = {x.get_altura()}")
        print(f"A área = {x.calc_area()}")     # uma instância chamando um método de instância

UI.main()                         # uma classe chamando um método de classe




