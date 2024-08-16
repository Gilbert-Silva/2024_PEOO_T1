import json

class Cliente:
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome
  def __str__(self):
    return f"{self.id} - {self.nome}"
  
def salvar():
  a = Cliente(1, "Douglas Crockford")  # json
  b = Cliente(2, "Jon Bosak")          # xml
  #print(a)
  #print(b)
  #print(a.__dict__)
  #print(vars(b))
  lista = [a, b]
  with open("clientes.json", mode="w") as arquivo:   # w - write
    json.dump(lista, arquivo, default = vars)

def abrir():
  lista = []
  with open("clientes.json", mode="r") as arquivo:   # r - read
    texto = json.load(arquivo)
    for obj in texto:   # {"id": 1, "nome": "Douglas Crockford"}
      c = Cliente(obj["id"], obj["nome"])
      lista.append(c)
    for cliente in lista:
      print(cliente)


#salvar()
abrir()



  