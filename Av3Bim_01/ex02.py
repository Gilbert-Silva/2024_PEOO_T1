from datetime import datetime, timedelta

class Evento:                     # 5 - classe
    def __init__(self, n, d, l):  # 5 - atributos
        self.__nome = n           # 5 - get/set
        self.__data = d           # 5 - init
        self.__local = l
    def get_nome(self):
        return self.__nome
    def get_data(self):
        return self.__data
    def get_local(self):
        return self.__local
    def set_nome(self, n):
        self.__nome = n
    def set_data(self, d):
        self.__data = d
    def set_local(self, l):
        self.local = l

class NumDiasError(Exception):    # 5 - classe + herança
    def __init__(self, dias):     # 5 - atributo
        super().__init__("Número de dias inválido")
        self.__dias = dias        # 5 - get
    def get_dias(self):           # 5 - init
        return self.__dias

class Congresso(Evento):                 # 5 - classe + herança
    def __init__(self, n, d, l, nd, i):  # 5 - atributos
        super().__init__(n, d, l)        # 5 - init e super 
        self.set_numdias(nd)             # 5 - raise e validação
        self.__inscricao = i             # 5 - get/set
    def get_numdias(self):               # 5 - data final
        return self.__numdias            # 10 - lista de dias
    def get_inscricao(self):
        return self.__inscricao
    def set_numdias(self, nd):
        self.__numdias = nd
        if nd < 1 or nd > 30:
            raise NumDiasError(nd)      
    def set_inscricao(self, i):
        self.__inscricao = i 
    def data_final(self):
        d = timedelta(days=self.__numdias - 1)
        return self.get_data() + d
    def dias(self):
        d = timedelta(days=1)
        x = self.get_data()
        dias = []
        for p in range(self.__numdias):
            dias.append(x)
            x = x + d
        return dias        

def main():
    nome = input("Informe o nome: ")
    data = datetime.strptime(input("Informe a data: "), "%d/%m/%Y")
    local = input("Informe o local: ")
    numdias = int(input("Informe o número de dias: "))
    inscricao = float(input("Informe o valor da inscrição: "))
    try:
        c = Congresso(nome, data, local, numdias, inscricao)
        print(c.get_nome())      # 5 - input
        print(c.get_data())         # 5 - CompraParcelada
        print(c.get_local())        # 10 - try except
        print(c.get_numdias())
        print(c.get_inscricao())
        print(c.data_final())
        print(c.dias())
    except NumDiasError as erro:
        print("Número de dias inválido")
        print(erro.get_dias())

main()   

