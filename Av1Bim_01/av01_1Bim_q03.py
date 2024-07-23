print("Digite uma frase com três palavras")
s = input()           # 6 - entrada
palavras = s.split()  # 6 - divisão
x = palavras[0]
y = palavras[1]
z = palavras[2]
m = min(len(x), len(y), len(z)) # 6 - menor/maior valor
#m = max(len(x), len(y), len(z))
if len(x) == m: print(x)  # 6 - teste
if len(y) == m: print(y)  # 6 - resultado
if len(z) == m: print(z)



