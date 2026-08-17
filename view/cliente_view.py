class ClienteView:
    @staticmethod
    def mostrar_menu():
        print("\n" + "=" * 50)
        print("         GESTÃO DE CLIENTES")
        print("=" * 50)
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Remover cliente")
        print("4 - Buscar por CPF")
        print("5 - Editar cliente")
        print("0 - Voltar")
        print("=" * 50)

    @staticmethod
    def pedir_dados_cadastro():
        return (input("Nome: "), input("CPF: "), input("Endereço: "), input("Email: "))

    @staticmethod
    def pedir_id():
        try:
            return int(input("Digite o ID do cliente: "))
        except ValueError:
            print("Erro: ID deve ser um número!")
            return None

    @staticmethod
    def pedir_cpf():
        return input("Digite o CPF: ")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(f"\n>>> {mensagem}\n")

    @staticmethod
    def listar_clientes(clientes):
        if not clientes:
            print("\nNenhum cliente encontrado!")
            return
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | CPF: {cliente[2]} | Email: {cliente[3]}")

    @staticmethod
    def mostrar_cliente(cliente):
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | CPF: {cliente[2]} | Email: {cliente[3]} | Endereço: {cliente[4]}")

    @staticmethod
    def pedir_opcao_edicao():
        try:
            return int(input("1-Nome  2-Email  3-Endereço: "))
        except ValueError:
            return None

    pedir_novo_nome = staticmethod(lambda: input("Novo nome: "))
    pedir_novo_email = staticmethod(lambda: input("Novo email: "))
    pedir_novo_endereco = staticmethod(lambda: input("Novo endereço: "))
