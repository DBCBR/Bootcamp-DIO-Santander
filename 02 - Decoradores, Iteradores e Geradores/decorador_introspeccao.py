import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)

    return envelope


@meu_decorador
def ola_mundo(nome, idade):
    print(f'Olá mundo, {nome} você tem {idade} anos!')
    return nome.upper()


print(ola_mundo.__name__)
