from model.cliente import ClienteModel
from view.cliente_view import ClienteView


class ClienteController:
    def __init__(self):
        self.model = ClienteModel()
        self.view = ClienteView()

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
                self.buscar_por_cpf()
            elif opcao == "5":
                self.editar()
            elif opcao == "0":
                break
            else:
                self.view.mostrar_mensagem("Opção inválida!")

    def cadastrar(self):
        nome, cpf, endereco, email = self.view.pedir_dados_cadastro()
        sucesso, mensagem = self.model.cadastrar(nome, cpf, endereco, email)
        self.view.mostrar_mensagem(mensagem)

    def listar(self):
        clientes = self.model.listar_todos()
        self.view.listar_clientes(clientes)

    def remover(self):
        id_cli = self.view.pedir_id()
        if id_cli is None:
            return
        sucesso, mensagem = self.model.remover(id_cli)
        self.view.mostrar_mensagem(mensagem)

    def buscar_por_cpf(self):
        cpf = self.view.pedir_cpf()
        cliente = self.model.buscar_por_cpf(cpf)
        if cliente:
            self.view.mostrar_cliente(cliente)
        else:
            self.view.mostrar_mensagem("Cliente não encontrado!")

    def editar(self):
        id_cli = self.view.pedir_id()
        if id_cli is None:
            return

        cliente = self.model.buscar_por_id(id_cli)
        if not cliente:
            self.view.mostrar_mensagem("Cliente não encontrado!")
            return

        opcao = self.view.pedir_opcao_edicao()

        if opcao == 1:
            novo_nome = self.view.pedir_novo_nome()
            sucesso, mensagem = self.model.atualizar_nome(id_cli, novo_nome)
        elif opcao == 2:
            novo_email = self.view.pedir_novo_email()
            sucesso, mensagem = self.model.atualizar_email(id_cli, novo_email)
        elif opcao == 3:
            novo_endereco = self.view.pedir_novo_endereco()
            sucesso, mensagem = self.model.atualizar_endereco(id_cli, novo_endereco)
        else:
            self.view.mostrar_mensagem("Opção inválida!")
            return

        self.view.mostrar_mensagem(mensagem)
