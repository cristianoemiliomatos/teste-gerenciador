import sqlite3
from pathlib import Path

banco = Path(__file__).parent.parent / "dados" / "dados.sqlite"
conexao = sqlite3.connect(banco)
cursor = conexao.cursor()

def estoque():
    cursor.execute("""
    SELECT nome, quantidade, preco, (preco*quantidade) as total FROM produtos

    """)
    relatorio = cursor.fetchall()

    for nome, quantidade, preco, total in relatorio:
        print(f"""
    -------------------------------------------------------------------------
    PRODUTO [{nome}] - QUANTIDADE - [{quantidade}] - PREÇO [{preco}]
    VALOR TOTAL EM PRODUTO [{total}]
    """)