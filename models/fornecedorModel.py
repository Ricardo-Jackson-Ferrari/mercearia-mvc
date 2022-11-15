from .categoriaFornecedorModel import CategoriaFornecedor


class Fornecedor:
    def __init__(
        self,
        nome: str,
        cnpj: str,
        telefone: str,
        categoria: CategoriaFornecedor,
    ) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria


class FornecedorNaoExiste(Exception):
    pass


class FornecedorJaExiste(Exception):
    pass
