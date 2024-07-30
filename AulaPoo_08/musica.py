class Musica:
    def __init__(self):
        self.__titulo = ""
        self.__artista = ""
        self.__album = ""
    def set_titulo(self, titulo):
        if titulo != "": self.__titulo = titulo
        else: raise ValueError("Informe um título")
    def set_artista(self, artista):
        if artista != "": self.__artista = artista
        else: raise ValueError("Informe um artista")
    def set_album(self, album):
        if album != "": self.__album = album
        else: raise ValueError("Informe um álbum")
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album}"
    
