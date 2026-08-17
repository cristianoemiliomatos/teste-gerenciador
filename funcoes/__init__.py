"""Ponto único de importação das funções do sistema."""

from .historico_compras import historico
from .historico_financeiro import financeiro
from .listar_funcionario import listar_funcionarios
from .remover_funcionario import remover_funcionario


def adicionar_produto(*args, **kwargs):
    from gestao_produtos.adicionar_produto import adicionar_produto as funcao
    return funcao(*args, **kwargs)


def comprar(*args, **kwargs):
    from gestao_produtos.comprar_produto import comprar as funcao
    return funcao(*args, **kwargs)


def estoque(*args, **kwargs):
    from gestao_produtos.estoque import estoque as funcao
    return funcao(*args, **kwargs)


def Cadastro(*args, **kwargs):
    from gestao_clientes.cadastrar_cliente import Cadastro as classe
    return classe(*args, **kwargs)


def cadastrar_funcionario(*args, **kwargs):
    from gestao_funcionarios.cadastrar_funcionario import cadastrar_funcionario as funcao
    return funcao(*args, **kwargs)


def editar_cliente(*args, **kwargs):
    from gestao_clientes.editar_cliente import mudar_nome
    return mudar_nome(*args, **kwargs)


def quantidade_clientes(*args, **kwargs):
    from gestao_clientes.quantidade_clientes import listar_clientes
    return listar_clientes(*args, **kwargs)


__all__ = [
    "historico", "financeiro", "listar_funcionarios", "remover_funcionario",
    "adicionar_produto", "comprar", "estoque", "Cadastro",
    "cadastrar_funcionario", "editar_cliente", "quantidade_clientes",
]
