from datetime import datetime
from datetime import timedelta
x = datetime.now()
print(x)
y = timedelta(days=1, hours=15)
print(y)
print(x + y)
print(type(x))
print(type(y))

x = datetime.now()
y = datetime(2024, 12, 31)
print(x)
print(y)
print(x-y)

