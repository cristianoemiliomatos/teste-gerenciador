import sqlite3
from pathlib import Path
def remover_funcionario():
    pasta_dados = Path(__file__).parent.parent / "dados" / "dados.sqlite"
    
    conexao = sqlite3.connect(pasta_dados)
    cursor = conexao.cursor()

    funcionario = int(input("Digite o ID do funcionario que voce quer remover: "))
    cursor.execute(
    "DELETE FROM funcionarios WHERE id = ?",
    (funcionario,)
    )
    conexao.commit()
    conexao.close()

