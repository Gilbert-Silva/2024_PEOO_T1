from datetime import datetime
from datetime import timedelta

x = datetime(2024, 8, 6)
y = datetime(2000, 10, 5, 10, 30, 20)
z = datetime(2024, 1, 1)

print(x)
print(y)
tempo = x-z
print(tempo)
print(type(tempo))

a = datetime(day=28, month=2, year=2023)
umdia = timedelta(days=1)
print(a)
a = a + umdia
print(a)
a = a + umdia
print(a)






