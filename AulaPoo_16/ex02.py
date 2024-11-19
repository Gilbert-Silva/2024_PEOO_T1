class MeuErro(Exception):
  def __init__(self, valor):
    self.valor = valor

def func(x):
  if x < 1: raise MeuErro(x)
  return x - 1

print(func(2))
print(func(1))
try:
  print(func(0))
except MeuErro as x:
  print("Deu erro, o valor informado foi", x.valor)



try:
  a = int(input("Informe o dividendo: "))
  b = int(input("Informe o divisor: "))
  print(a/b)
except Exception as erro:
  print(type(erro))
  print(erro)
  print(vars(erro))
