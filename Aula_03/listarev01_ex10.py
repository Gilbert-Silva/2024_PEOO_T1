print("Digite uma data no formato dd/mm/aaaa")
data = input()
dia, mes, ano = data.split("/")
d = int(dia)
m = int(mes)
a = int(ano)
maior = 31
if m == 4 or m == 6 or m == 9 or m == 11: maior = 30
if m == 2:
    if a%4==0 and a%100!=0 or a%400==0: maior = 29
    else: maior = 28

if a>=1900 and a<=2100 and m>=1 and m<=12 and d>=1 and d<=maior:
    print("A data é válida")
else:
    print("A data é inválida")

