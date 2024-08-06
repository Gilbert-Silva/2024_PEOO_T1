from datetime import datetime
from datetime import timedelta


texto = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
x = datetime.strptime(texto, "%d/%m/%Y")
print(x)   # datetime
y = datetime.now()
print(y-x) # timedelta


