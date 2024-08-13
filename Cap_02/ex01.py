from datetime import datetime

class Atleta:
    def __init__(self, nome : str, peso : float, altura : float):
        self.nome = nome
        self.peso = peso
        self.altura = altura
    def __str__(self):
        return f"{self.nome} - {self.peso} kg - {self.altura} m"    

class Time:
    def __init__(self, nome : str):
        self.nome = nome
        self.atletas = []
    def inserir(self, obj : Atleta):
        self.atletas.append(obj)
    def __str__(self):
        return f"{self.nome} tem {len(self.atletas)} atleta(s)"    

class Compromisso:
    def __init__(self, titulo : str, local : str, data : datetime):
        self.titulo = titulo
        self.local = local
        self.data = data
    def __str__(self):
        agora = datetime.now()
        if self.data < agora:
            return f"{self.titulo} - {self.local} - {self.data} - aconteceu há {agora - self.data}"
        else:
            return f"{self.titulo} - {self.local} - {self.data} - vai acontecer em {self.data - agora}"
                

c1 = Compromisso("Cap POO", "Lab11", datetime.strptime("13/08/2024 10:30", "%d/%m/%Y %H:%M"))
print(c1)

t = input("Informe o título do compromisso: ")
l = input("Informe o local: ")
d = input("Informe a data do compromisso 'dd/mm/aaaa hh:mm': ")

c2 = Compromisso(t, l, datetime.strptime(d, "%d/%m/%Y %H:%M"))
print(c2)

n = input("Informe o nome do atleta: ")
p = input("Informe o peso do atleta em kg: ")
a = float(input("Infome a altura em metros: "))
x = Atleta(n, float(p), a)
print(x)


n = input("Informe o nome do atleta: ")
p = input("Informe o peso do atleta em kg: ")
a = float(input("Infome a altura em metros: "))
y = Atleta(n, float(p), a)
print(y)


t = input("Informe o nome do time: ")
time = Time(t)
time.inserir(x)
time.inserir(y)
print(time)



