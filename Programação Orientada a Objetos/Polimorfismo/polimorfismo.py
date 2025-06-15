class Passaro:
    def voar(self):
        print("Voando alto no céu!")


class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Não posso voar, mas posso correr rápido!")


class Aviao:
    def voar(self):
        print("Decolando e voando alto!")


def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())
