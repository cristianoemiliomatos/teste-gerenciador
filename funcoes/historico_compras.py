import sqlite3
from pathlib import Path

banco = Path(__file__).parent.parent/ "dados"/ "dados.sqlite"
def historico():
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id, id_cliente, produto_id, valor_total, data_venda, quantidade FROM vendas
    """)
    historico = cursor.fetchall()
    for id, id_cliente, produto_id, valor_total, data_venda, quantidade in historico:
        print("-----------------------------------------------------------------------------")
        print(f"ID CLIENTE: {id_cliente} PRODUTO ID: {produto_id} VALOR TOTAL: {valor_total}")
        print(f"QUANTIDADE: {quantidade} - Data: {data_venda}")
