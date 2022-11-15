from .cargoFuncionarioModel import CargoFuncionario
from .pessoaModel import Pessoa


class Funcionario(Pessoa):
    def __init__(
        self,
        nome: str,
        cpf: str,
        cargo: CargoFuncionario,
        telefone: str,
    ) -> None:
        super().__init__(nome, cpf, telefone)
        self.cargo = cargo


class FuncionarioNaoExiste(Exception):
    pass


class FuncionarioJaExiste(Exception):
    pass
