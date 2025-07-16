from datetime import datetime, timedelta

tipo_carro = "P"
tempo_pequeno = timedelta(minutes=30)
tempo_medio = timedelta(minutes=60)
tempo_grande = timedelta(minutes=120)
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + tempo_pequeno
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + tempo_medio
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + tempo_grande
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
