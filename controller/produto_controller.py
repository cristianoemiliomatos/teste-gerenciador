from model.produto import ProdutoModel
from view.produto_view import ProdutoView


class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()
        self.view = ProdutoView()

    def run(self):
        while True:
            self.view.mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.listar_com_total()
            elif opcao == "4":
                self.remover()
            elif opcao == "5":
                self.comprar()
            elif opcao == "6":
                self.atualizar()
            elif opcao == "0":
                break
            else:
                self.view.mostrar_mensagem("Opção inválida!")

    def adicionar(self):
        nome, quantidade, preco = self.view.pedir_dados_produto()
        if nome is None:
            return
        sucesso, mensagem = self.model.adicionar(nome, quantidade, preco)
        self.view.mostrar_mensagem(mensagem)

    def listar(self):
        produtos = self.model.listar_todos()
        self.view.listar_produtos(produtos)

    def listar_com_total(self):
        produtos = self.model.listar_com_total()
        self.view.listar_estoque_com_total(produtos)

    def remover(self):
        id_prod = self.view.pedir_id()
        if id_prod is None:
            return
        sucesso, mensagem = self.model.remover(id_prod)
        self.view.mostrar_mensagem(mensagem)

    def comprar(self):
        id_prod = self.view.pedir_id()
        if id_prod is None:
            return

        quantidade = self.view.pedir_quantidade()
        if quantidade is None:
            return

        sucesso, preco_total, mensagem = self.model.comprar(id_prod, quantidade)
        if sucesso:
            self.view.mostrar_preco_compra(preco_total)
        self.view.mostrar_mensagem(mensagem)

    def atualizar(self):
        id_prod = self.view.pedir_id()
        if id_prod is None:
            return

        produto = self.model.buscar_por_id(id_prod)
        if not produto:
            self.view.mostrar_mensagem("Produto não encontrado!")
            return

        opcao = self.view.pedir_opcao_edicao()

        if opcao == 1:
            nova_quantidade = self.view.pedir_nova_quantidade()
            if nova_quantidade is None:
                return
            sucesso, mensagem = self.model.atualizar_quantidade(id_prod, nova_quantidade)
        elif opcao == 2:
            novo_preco = self.view.pedir_novo_preco()
            if novo_preco is None:
                return
            sucesso, mensagem = self.model.atualizar_preco(id_prod, novo_preco)
        else:
            self.view.mostrar_mensagem("Opção inválida!")
            return

        self.view.mostrar_mensagem(mensagem)
