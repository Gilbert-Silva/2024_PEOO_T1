from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, cor):
        self.__cor = cor
    @abstractmethod
    def getArea(self):
        pass

class Circulo(Figura):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio
    def getArea(self):
        return math.pi * self.__raio ** 2
    

x = Circulo("Azul", 1)
print(x.getArea())
print(isinstance(x, Circulo))
print(isinstance(x, Figura))
print(isinstance(x, ABC))
print(isinstance(x, object))


