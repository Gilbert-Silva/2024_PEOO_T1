from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__nasc = nasc
        if nome == "": raise ValueError("Nome inválido")
        if cpf == "": raise ValueError("CPF inválido")
        if fone == "": raise ValueError("Fone inválido")
        if nasc > datetime.now(): raise ValueError("Nascimento inválido")
    def idade(self):
        hoje = datetime.now()
        # Solução 1 - obtém o número de dias vividos e calcula o número aprox de anos e meses,
        #   dividindo os dias vividos por 365 e o resto por 30
        tempo = hoje - self.__nasc    # intervalo = tempo de vida
        dias = tempo.days             # número de dias vividos - 4000
        anos = dias // 365            # anos vividos           4000 // 365 = 10  
        meses = dias % 365 // 30      # meses vividos          4000 % 365  = 350
        return f"{anos} ano(s) e {meses} mes(es)"
        # Solução 2 - obtém os anos vividos diminuindo o ano atual do ano do nascimento
        #             e os meses vividos diminuindo o mês atual do mes do nascimento
        anos = hoje.year - self.__nasc.year
        meses = hoje.month - self.__nasc.month
        if meses < 0: 
            anos -= 1
            meses += 12
        return f"{anos} ano(s) e {meses} mes(es)"
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__fone} - {self.__nasc.strftime('%d/%m/%Y')}"

class UI:
    @staticmethod
    def menu():
        print("1 - Novo Paciente, 2 - Fim")
        return int(input("Informe uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.novo_paciente()
    @staticmethod
    def novo_paciente():
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        fone = input("Informe o fone: ")
        nasc = input("Informe a data de nascimento dd/mm/aaaa: ")
        p = Paciente(nome, cpf, fone, datetime.strptime(nasc, "%d/%m/%Y"))
        print(p)
        print(p.idade())

UI.main()                

