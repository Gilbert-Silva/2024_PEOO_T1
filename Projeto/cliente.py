# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
  
class Clientes:
  objetos = []    # atributo estático
  @classmethod
  def inserir(cls, obj):
    cls.objetos.append(obj)
  @classmethod
  def listar(cls):
    return cls.objetos
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)
  @classmethod
  def abrir(cls):
    cls.objetos = []
    with open("clientes.json", mode="r") as arquivo:   # r - read
      texto = json.load(arquivo)
      for obj in texto:   
        c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
        cls.objetos.append(c)
  
def teste1():
  a = Cliente(1, "Douglas Crockford", "email1@email.com", "1234")  # json
  b = Cliente(2, "Jon Bosak", "email@gmail.com", "4321")          # xml
  #crud = Clientes()
  Clientes.inserir(a)
  Clientes.inserir(b)
  Clientes.salvar()
  for c in Clientes.listar(): print(c)

def teste2():
  #crud = Clientes()
  Clientes.abrir()
  for c in Clientes.listar(): print(c)

teste2()








       