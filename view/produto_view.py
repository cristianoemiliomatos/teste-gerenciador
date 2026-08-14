class ProdutoView:
    @staticmethod
    def mostrar_menu():
        print("\n" + "="*50)
        print("         GESTÃO DE PRODUTOS")
        print("="*50)
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Ver estoque com totais")
        print("4 - Remover produto")
        print("5 - Comprar produto")
        print("6 - Atualizar produto")
        print("0 - Voltar")
        print("="*50)

    @staticmethod
    def pedir_dados_produto():
        nome = input("Digite o nome do produto: ")
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
        except ValueError:
            print("Erro: Quantidade deve ser um número inteiro!")
            return None, None, None
        try:
            preco = float(input("Digite o preço do produto: "))
        except ValueError:
            print("Erro: Preço deve ser um número!")
            return None, None, None
        return nome, quantidade, preco

    @staticmethod
    def pedir_id():
        try:
            return int(input("Digite o ID do produto: "))
        except ValueError:
            print("Erro: ID deve ser um número!")
            return None

    @staticmethod
    def pedir_quantidade():
        try:
            return int(input("Digite a quantidade: "))
        except ValueError:
            print("Erro: Quantidade deve ser um número inteiro!")
            return None

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(f"\n>>> {mensagem}\n")

    @staticmethod
    def listar_produtos(produtos):
        if not produtos:
            print("\nNenhum produto encontrado!")
            return
        print("\n" + "="*80)
        print(f"{'ID':<5} {'NOME':<30} {'QUANTIDADE':<15} {'PREÇO':<15}")
        print("="*80)
        for id_prod, nome, quantidade, preco in produtos:
            print(f"{id_prod:<5} {nome:<30} {quantidade:<15} R$ {preco:.2f}")
        print("="*80 + "\n")

    @staticmethod
    def listar_estoque_com_total(produtos):
        if not produtos:
            print("\nNenhum produto encontrado!")
            return
        print("\n" + "="*100)
        print(f"{'NOME':<30} {'QUANTIDADE':<15} {'PREÇO':<15} {'TOTAL EM ESTOQUE':<20}")
        print("="*100)
        for nome, quantidade, preco, total in produtos:
            print(f"{nome:<30} {quantidade:<15} R$ {preco:<14.2f} R$ {total:.2f}")
        print("="*100 + "\n")

    @staticmethod
    def mostrar_preco_compra(preco_total):
        print(f"\n>>> Valor total da compra: R$ {preco_total:.2f}\n")

    @staticmethod
    def pedir_opcao_edicao():
        print("\nO que deseja atualizar?")
        print("1 - Quantidade")
        print("2 - Preço")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: Opção deve ser um número!")
            return None

    @staticmethod
    def pedir_nova_quantidade():
        try:
            return int(input("Digite a nova quantidade: "))
        except ValueError:
            print("Erro: Quantidade deve ser um número inteiro!")
            return None

    @staticmethod
    def pedir_novo_preco():
        try:
            return float(input("Digite o novo preço: "))
        except ValueError:
            print("Erro: Preço deve ser um número!")
            return None
