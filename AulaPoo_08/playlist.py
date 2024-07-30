class PlayList:
    def __init__(self, nome, descricao):
        if nome != "": self.__nome = nome
        else: raise ValueError("Informe um nome")
        self.__descricao = descricao
        self.__musicas = []
    def inserir(self, m):  # m é um objeto da classe Música
        self.__musicas.append(m)
    def listar(self):
        return self.__musicas[:]
    def __str__(self):
        return f"Playlist {self.__nome} - {self.__descricao} tem {len(self.__musicas)} música(s)"    