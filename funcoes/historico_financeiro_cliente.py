import sqlite3
from pathlib import Path

banco = Path(__file__).parent.parent/ "dados"/ "dados.sqlite"
def historico_financeiro_pessoal():
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    id = int(input("Digite o seu ID: "))
    cursor.execute("""
    SELECT SUM(valor_total) FROM vendas WHERE id_cliente = ?
    """,(id,))
    historico = cursor.fetchall()
    for valor in historico:
        print("-----------------------------------------------------------------------------")
        print(f"Valor total gasto: {valor}")


        
