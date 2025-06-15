class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando: 'Blim blim blim!'")

    def parar(self):
        print("Parando a bicicleta.")
        print("A bicicleta está parada.")

    def acelerar(self):
        print("Acelerando a bicicleta.")
        print("A bicicleta está em movimento.")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


B1 = Bicicleta("vermelha", "Caloi", 2020, 1500.00)
print(f"Bicicleta 1: {B1.cor}, {B1.modelo}, {B1.ano}, R${B1.valor:.2f}")
B1.buzinar()
B1.parar()
B1.acelerar()

B2 = Bicicleta("azul", "Monark", 2021, 1800.00)
print(f"Bicicleta 2: {B2.cor}, {B2.modelo}, {B2.ano}, R${B2.valor:.2f}")
B2.buzinar()
B2.parar()
B2.acelerar()
