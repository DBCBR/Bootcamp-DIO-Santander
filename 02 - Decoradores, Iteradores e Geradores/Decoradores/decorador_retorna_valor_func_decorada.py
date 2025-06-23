def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('faz algo antes da execução da função decorada')
        resultado = funcao(*args, **kwargs)
        print('faz algo depois da execução da função decorada')
        return resultado
    return envelope


@meu_decorador
def ola_mundo(nome, idade):
    print(f'Olá mundo, {nome} você tem {idade} anos!')
    return nome.upper()


resuldato = ola_mundo('David', 38)
print(resuldato)
