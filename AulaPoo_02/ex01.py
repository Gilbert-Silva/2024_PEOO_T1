class Circulo:   # modelo OO de uma figura geométrica: círculo
    pass

a = Circulo()
b = Circulo()
c = a
print(a)
print(b)
print(c)
x = 5
y = 5
x = 10
print(id(a))
print(id(b))
print(id(c))
print(id(x))
print(id(y))
b = None
print(type(b))
print(id(b))


