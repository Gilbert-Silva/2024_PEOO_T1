import enum

class Estacao(enum.Enum):
    Outono = 1
    Inverno = 2
    Primavera = 3
    Verão = 4

class Turno(enum.Enum):
    Matutino = 1
    Vespertino = 2
    Noturno = 3

class Turma:
    def __init__(self):
        self.curso = "Infoweb"
        self.ano = 2024
        self.turno = Turno.Vespertino

a = Estacao.Verão
print(a, type(a))
print(a.name)
print(a.value)

t = Turma()
print(t)
