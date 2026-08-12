import sqlite3
from pathlib import Path

pasta_dados = Path(__file__).parent / "dados"
clientes = pasta_dados / "dados.sqlite"

conexao = sqlite3.connect(clientes)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    produto TEXT NOT NULL,
    valor REAL NOT NULL CHECK (valor > 0),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
)
""")

conexao.commit()
conexao.close()