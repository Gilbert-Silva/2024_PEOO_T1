class Corrida:                # entidade - modelo de uma corrida
    def __init__(self):       # definição dos atributos no __init__
        # atributos estão encapsulados - garante que os dados são válidos
        self.__distancia = 1  # em metros
        self.__horas = 1      # horas
        self.__minutos = 1    # minutos
        self.__segundos = 1   # segundos
    def set_distancia(self, distancia): # definição da distância
        if distancia > 0: self.__distancia = distancia
        else: raise ValueError("Distância não pode ser negativa")
    def get_distancia(self):            # retorno o valor do atributo
        return self.__distancia
    def set_tempo(self, tempo): #hh:mm:ss - definição do tempo
        t = tempo.split(":")
        self.__horas = int(t[0])
        self.__minutos = int(t[1])
        self.__segundos = int(t[2])
        if self.__horas < 0 or self.__minutos < 0 or self.__segundos < 0 or self.__horas + self.__minutos + self.__segundos == 0:
          raise ValueError("Tempo informado é inválido")
    def get_tempo(self): # retorna os atributos no formato h:m:s
        return f"{self.__horas}:{self.__minutos}:{self.__segundos}"
    def pace(self):         # quantos minutos, o atleta gasta para correr um kilometro
        d = self.__distancia / 1000
        t = self.__horas * 60 + self.__minutos + self.__segundos/60
        return t/d
