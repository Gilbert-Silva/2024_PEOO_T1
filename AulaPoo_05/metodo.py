class Teste:
    def __init__(self):
        self.atributo1 = 1    # público   - todo mundo pode usar
        self._atributo2 = 2   # protegido - deve ser usado na classe e nas classes descendentes de Teste
        self.__atributo3 = 3  # privado   - deve ser usado apenas na classe Teste
    def metodo1(self):
        return self.atributo1
    def _metodo2(self):
        return self._atributo2
    def __metodo3(self):
        return self.__atributo3
    def metodo4(self):
        return self.__metodo3()

x = Teste()
print(x.atributo1)         # o acesso é ok
print(x._atributo2)        # o acesso é possível mas não deve ser feito
#print(x.__atributo3)      # não é possível acessar
print(x._Teste__atributo3) # o acesso com o nome da classe não deve ser feito
print(x.metodo1())
print(x._metodo2())
#print(x.__metodo3())
print(x._Teste__metodo3())
print(x.metodo4())




