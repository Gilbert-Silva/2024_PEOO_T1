from enum import IntFlag

class Dias(IntFlag):
    Domingo = 1   # 0000.0001
    Segunda = 2   # 0000.0010
    Terca = 4
    Quarta = 8
    Quinta = 16
    Sexta = 32
    Sabado = 64

def menu():
    print("Informe 0 para encerrar...")
    dia = int(input("Selecione um dia: 1 - Domingo, 2 - Segunda, ... , 7 - Sábado: "))
    return dia   

def main():
    dias = Dias(0) 
    op = 10
    while op != 0:
        op = menu()
        match op:
            case 1: dias = dias | Dias.Domingo
            case 2: dias = dias | Dias.Segunda
            case 3: dias = dias | Dias.Terca
            case 4: dias = dias | Dias.Quarta
            case 5: dias = dias | Dias.Quinta
            case 6: dias = dias | Dias.Sexta
            case 7: dias = dias | Dias.Sabado
    print(dias)

main()



