class Corrida:
    def __init__(self):
        self.distancia = 1  # em metros
        self.horas = 1      # horas
        self.minutos = 1    # minutos
        self.segundos = 1   # segundos
    def pace(self):         # quantos minutos, o atleta gasta para correr um kilometro
        d = self.distancia / 1000
        t = self.horas * 60 + self.minutos + self.segundos/60
        return t/d
    
c = Corrida()
c.distancia = float(input("Informe a distância percorrida em metros: "))
c.horas = int(input("Informe o número de horas: "))
c.minutos = int(input("Informe o número de minutos: "))
c.segundos = int(input("Informe o número de segundos: "))
print(f"Seu pace é de {c.pace()} minutos/km")




