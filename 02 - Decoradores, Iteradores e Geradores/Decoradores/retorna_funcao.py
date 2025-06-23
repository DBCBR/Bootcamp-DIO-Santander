def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div


print(calculadora("+")(2, 3))  # Saída: 5
print(calculadora("-")(5, 2))  # Saída: 3
print(calculadora("*")(3, 4))  # Saída: 12
print(calculadora("/")(10, 2))  # Saída: 5.0
