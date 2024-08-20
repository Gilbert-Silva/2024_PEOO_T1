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
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.email = obj.email
      c.fone = obj.fone
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
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

class UI:
  @staticmethod
  def menu():
    print("1 - Inserir cliente, 2 - Listar clientes, 3 - atualizar cliente, 4 - excluir cliente, 9 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 9:
      op = UI.menu()
      if op == 1: UI.cliente_inserir()
      if op == 2: UI.cliente_listar()
      if op == 3: UI.cliente_atualizar()
      if op == 4: UI.cliente_excluir()

  @staticmethod
  def cliente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    c = Cliente(0, nome, email, fone)
    Clientes.inserir(c)

  @staticmethod
  def cliente_listar():  
    for c in Clientes.listar():
      print(c)

  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    c = Cliente(id, "", "", "")
    Clientes.excluir(c)

UI.main()
