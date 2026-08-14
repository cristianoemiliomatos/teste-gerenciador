import sqlite3
from pathlib import Path


class ProdutoModel:
    def __init__(self, db_path=None):
        self.db_path = db_path or Path(__file__).resolve().parent.parent / "dados" / "dados.sqlite"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL CHECK (quantidade >= 0),
                    preco REAL NOT NULL CHECK (preco > 0)
                )
            """)
            conn.commit()

    def adicionar(self, nome, quantidade, preco):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                    (nome, quantidade, preco)
                )
                conn.commit()
            return True, "Produto adicionado com sucesso!"
        except Exception as e:
            return False, f"Erro ao adicionar: {str(e)}"

    def remover(self, id_produto):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Produto removido com sucesso!"
                else:
                    return False, "Produto não encontrado!"
        except Exception as e:
            return False, f"Erro ao remover: {str(e)}"

    def listar_todos(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
                return cursor.fetchall()
        except Exception as e:
            return []

    def listar_com_total(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT nome, quantidade, preco, (preco*quantidade) as total FROM produtos")
                return cursor.fetchall()
        except Exception as e:
            return []

    def buscar_por_id(self, id_produto):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, quantidade, preco FROM produtos WHERE id = ?", (id_produto,))
                return cursor.fetchone()
        except Exception as e:
            return None

    def atualizar_quantidade(self, id_produto, nova_quantidade):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Quantidade atualizada com sucesso!"
                else:
                    return False, "Produto não encontrado!"
        except Exception as e:
            return False, f"Erro ao atualizar: {str(e)}"

    def atualizar_preco(self, id_produto, novo_preco):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (novo_preco, id_produto))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Preço atualizado com sucesso!"
                else:
                    return False, "Produto não encontrado!"
        except Exception as e:
            return False, f"Erro ao atualizar: {str(e)}"

    def comprar(self, id_produto, quantidade_comprada):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT quantidade, preco FROM produtos WHERE id = ?", (id_produto,))
                resultado = cursor.fetchone()
                
                if resultado is None:
                    return False, None, "Produto não encontrado!"
                
                quantidade_estoque, preco = resultado
                
                if quantidade_comprada > quantidade_estoque:
                    return False, None, f"Quantidade insuficiente! Disponível: {quantidade_estoque}"
                
                preco_total = preco * quantidade_comprada
                
                cursor.execute(
                    "UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?",
                    (quantidade_comprada, id_produto)
                )
                conn.commit()
                
                return True, preco_total, "Compra realizada com sucesso!"
        except Exception as e:
            return False, None, f"Erro ao comprar: {str(e)}"
