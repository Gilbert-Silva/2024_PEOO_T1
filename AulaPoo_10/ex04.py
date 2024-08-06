from datetime import datetime
from datetime import timedelta

x = datetime.now() # método de classe
print(x.day)       # atributo
print(x.month)
print(x.year)
print(x.hour)
print(x.minute)
print(x.second)
print(x.date())    # método de instância
print(x.time())
print(x.weekday())
print(x.strftime("%d/%m/%Y %H:%M"))
print(x.strftime("%A, %d/%B/%Y"))
print(x.strftime("%a, %d/%b/%y"))





x = datetime.now()
t = 0
for i in range(1000000):
  t += 1
y = datetime.now()
print(y-x)


