# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from crud import Crud

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone
    self.senha = senha
  def __str__(self):
    return f"{self.nome} - {self.email} - {self.fone}"

# Persistência
class Clientes(Crud):
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

