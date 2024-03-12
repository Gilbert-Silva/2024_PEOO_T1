print("Digite uma frase:")
frase = input()

for x in range(len(frase)):
   frase = frase[1:] + frase[0]
   print(frase)

