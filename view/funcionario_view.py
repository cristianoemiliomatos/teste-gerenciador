class FuncionarioView:
    @staticmethod
    def mostrar_menu():
        print("\n" + "="*50)
        print("         GESTÃO DE FUNCIONÁRIOS")
        print("="*50)
        print("1 - Cadastrar funcionário")
        print("2 - Listar funcionários")
        print("3 - Remover funcionário")
        print("4 - Buscar funcionário")
        print("5 - Atualizar funcionário")
        print("0 - Voltar")
        print("="*50)

    @staticmethod
    def pedir_dados_cadastro():
        nome = input("Digite o nome do funcionário: ")
        try:
            salario = float(input("Digite o salário do funcionário: "))
        except ValueError:
            print("Erro: Salário deve ser um número!")
            return None, None, None
        cpf = input("Digite o CPF do funcionário: ")
        return nome, salario, cpf

    @staticmethod
    def pedir_id():
        try:
            return int(input("Digite o ID do funcionário: "))
        except ValueError:
            print("Erro: ID deve ser um número!")
            return None

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(f"\n>>> {mensagem}\n")

    @staticmethod
    def listar_funcionarios(funcionarios):
        if not funcionarios:
            print("\nNenhum funcionário encontrado!")
            return
        print("\n" + "="*80)
        print(f"{'ID':<5} {'NOME':<30} {'CPF':<15} {'SALÁRIO':<15}")
        print("="*80)
        for id_func, nome, cpf, salario in funcionarios:
            print(f"{id_func:<5} {nome:<30} {cpf:<15} R$ {salario:.2f}")
        print("="*80 + "\n")

    @staticmethod
    def pedir_novo_nome():
        return input("Digite o novo nome: ")

    @staticmethod
    def pedir_novo_salario():
        try:
            return float(input("Digite o novo salário: "))
        except ValueError:
            print("Erro: Salário deve ser um número!")
            return None

    @staticmethod
    def pedir_novo_cpf():
        return input("Digite o novo CPF: ")
