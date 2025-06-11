salario = 4000


def salario_bonus(bonus):
    global salario  # Declara que vamos usar a variável global 'salario'
    salario += bonus  # Adiciona o bônus ao salário global
    return salario


salario_bonus(1000)  # Chama a função com um bônus de 1000
print(salario)  # Imprime o salário atualizado
