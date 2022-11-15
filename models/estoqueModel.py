from .produtoModel import Produto


class Estoque:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade


class EstoqueNaoExiste(Exception):
    pass


class EstoqueJaExiste(Exception):
    pass
