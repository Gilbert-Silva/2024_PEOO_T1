class Aluno:
    def __init__(self):
        self.nome = ""
        self.prox = None

a = Aluno()
b = Aluno()
c = Aluno()
d = Aluno()
e = Aluno()
a.nome = "Ana Alice"
a.prox = b
b.nome = "Igor"
b.prox = c
c.nome = "Danilo"
c.prox = d
d.nome = "Jamily"
d.prox = e
e.nome = "Juliana"
e.prox = None

x = a
while x != None:
    print(x.nome)
    x = x.prox
    