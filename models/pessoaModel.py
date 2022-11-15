class Pessoa:
    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


class PessoaNaoExiste(Exception):
    pass


class PessoaJaExiste(Exception):
    pass
