from triangulo import Triangulo
from corrida import Corrida
#import triangulo
#import corrida

class UI:  # interface com o usuário - print/input estão aqui
    @staticmethod
    def menu():
        print("1 - corrida, 2 - triângulo, 3 - fim")
        return int(input("Informe uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.nova_corrida()
            if op == 2: UI.novo_triangulo()
    @staticmethod
    def nova_corrida():
        c = Corrida()
        distancia = int(input("Informe a distância em metros: "))
        tempo = input("Informe o tempo 'h:m:s': ")
        c.set_distancia(distancia)
        c.set_tempo(tempo)
        print(f"Seu pace foi {c.pace()} min/km")
    def novo_triangulo():
        x = Triangulo()  # x é uma variável local do método area_triangulo
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        print(f"O triângulo tem base = {x.get_base()}") 
        print(f"O triângulo tem altura = {x.get_altura()}")
        print(f"A área = {x.calc_area()}")     # uma instância chamando um método de instância

# padrão utilizado no Java, C#
UI.main()
