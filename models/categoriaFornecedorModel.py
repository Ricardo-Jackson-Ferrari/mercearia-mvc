class CategoriaFornecedor:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class CategoriaFornecedorNaoExiste(Exception):
    pass


class CategoriaFornecedorJaExiste(Exception):
    pass
