nomes = []
matrs = []
k = 0
while k < 3:
    nome = input("Informe seu nome: ")
    matr = input("Informe sua matrícula: ")
    nomes.append(nome)
    matrs.append(matr)
    k += 1
for k in range(3):
    nome = nomes[k]
    matr = matrs[k]
    ano = int(matr[0:4])
    print(f"Nome = {nome}, Matrícula = {matr}, Ano = {ano}")