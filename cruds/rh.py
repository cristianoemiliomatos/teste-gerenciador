
def rh():
    import sys
    from pathlib import Path

    caminho_raiz = Path(__file__).parent.parent
    sys.path.append(str(caminho_raiz))

    import funcoes

    while True:
        print("""
        |=============================|
        |        PAINEL DO RH         |
        |=============================|
        """)

        print("1 - cadastrar funcionario")
        print("2 - Lista de funcionarios")
        print("3 - Demitir funcionario")
        print("3 - Sair")
        opcao = int(input("Digite a opção que voce quer: "))
        match opcao:
            case 1:
                funcoes.cadastrar_funcionario()
            case 2:
                funcoes.listar_funcionarios()
            case 3:
                funcoes.remover_funcionario()
            case 4:
                print("Saindo !!!")
                break
            case _:
                print("Opção Invalida")