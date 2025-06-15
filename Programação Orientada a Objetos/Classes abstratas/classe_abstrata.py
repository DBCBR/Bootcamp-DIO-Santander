from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("TV ligada")

    def desligar(self):
        print("TV desligada")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ar-condicionado ligado")

    def desligar(self):
        print("Ar-condicionado desligado")

    @property
    def marca(self):
        return "Samsung"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
