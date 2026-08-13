import sqlite3
from pathlib import Path
def cadastrar_funcionario():
    pasta_dados = Path(__file__).parent.parent / "dados"/ "dados.sqlite"
    

    conexao = sqlite3.connect(pasta_dados)
    cursor = conexao.cursor()

    nome = input("Digite o nome do funcionario: ")
    salario = float(input("Digite o salario do funcionario: "))
    cpf = input("Digite o cpf do funcionario: ")

    cursor.execute("""
    INSERT INTO funcionarios (nome, salario, cpf) VALUES (?,?,?)
    """,(nome, salario, cpf))

    conexao.commit()
    conexao.close()

