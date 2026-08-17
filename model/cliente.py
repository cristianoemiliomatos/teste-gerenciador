import sqlite3
from pathlib import Path
from datetime import date


class ClienteModel:
    def __init__(self, db_path=None):
        self.db_path = db_path or Path(__file__).resolve().parent.parent / "dados" / "dados.sqlite"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    endereco TEXT,
                    email TEXT,
                    data_cadastro TEXT
                )
            """)
            conn.commit()

    def cadastrar(self, nome, cpf, endereco, email):
        try:
            data_cadastro = date.today().strftime("%d/%m/%Y")
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT INTO clientes (nome, cpf, endereco, email, data_cadastro) VALUES (?, ?, ?, ?, ?)",
                    (nome, cpf, endereco, email, data_cadastro)
                )
                conn.commit()
            return True, "Cliente cadastrado com sucesso!"
        except sqlite3.IntegrityError:
            return False, "Erro: CPF já cadastrado!"
        except Exception as e:
            return False, f"Erro ao cadastrar: {str(e)}"

    def remover(self, id_cliente):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Cliente removido com sucesso!"
                else:
                    return False, "Cliente não encontrado!"
        except Exception as e:
            return False, f"Erro ao remover: {str(e)}"

    def listar_todos(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, cpf, email FROM clientes")
                return cursor.fetchall()
        except Exception as e:
            return []

    def buscar_por_cpf(self, cpf):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, cpf, email, endereco FROM clientes WHERE cpf = ?", (cpf,))
                return cursor.fetchone()
        except Exception as e:
            return None

    def buscar_por_id(self, id_cliente):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, cpf, email, endereco FROM clientes WHERE id = ?", (id_cliente,))
                return cursor.fetchone()
        except Exception as e:
            return None

    def atualizar_nome(self, id_cliente, novo_nome):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", (novo_nome, id_cliente))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Nome atualizado com sucesso!"
                else:
                    return False, "Cliente não encontrado!"
        except Exception as e:
            return False, f"Erro ao atualizar: {str(e)}"

    def atualizar_email(self, id_cliente, novo_email):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Email atualizado com sucesso!"
                else:
                    return False, "Cliente não encontrado!"
        except Exception as e:
            return False, f"Erro ao atualizar: {str(e)}"

    def atualizar_endereco(self, id_cliente, novo_endereco):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE clientes SET endereco = ? WHERE id = ?", (novo_endereco, id_cliente))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Endereço atualizado com sucesso!"
                else:
                    return False, "Cliente não encontrado!"
        except Exception as e:
            return False, f"Erro ao atualizar: {str(e)}"
