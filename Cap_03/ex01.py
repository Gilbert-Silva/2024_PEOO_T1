from datetime import datetime
class Aluno:
    def __init__(self, nome, nasc):
        self.nome = nome
        self.nasc = nasc
    def __str__(self):
        return f"{self.nome} - {self.nasc}"

a = Aluno("Gilbert", datetime.strptime("10/10/2000", "%d/%m/%Y"))
b = Aluno("Eduardo", datetime.strptime("15/10/2000", "%d/%m/%Y"))
c = Aluno("Álvaro", datetime.strptime("5/5/2000", "%d/%m/%Y"))
alunos = [a, b, c]
for obj in alunos:
    if obj.nasc.month == 10: print(obj)

import uuid
print(str(uuid.uuid4()))

