from controller.funcionario_controller import FuncionarioController
from controller.cliente_controller import ClienteController
from controller.produto_controller import ProdutoController


def mostrar_menu_principal():
    print("\n" + "="*50)
    print("     SISTEMA DE GERENCIAMENTO")
    print("="*50)
    print("1 - Gestão de Funcionários")
    print("2 - Gestão de Clientes")
    print("3 - Gestão de Produtos")
    print("0 - Sair")
    print("="*50)


def main():
    while True:
        mostrar_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            controller = FuncionarioController()
            controller.run()
        elif opcao == "2":
            controller = ClienteController()
            controller.run()
        elif opcao == "3":
            controller = ProdutoController()
            controller.run()
        elif opcao == "0":
            print("\nAté logo!")
            break
        else:
            print("\n>>> Opção inválida!\n")


if __name__ == "__main__":
    main()
