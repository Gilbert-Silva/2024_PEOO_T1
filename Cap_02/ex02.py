from datetime import datetime
from datetime import timedelta

class Aluno:
    def __init__(self, nome, mat):
        self.nome = nome
        self.mat = mat
    def __str__(self):
        return f"Sou um aluno chamado(a) {self.nome}"
a = 1
b = 1.5
c = False
d = "Teste"
e = "10/08/2024"
f = datetime.strptime(e, "%d/%m/%Y")
g = datetime.now()
h = g - f
i = Aluno("Gibert", "07687965")
j = [3, 1, 2]
k = (3, 1, 2)
l = { 3, 1, 2 }
m = { "key1" : 1,  "key2" : 5 }

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))
print(k, type(k))
print(l, type(l))
print(m, type(m))
print(i.__dict__)





