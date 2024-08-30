from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome):
        self.nome = nome
        self.nasc = datetime(1582,10,3)

x = Paciente("Gilbert")
print(x.nome)
print(x.nasc)

x.nasc = x.nasc + timedelta(days = 1)
print(x.nasc)

x.nasc = x.nasc + timedelta(days = 1)
print(x.nasc)

x.nasc = x.nasc + timedelta(days = 1)
print(x.nasc)

y = float(input("Informe um valor real: "))
print(y + 0.5)


