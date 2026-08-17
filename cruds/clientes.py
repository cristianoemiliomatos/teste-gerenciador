def cliente():
    import sys
    from pathlib import Path

    caminho_raiz = Path(__file__).parent.parent
    sys.path.append(str(caminho_raiz))

    import funcoes
    while True:
        print("""
            |=============================|
            |      PAINEL DO CLIENTE      |
            |=============================|
            """)

        print("1 - Fazer compras")
        print("2 - Historico de compras")
        print("3 - Historico financeiro")
        print("4 - Sair")

        opcao = int(input("Digite a opção que deseja: "))

        match opcao:
            case 1:
                funcoes.comprar_produto()
            case 2:
                funcoes.historico_cliente()
            case 3:
                funcoes.historico_financeiro_pessoal()
            case 4:
                break
            case _:
                print("Opção invalida !!!")