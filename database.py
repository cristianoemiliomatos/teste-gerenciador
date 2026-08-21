import sqlite3
from pathlib import Path


def inicializar_banco():
    pasta_dados = Path(__file__).resolve().parent / "dados"
    pasta_dados.mkdir(parents=True, exist_ok=True)

    banco = pasta_dados / "dados.sqlite"
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            salario REAL NOT NULL CHECK (salario > 0),
            cpf TEXT NOT NULL UNIQUE
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            endereco TEXT,
            email TEXT,
            data_cadastro TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL CHECK (quantidade >= 0),
            preco REAL NOT NULL CHECK (preco > 0)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER,
            produto_id INTEGER,
            quantidade INTEGER,
            valor_total REAL,
            data_venda TEXT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
        """
    )

    conexao.commit()
    conexao.close()


inicializar_banco()