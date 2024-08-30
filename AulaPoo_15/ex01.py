import json
from datetime import datetime
import enum

class EstadoCivil(enum.Enum):
  Solteiro = 1
  Casado = 2
  Divorciado = 3
  Viúvo = 4

class Paciente:
    def __init__(self, id, nome, fone, nasc, estado):
        self.id = id
        self.__nome = nome
        self.fone = fone
        self.nasc = nasc
        self.estado = estado
    def __str__(self):
        return f"{self.id} - {self.__nome} - {self.fone} - {self.nasc.strftime('%d/%m/%Y')} - {self.estado}"
    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["nome"] = self.__nome
      dic["fone"] = self.fone
      dic["nasc"] = self.nasc.strftime("%d/%m/%Y")
      dic["estado"] = self.estado.value
      return dic    

class Pacientes:
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
      c.fone = obj.fone
      c.nasc = obj.nasc
      c.estado = obj.estado
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
  def aniversariantes(cls, mes):
    cls.abrir()
    r = []
    for c in cls.objetos:
      if c.nasc.month == mes: r.append(c) 
    return r

  @classmethod
  def salvar(cls):
    with open("pacientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Paciente.to_json)
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("pacientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Paciente(obj["id"], obj["nome"], obj["fone"], datetime.strptime(obj["nasc"], "%d/%m/%Y"), EstadoCivil(obj["estado"]))
          cls.objetos.append(c)
    except FileNotFoundError:
      pass


class UI:
  @staticmethod
  def menu():
    print("Cadastro de Pacientes")
    print("  1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Aniversariantes")
    print("Outras opções")
    print("  9 - Fim")

    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 9:
      op = UI.menu()
      if op == 1: UI.paciente_inserir()
      if op == 2: UI.paciente_listar()
      #if op == 3: UI.paciente_atualizar()
      #if op == 4: UI.paciente_excluir()
      if op == 5: UI.paciente_aniversariantes()

  @staticmethod
  def paciente_inserir():
    nome = input("Informe o nome: ")
    fone = input("Informe o fone: ")
    nasc = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
    estado = int(input("Informe o estado civil: 1-Solteiro(a), 2-Casado(a), 3-Divorciado(a), 4-Viúvo(a): "))
    c = Paciente(0, nome, fone, nasc, EstadoCivil(estado))
    Pacientes.inserir(c)

  @staticmethod
  def paciente_listar():  
    for c in Pacientes.listar():
      print(c)

  @staticmethod
  def paciente_aniversariantes(): 
    mes = int(input("Informe o mês da lista de aniversariantes: ")) 
    for c in Pacientes.aniversariantes(mes):
      print(c)
 
UI.main()


