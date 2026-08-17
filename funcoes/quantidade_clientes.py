import sqlite3
from pathlib import Path

banco = Path(__file__).parent.parent / "dados" / "dados.sqlite"
conexao = sqlite3.connect(banco)
cursor = conexao.cursor()

cursor.execute("""
SELECT nome,cpf FROM clientes
""")
relatorio = cursor.fetchall()

for nome,cpf in relatorio:
    print(f"NOME - [{nome}] CPF - [{cpf}]")