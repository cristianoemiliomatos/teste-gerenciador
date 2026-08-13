from dataclasses import dataclass, field
import sqlite3
from pathlib import Path
from datetime import date


@dataclass
class Cadastro:
    nome: str
    cpf: str
    endereco: str
    email: str
    data_cadastro: str = field(default_factory=lambda: date.today().strftime("%d/%m/%Y"))

    def cadastrar(self, db_path: Path = None):
        db_path = db_path or Path(__file__).resolve().parent.parent / "dados" / "dados.sqlite"
        db_path.parent.mkdir(parents=True, exist_ok=True)

        with sqlite3.connect(db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    endereco TEXT,
                    email TEXT,
                    data_cadastro TEXT
                )
            """)
            conn.execute(
                "INSERT INTO clientes (nome, cpf, endereco, email, data_cadastro) VALUES (?, ?, ?, ?, ?)",
                (self.nome, self.cpf, self.endereco, self.email, self.data_cadastro)
            )
            conn.commit()


if __name__ == "__main__":
    nome = input("Nome: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    email = input("Email: ")

    cliente = Cadastro(nome, cpf, endereco, email)
    cliente.cadastrar()
    print("Cadastrado!")