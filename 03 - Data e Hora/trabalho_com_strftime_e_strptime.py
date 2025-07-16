from datetime import datetime

data_hota_atual = datetime.now()
data_hora_str = "2025-07-10 10:53"
mascara_ptbr = "%d/%m/%Y"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hota_atual.strftime(mascara_ptbr))  # Formata a data atual

data_convertida = datetime.strptime(data_hora_str, mascara_en)  # Converte a string para datetime
print(data_convertida)  # Exibe a data convertida
print(type(data_convertida))  # Exibe o tipo da data convertida
