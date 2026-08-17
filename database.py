import sqlite3
from pathlib import Path

pasta_dados = Path(__file__).parent / "dados"
banco = pasta_dados / "dados.sqlite"

conexao = sqlite3.connect(banco)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    salario REAL NOT NULL CHECK (salario > 0),
    cpf TEXT NOT NULL
)
""")

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

if "produto_id" not in colunas:
    cursor.execute("ALTER TABLE vendas ADD COLUMN produto_id INTEGER")
if "id_cliente" not in colunas:
    cursor.execute("ALTER TABLE vendas ADD COLUMN id_cliente INTEGER")
if "valor_total" not in colunas:
    cursor.execute("ALTER TABLE vendas ADD COLUMN valor_total REAL")
if "data_venda" not in colunas:
    cursor.execute("ALTER TABLE vendas ADD COLUMN data_venda TEXT")

conexao.commit()
conexao.close()
