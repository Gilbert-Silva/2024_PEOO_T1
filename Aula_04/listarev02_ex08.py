s = input("Digite uma frase: ") + " "
# solução 1 - encontrando um espaço
for k in range(len(s)):
    if s[k] == " ": print(s[k-1], end="")
print()
# solução 2
palavras = s.split()
for p in palavras:
    print(p[-1], end="")

