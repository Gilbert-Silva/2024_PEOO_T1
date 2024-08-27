print("usando lista")

n = int(input())
while n != 0:
    numeros = []
    a = input()
    for x in map(int, a.split()):
        if x in numeros: numeros.remove(x)
        else: numeros.append(x)
    print(*numeros)
    n = int(input())


print("usando set")
n = int(input())
while n != 0:
    numeros = set()
    a = input()
    for x in map(int, a.split()):
        if x in numeros: numeros.remove(x)
        else: numeros.add(x)
    print(*numeros)
    n = int(input())

print("usando xor")
n = int(input())
while n != 0:
    numeros = 0
    a = input()
    for x in map(int, a.split()):
        numeros = numeros ^ x
    print(numeros)
    n = int(input())

print("usando xor 2")
n = int(input())
while n != 0:
    numeros = 0
    a = input() + " "
    s = ""
    for c in a:
        if c == " ":
            x = int(s)
            numeros = numeros ^ x
            s = ""
        else:
            s += c
    print(numeros)
    n = int(input())