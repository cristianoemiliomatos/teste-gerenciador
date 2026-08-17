import sqlite3
from pathlib import Path

banco = Path(__file__).parent.parent/ "dados"/ "dados.sqlite"
def historico_cliente():
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    id = int(input("Digite o seu ID: "))
    cursor.execute("""
    SELECT * FROM vendas WHERE id_cliente = ?""", (id,))
    historico = cursor.fetchall()
    for id, id_cliente, produto_id, valor_total, data_venda, quantidade in historico:
            print("-----------------------------------------------------------------------------")
            print(f"ID CLIENTE: {id_cliente} PRODUTO ID: {produto_id} VALOR TOTAL: {valor_total}")
            print(f"QUANTIDADE: {quantidade} - Data: {data_venda}")

    

