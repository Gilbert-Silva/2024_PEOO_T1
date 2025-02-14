from cliente import Cliente, Clientes

#a = Cliente(1, "Teste", "Teste@email.com", "1234", "1234")
#Clientes.inserir(a)

#a = Cliente(4, "Gilbert", "gilbert@email.com", "4444", "8888")
#Clientes.atualizar(a)

#a = Cliente(4, "", "", "", "")
#Clientes.excluir(a)

for c in Clientes.listar():
    print(c)

