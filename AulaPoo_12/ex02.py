import enum

class Dia(enum.IntFlag):
    Domingo = 1     # 0000.0001
    Segunda = 2     # 0000.0010
    Terça = 4       # 0000.0100
    Quarta = 8      # 0000.1000
    Quinta = 16     # 0001.0000
    Sexta = 32      # 0010.0000
    Sábado = 64     # 0100.0000

hoje = Dia.Terça
peoo = Dia.Terça | Dia.Sexta    # | união
fds = Dia.Sábado | Dia.Domingo
print(hoje)
print(peoo)    
print(fds)

class EstadoMensagem(enum.Enum):
    Enviando = 1
    Enviada = 2
    Recebida = 3
    Lida = 4

class Mensagem:
    def __init__(self, texto):
        self.texto = texto
        self.estado = EstadoMensagem.Enviando


