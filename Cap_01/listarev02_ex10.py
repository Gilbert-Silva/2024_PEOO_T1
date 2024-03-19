s = input()
for x in s: # passa em cada elemento da lista/string/range
    s = s[1:] + s[0]
    print(s)
print()
k = 0
while k < len(s):
    k += 1
    s = s[1:] + s[0]
    print(s)
    #print(k)
