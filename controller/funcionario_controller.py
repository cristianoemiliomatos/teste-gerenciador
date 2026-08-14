from model.funcionario import FuncionarioModel
from view.funcionario_view import FuncionarioView


class FuncionarioController:
    def __init__(self):
        self.model = FuncionarioModel()
        self.view = FuncionarioView()

    def run(self):
        while True:
            self.view.mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.remover()
            elif opcao == "4":
                self.buscar()
            elif opcao == "5":
                self.atualizar()
            elif opcao == "0":
                break
            else:
                self.view.mostrar_mensagem("Opção inválida!")

    def cadastrar(self):
        dados = self.view.pedir_dados_cadastro()
        if dados[0] is None:
            return
        nome, salario, cpf = dados
        sucesso, mensagem = self.model.cadastrar(nome, salario, cpf)
        self.view.mostrar_mensagem(mensagem)

    def listar(self):
        funcionarios = self.model.listar_todos()
        self.view.listar_funcionarios(funcionarios)

    def remover(self):
        id_func = self.view.pedir_id()
        if id_func is None:
            return
        sucesso, mensagem = self.model.remover(id_func)
        self.view.mostrar_mensagem(mensagem)

    def buscar(self):
        id_func = self.view.pedir_id()
        if id_func is None:
            return
        funcionario = self.model.buscar_por_id(id_func)
        if funcionario:
            id_f, nome, cpf, salario = funcionario
            self.view.mostrar_mensagem(f"ID: {id_f} | Nome: {nome} | CPF: {cpf} | Salário: R$ {salario:.2f}")
        else:
            self.view.mostrar_mensagem("Funcionário não encontrado!")

    def atualizar(self):
        id_func = self.view.pedir_id()
        if id_func is None:
            return

        print("\nO que deseja atualizar?")
        print("1 - Nome")
        print("2 - Salário")
        print("3 - CPF")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = self.view.pedir_novo_nome()
            sucesso, mensagem = self.model.atualizar(id_func, nome=nome)
        elif opcao == "2":
            salario = self.view.pedir_novo_salario()
            if salario is None:
                return
            sucesso, mensagem = self.model.atualizar(id_func, salario=salario)
        elif opcao == "3":
            cpf = self.view.pedir_novo_cpf()
            sucesso, mensagem = self.model.atualizar(id_func, cpf=cpf)
        else:
            self.view.mostrar_mensagem("Opção inválida!")
            return

        self.view.mostrar_mensagem(mensagem)
