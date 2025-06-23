def principal():
    print('executando a função principal')

    def funcao_interna():
        print('executando a função interna')

    def funcao_interna2():
        print('executando a função interna 2')

    funcao_interna()
    funcao_interna2()


principal()
