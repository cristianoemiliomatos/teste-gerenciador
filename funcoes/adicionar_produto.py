import sqlite3
from pathlib import Path

def adicionar_produto():
    arquivo = Path(__file__).parent.parent/"dados"/"dados.sqlite"

    conexao = sqlite3.connect(arquivo)
    cursor = conexao.cursor()

    nome = input("Digite o nome do produto: ")

    try:
        quantidade = int(input("Digite a quantidade do produto: "))
    except ValueError:
        print("Erro: A quantidade deve ser um número inteiro válido.")
        exit()

    try:
        preco = float(input("Digite o valor do produto: "))
    except ValueError:
        print("Erro: O preço deve ser um número válido.")
        exit()



    cursor.execute("""
    INSERT INTO produtos (nome, quantidade, preco) VALUES (?,?,?)
    """,(nome, quantidade, preco))

    conexao.commit()
    conexao.close()