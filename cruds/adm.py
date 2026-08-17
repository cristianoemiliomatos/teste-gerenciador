def adm():

    import sys
    from pathlib import Path

    caminho_raiz = Path(__file__).parent.parent
    sys.path.append(str(caminho_raiz))

    import funcoes
    while True:
        print("""
        |===================================|
        |      PAINEL DO ADMINISTRADOR      |
        |===================================|
        """)

        print("1 - Visualizar relatorio")
        print("2 - Historico de compras")
        print("3 - Historico financeiro")
        print("4 - Listar Funcionarios")
        print("5 - Sair")

        opcao = int(input("Digite a opção que voce deseja: "))
        match opcao:
            case 1:
                funcoes.estoque()
            case 2:
                funcoes.historico()
            case 3:
                funcoes.financeiro()
            case 4:
                funcoes.listar_funcionarios()
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opção Invalida !!!")