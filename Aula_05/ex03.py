class Aluno:
    def __init__(self):       # construtor
        self.nome = ""        # atributo
        self.matricula = ""
    def ano_ingresso(self):   # método
        return int(self.matricula[0:4])

a = Aluno()
a.nome = "Igor"
a.matricula = "20231011110000"
b = Aluno()
b.nome = "Clara"
b.matricula = "20241011110001"
print(a)
print(a.nome, a.matricula, a.ano_ingresso())
print(b)
print(b.nome, b.matricula, b.ano_ingresso())

