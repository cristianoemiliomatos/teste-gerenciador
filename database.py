import sqlite3
from pathlib import Path

pasta_dados = Path(__file__).parent / "dados"
clientes = pasta_dados / "dados.sqlite"

conexao = sqlite3.connect(clientes)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    salario REAL NOT NULL CHECK (salario > 0),
    cpf TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()