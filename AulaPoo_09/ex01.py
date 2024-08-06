class Jogador:
    def __init__(self, nome, gols):
        self.__nome = nome
        self.__gols = gols
    def get_nome(self):
        return self.__nome
    def get_gols(self):
        return self.__gols
    def __str__(self):
        return f"{self.__nome} - {self.__gols}"

j1 = Jogador("Gilbert", 10)
j2 = Jogador("Minora", 8)
j3 = Jogador("Eduardo", 15)
jogadores = []
jogadores.append(j1)
jogadores.append(j2)
jogadores.append(j3)
for j in jogadores: print(j)

x = [10, 15, 8, 20]
print(max(x))

maior = jogadores[0]
for j in jogadores:
    if j.get_gols() > maior.get_gols(): maior = j
print(maior)

#print(max(jogadores))
