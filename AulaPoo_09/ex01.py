class Jogador:
    def __init__(self, nome, gols):
        self.__nome = nome
        self.__gols = gols
    def get_nome(self):
        return self.__nome
    def get_gols(self):
        return self.__gols

j1 = Jogador("Gilbert", 10)
j2 = Jogador("Minora", 8)
jogadores = []
jogadores.append(j1)
jogadores.append(j2)
print(j1.get_nome())
print(jogadores[0].get_nome())
print(jogadores[0].get_gols())
for j in jogadores: print(j.get_gols())
print(id(j1))
print(id(jogadores[0]))
