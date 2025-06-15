class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando um objeto Cachorro")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Destruindo o objeto Cachorro")

    def latir(self):
        print('Au Au!')


def criar_cachorro():
    c = Cachorro("Rex", "Marrom", False)
    print(c.nome)
    c.latir()


criar_cachorro()
