class Triangulo:               # entidade
    def __init__(self):        # construtor
        self.__b = 1           # atibutos - atributos de uma instância (objeto)
        self.__h = 1
    def set_base(self, valor):
        if valor > 0: self.__b = valor
        else: raise ValueError("A base não pode ser negativa")
    def get_base(self):
        return self.__b    
    def set_altura(self, valor):
        if valor > 0: self.__h = valor
        else: raise ValueError("A altura não pode ser negativa")
    def get_altura(self):
        return self.__h    
    def calc_area(self):       # método de cálculo - método de instância
        return self.__b * self.__h / 2
