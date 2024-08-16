x = {"RN" : ["Natal", "Parnamirim"], "PB" : "João Pessoa", "PE" : "Recife"}
print(x)
print(type(x))
print(x["RN"][0])
print(x["PB"])
print(x["PE"])
x["AM"] = "Manaus"
print(x)
x["RN"] = "Natal"
print(x)
print(*x)

for item in x.items():
    print(item, type(item))
    


