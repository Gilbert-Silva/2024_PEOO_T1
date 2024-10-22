from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios

class View:
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        Clientes.inserir(c)

    def horario_inserir(data):
        c = Horario(0, data)
        Horarios.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def horario_listar():
        return Horarios.listar()    

    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)    