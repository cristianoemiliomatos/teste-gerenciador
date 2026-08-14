import sqlite3
from pathlib import Path

def comprar():
    while True:
        print("1 - Quero comprar")
        print("2 - Não quero comprar")
        deseja_comprar = int(input("Deseja comprar um produto ? : "))
        if deseja_comprar == 2:
            break
        if deseja_comprar == 1:
            banco = Path(__file__).parent.parent / "dados" / "dados.sqlite"
            conexao = sqlite3.connect(banco)
            cursor = conexao.cursor()

            cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
            produtos = cursor.fetchall()
            for id, nome, quantidade, preco in produtos:
                print(f"ID: {id} - PRODUTO - {nome} - Em estoque - {quantidade}")

            try:
                escolha = int(input("Digite o ID do produto que você quer: "))
                quantidade1 = int(input("Digite a quantidade que você quer: "))
            except ValueError:
                print("Valor inválido !!!")
                return

            cursor.execute("SELECT quantidade, preco FROM produtos WHERE id = ?", (escolha,))
            resultado = cursor.fetchone()
            if resultado is None:
                print("Produto não encontrado !!!")
                return

            quantidade_estoque, preco = resultado

            if quantidade1 <= 0:
                print("Quantidade não pode ser 0 ou menor !!!")
                return
            if quantidade1 > quantidade_estoque:
                print("Não temos essa quantidade no estoque")
                return

            preco_compra = preco * quantidade1
            print(f"\n\nO valor da sua compra fica em {preco_compra}")



            cursor.execute(
                "UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?",
                (quantidade1, escolha)
            )
            conexao.commit()
            cursor.close()
            conexao.close()


