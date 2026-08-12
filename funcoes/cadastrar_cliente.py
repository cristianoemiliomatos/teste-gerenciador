from dataclasses import dataclass
import sqlite3
from pathlib import Path
import datetime
@dataclass
class Cadastro:
    nome: str
    cpf: str
    endereco: str
    email:str
    data_cadastro: str


    def cadastrar(self):
        pasta_dados = Path(__file__).resolve().parent.parent / "dados"
        clientes = pasta_dados / "dados.sqlite"

        conexao = sqlite3.connect(clientes)
        cursor = conexao.cursor()

        cursor.execute("""
       INSERT INTO clientes (nome, cpf, endereco, email, data_cadastro) VALUES (?,?,?,?,?)
        """, (self.nome, self.cpf, self.endereco, self.email, self.data_cadastro))

        conexao.commit()
        conexao.close()


nome = input("Digite o seu nome: ")
cpf = input("Digite seu cpf: ")
endereco = input("Digite seu endereço")
email = input("Digite seu email: ")
hoje = datetime.date.today()
data_cadastro = hoje.strftime("%d/%m/%Y")


c = Cadastro("Cristiano", "12345678910", "rua joao", "cris@gmail.com", "12/02/2026")
c.cadastrar()

