import sqlite3
from pathlib import Path

banco = Path(__file__).parent.parent/ "dados"/ "dados.sqlite"
def financeiro():
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT SUM(valor_total)  FROM vendas
    """)
    resultado = cursor.fetchone()
    total = resultado[0]
    print(f"Valor total em vendas: {total}")
       

if __name__ == "__main__":
    financeiro()
