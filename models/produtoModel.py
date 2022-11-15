from .categoriaProduto import CategoriaProduto


class ProdutoNaoExiste(Exception):
    pass


class ProdutoJaExiste(Exception):
    pass


class Produto:
    def __init__(
        self, nome: str, categoria: CategoriaProduto, preco: float
    ) -> None:
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
