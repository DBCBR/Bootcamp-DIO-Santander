from datetime import date
import datetime

data = date(2025, 7, 10)
print(data)
print(date.today())

# Opção 1: Usar datetime.date.today() para obter apenas a data
print(datetime.date.today())

# Opção 2: Usar datetime.datetime.today() para obter data e hora
print(datetime.datetime.today())
