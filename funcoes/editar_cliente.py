import sqlite3
from pathlib import Path

pasta_dados = Path(__file__).parent.parent/"dados"/"dados.sqlite"
conexao = sqlite3.connect(pasta_dados)
cursor = conexao.cursor()

def mudar_nome():
    id = input("Digite o ID do cliente: ")
    nome = input("Para que nome você quer mudar: ")
    cursor.execute("""
    UPDATE clientes SET nome = ? WHERE id = ?
    """,(nome,id))

    conexao.commit()
    conexao.close()

