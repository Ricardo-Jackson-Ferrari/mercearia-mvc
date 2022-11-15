class CargoFuncionario:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class CargoFuncionarioNaoExiste(Exception):
    pass


class CargoFuncionarioJaExiste(Exception):
    pass
