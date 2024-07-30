import random
class Bingo:
    def __init__(self):
        self.__numBolas = 10
        self.__sorteados = []
    def iniciar(self, numBolas):
        if numBolas > 0: self.__numBolas = numBolas
        else: raise ValueError("Número de bolas deve ser positivo")
        self.__sorteados.clear()
    def proximo(self):  # sorteia um número e armazena na lista
        if len(self.__sorteados) == self.__numBolas: return "Fim do Jogo"
        n = random.randint(1, self.__numBolas)
        #print("Dentro do método", n)
        while n in self.__sorteados:
            n = random.randint(1, self.__numBolas)
            #print("Dentro do método", n)
        self.__sorteados.append(n)
        return n
    def sorteados(self):
        return sorted(self.__sorteados)

class UI:
    @staticmethod
    def menu():
        print("1-Novo Jogo, 2-Próximo, 3-Sorteados, 4-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main(): 
        b = Bingo()              
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.novo_jogo(b)
            if op == 2: UI.proximo(b)
            if op == 3: UI.sorteados(b)
    @staticmethod
    def novo_jogo(b):
        n = int(input("Informe o número de bolas do bingo: "))
        b.iniciar(n)
    @staticmethod
    def proximo(b):
        print(b.proximo())
    @staticmethod
    def sorteados(b):
        print(b.sorteados())

UI.main()

    
