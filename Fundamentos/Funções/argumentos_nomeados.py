def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro salvo: {marca}, {modelo}, {ano}, {placa}")


salvar_carro("Toyota", "Corolla", 2020, "ABC-1234")
salvar_carro(marca="Honda", modelo="Civic", ano=2021, placa="XYZ-5678")
salvar_carro(
    **{
        "marca": "Ford",
        "modelo": "Focus",
        "ano": 2019,
        "placa": "LMN-8901"
    }
)
