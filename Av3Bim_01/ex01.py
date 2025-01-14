from datetime import datetime

class Compra:                     # 5 - classe
    def __init__(self, c, d, v):  # 5 - atributos
        self.__cliente = c        # 5 - get/set
        self.__data = d           # 5 - init
        self.__valor = v
    def get_cliente(self):
        return self.__cliente
    def get_data(self):
        return self.__data
    def get_valor(self):
        return self.__valor
    def set_cliente(self, c):
        self.__cliente = c
    def set_data(self, d):
        self.__data = d
    def set_valor(self, v):
        self.__valor = v

class ParcelaError(Exception):        # 5 - classe + herança
    def __init__(self, parcelas):     # 5 - atributo
        super().__init__("Número de parcelas inválido")
        self.__parcelas = parcelas    # 5 - get
    def get_parcelas(self):           # 5 - init
        return self.__parcelas

class CompraParcelada(Compra):           # 5 - classe + herança
    def __init__(self, c, d, v, cr, p):  # 5 - atributos
        super().__init__(c, d, v)        # 5 - init e super 
        self.__cartao = cr               # 5 - raise e validação
        self.set_parcelas(p)             # 5 - get/set
    def get_cartao(self):                # 5 - valor parcela
        return self.__cartao             # 10 - vencimentos
    def get_parcelas(self):
        return self.__parcelas
    def set_cartao(self, cr):
        self.__cartao = cr
    def set_parcelas(self, p):
        self.__parcelas = p 
        if p < 2 or p > 12:
            raise ParcelaError(p)      
    def valor_parcela(self):
        return self.get_valor() / self.__parcelas
    def vencimentos(self):
        mes = self.get_data().month
        ano = self.get_data().year
        venc = []
        for p in range(self.__parcelas):
            mes = mes + 1
            if mes == 13:
                mes = 1
                ano = ano + 1
            data = datetime(year=ano, month=mes, day=1)
            venc.append(data)
        return venc        

def main():
    cliente = input("Informe o cliente: ")
    data = datetime.strptime(input("Informe a data: "), "%d/%m/%Y")
    valor = float(input("Informe o valor: "))
    cartao = input("Informe o cartão: ")
    parcelas = int(input("Informe o número de parcelas: "))
    try:
        c = CompraParcelada(cliente, data, valor, cartao, parcelas)
        print(c.get_cliente())      # 5 - input
        print(c.get_data())         # 5 - CompraParcelada
        print(c.get_valor())        # 10 - try except
        print(c.get_cartao())
        print(c.get_parcelas())
        print(c.valor_parcela())
        print(c.vencimentos())
    except ParcelaError as erro:
        print("Número de parcelas inválido")
        print(erro.get_parcelas())

main()   

