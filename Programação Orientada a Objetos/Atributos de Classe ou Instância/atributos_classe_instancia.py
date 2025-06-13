class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Escola: {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("David", 1)
aluno_2 = Estudante("Ana", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "DIO - Digital Innovation One"
aluno_3 = Estudante("Carlos", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
