class Disciplina:
    def __init__(self):                       # atributo - 10
        self.__nome = "sem nome"              # encapsulamento - 10
        self.__nota1 = 0                      # validação - 10
        self.__nota2 = 0                      # get - 10
        self.__notaf = 0                      # set - 10
    def get_nome(self):                       # cálculo - 10
        return self.__nome
    def get_nota1(self):
        return self.__nota1
    def get_nota2(self):
        return self.__nota2
    def get_notaf(self):
        return self.__notaf
    def set_nome(self, nome):
        if nome != "": self.__nome = nome
        else: raise ValueError("Nome não pode ser vazio")
    def set_nota1(self, nota1):
        if 0 <= nota1 <= 100: self.__nota1 = nota1
        else: raise ValueError("Nota deve estar entre 0 e 100")
    def set_nota2(self, nota2):
        if 0 <= nota2 <= 100: self.__nota2 = nota2
        else: raise ValueError("Nota deve estar entre 0 e 100")
    def set_notaf(self, notaf):
        if 0 <= notaf <= 100: self.__notaf = notaf
        else: raise ValueError("Nota deve estar entre 0 e 100")
    def media(self):
        mp = (2*self.__nota1 + 3*self.__nota2) / 5
        if mp >= 60: return mp
        return (mp + self.__notaf) / 2

                                       # classe/static - 10
                                       # menu/main - 10
                                       # calcular/obj
                                       # entrada/saída de dados - 10

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
        d = Disciplina()
        nome = input("Informe o nome da disciplina: ")
        nota1 = int(input("Informe a nota do 1º bimestre: "))
        nota2 = int(input("Informe a nota do 2º bimestre: "))
        notaf = int(input("Informe a nota da avaliação final: "))
        d.set_nome(nome)
        d.set_nota1(nota1)
        d.set_nota2(nota2)
        d.set_notaf(notaf)
        print(f"Disciplina {d.get_nome()} - {d.get_nota1()} - {d.get_nota2()} - {d.get_notaf()}")
        print(f"Média = {d.media()}")

UI.main()


    
        
