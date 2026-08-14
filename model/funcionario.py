import sqlite3
from pathlib import Path


class FuncionarioModel:
    def __init__(self, db_path=None):
        self.db_path = db_path or Path(__file__).resolve().parent.parent / "dados" / "dados.sqlite"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS funcionarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    salario REAL NOT NULL CHECK (salario > 0),
                    cpf TEXT NOT NULL
                )
            """)
            conn.commit()

    def cadastrar(self, nome, salario, cpf):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT INTO funcionarios (nome, salario, cpf) VALUES (?, ?, ?)",
                    (nome, salario, cpf)
                )
                conn.commit()
            return True, "Funcionário cadastrado com sucesso!"
        except Exception as e:
            return False, f"Erro ao cadastrar: {str(e)}"

    def remover(self, id_funcionario):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario,))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Funcionário removido com sucesso!"
                else:
                    return False, "Funcionário não encontrado!"
        except Exception as e:
            return False, f"Erro ao remover: {str(e)}"

    def listar_todos(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, cpf, salario FROM funcionarios")
                return cursor.fetchall()
        except Exception as e:
            return []

    def buscar_por_id(self, id_funcionario):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, cpf, salario FROM funcionarios WHERE id = ?", (id_funcionario,))
                return cursor.fetchone()
        except Exception as e:
            return None

    def atualizar(self, id_funcionario, nome=None, salario=None, cpf=None):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                if nome:
                    cursor.execute("UPDATE funcionarios SET nome = ? WHERE id = ?", (nome, id_funcionario))
                if salario:
                    cursor.execute("UPDATE funcionarios SET salario = ? WHERE id = ?", (salario, id_funcionario))
                if cpf:
                    cursor.execute("UPDATE funcionarios SET cpf = ? WHERE id = ?", (cpf, id_funcionario))
                conn.commit()
            return True, "Funcionário atualizado com sucesso!"
        except Exception as e:
            return False, f"Erro ao atualizar: {str(e)}"
