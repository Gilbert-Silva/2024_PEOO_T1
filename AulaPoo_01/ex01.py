class Triangulo:
    def __init__(self):     # método construtor
        self.b = 0          # atributo ou campo
        self.h = 0
    def calc_area(self):    # método
        return self.b * self.h / 2
    
x = Triangulo()
print(x)
x.b = 10
x.h = 20
print(x.b, x.h)
y = x
y.b = 30
y.h = 40
print(x.b, x.h)
z = Triangulo()



       