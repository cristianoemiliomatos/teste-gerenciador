import sqlite3
from pathlib import Path
from datetime import datetime

def comprar(id_cliente=None):
    
    if id_cliente is None:
        try:
            id_cliente = int(input("Digite o ID do cliente: "))
        except ValueError:
            print("ID do cliente inválido !!!")
            return

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

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER,
                    produto_id INTEGER,
                    quantidade INTEGER,
                    valor_total REAL,
                    data_venda TEXT
                )
            """)

            colunas = [coluna[1] for coluna in cursor.execute("PRAGMA table_info(vendas)")]
            if "id_cliente" not in colunas:
                cursor.execute("ALTER TABLE vendas ADD COLUMN id_cliente INTEGER")
            if "produto_id" not in colunas:
                cursor.execute("ALTER TABLE vendas ADD COLUMN produto_id INTEGER")
            if "quantidade" not in colunas:
                cursor.execute("ALTER TABLE vendas ADD COLUMN quantidade INTEGER")
            if "valor_total" not in colunas:
                cursor.execute("ALTER TABLE vendas ADD COLUMN valor_total REAL")
            if "data_venda" not in colunas:
                cursor.execute("ALTER TABLE vendas ADD COLUMN data_venda TEXT")

            cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
            produtos = cursor.fetchall()

            cursor.execute("SELECT 1 FROM clientes WHERE id = ?", (id_cliente,))
            if cursor.fetchone() is None:
                print("Cliente não encontrado !!!")
                conexao.close()
                return

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

            cursor.execute("""
                INSERT INTO vendas
                (id_cliente, produto_id, quantidade, valor_total, data_venda)
                VALUES (?, ?, ?, ?, ?)
            """, (id_cliente, escolha, quantidade1, preco_compra,
                datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            conexao.commit()
            cursor.close()
            conexao.close()

if __name__ == "__main__":
    comprar()
