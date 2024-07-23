class Frete:
    def __init__(self, produto, distancia, peso):
        self.set_produto(produto)
        self.set_distancia(distancia)
        self.set_peso(peso)
    def __str__(self):
        return f"{self.__produto} - {self.__distancia} - {self.__peso}"    
    def get_produto(self):
        return self.__produto
    def get_distancia(self):
        return self.__distancia
    def get_peso(self):
        return self.__peso
    def set_produto(self, produto):
        if produto != "": self.__produto = produto
        else: raise ValueError("Produto não pode ser vazio")
    def set_distancia(self, distancia):
        if distancia > 0: self.__distancia = distancia
        else: raise ValueError("Distância não pode ser negativa")
    def set_peso(self, peso):
        if peso > 0: self.__peso = peso
        else: raise ValueError("Peso não pode ser negativo")
    def frete(self):
        return self.__distancia * self.__peso / 100

class UI:  # interface com o usuário - print/input estão aqui
    @staticmethod
    def menu():
        print("1 - Calcular, 2 - fim")
        return int(input("Informe uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.calculo()
    @staticmethod
    def calculo():
        nome = input("Informe o nome do produto: ")
        distancia = float(input("Informe a distância: "))
        peso = float(input("Informe o peso: "))
        f = Frete(nome, distancia, peso)
        #f.set_produto(nome)
        #f.set_distancia(distancia)
        #f.set_peso(peso)
        print(f)
        #print(f"Produto {f.get_produto()} - {f.get_distancia()} - {f.get_peso()}")
        print(f"Frete = {f.frete()}")

UI.main()


