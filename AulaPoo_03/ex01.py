class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
print(x)
print(x.b)
print(x.h)
x.b = float(input("Digite o valor da base: "))
x.h = float(input("Digite o valor da altura: "))
print(x.b)
print(x.h)
print(x.calc_area())
y = Triangulo()
y.b = float(input("Digite o valor da base: "))
y.h = float(input("Digite o valor da altura: "))
print(y.b)
print(y.h)
print(y.calc_area())




