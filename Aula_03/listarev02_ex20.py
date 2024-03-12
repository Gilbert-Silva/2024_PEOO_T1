#n = int(input())
for n in range(1, 11):
    print(n, end=" ")
    for k in range(1, n + 1):
        if k % 2 == 0: print(k, end=" ")
    print()    
