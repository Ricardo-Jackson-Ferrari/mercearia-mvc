class CategoriaProduto:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class CategoriaProdutoNaoExiste(Exception):
    pass


class CategoriaProdutoJaExiste(Exception):
    pass
