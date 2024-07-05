class Aluno:
    def __init__(self):
        self.nome = ""
        self.matricula = ""
        self.email = ""
    def ano_ingresso(self):         # 01234567890
        return self.matricula[0:4]  # 2023101111####
    def curso(self):
        return self.matricula[5:10]
        
a1 = Aluno()   
a1.nome = "Igor"
a1.matricula = "20231011119000"
a1.email = "igor@ifrn.edu.br"

print(a1.nome)
print(a1.matricula)
print(a1.email)
print(a1.ano_ingresso())
print(a1.curso())

