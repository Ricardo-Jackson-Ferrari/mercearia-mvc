from .pessoaModel import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        super().__init__(nome, cpf, telefone)


class ClienteNaoExiste(Exception):
    pass


class ClienteJaExiste(Exception):
    pass
