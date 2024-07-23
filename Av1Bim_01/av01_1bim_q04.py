print("Escreva números inteiros, digite 0 para parar")
x = 10 # qualquer valor diferente de zero
total = 0
while x != 0:
    x = int(input())
    if x % 2 == 0 and x != 0:
        total += x     # somando
        # total += 1   # contando
print(total)        




 