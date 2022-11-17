import json
from typing import List

from models import (
    CargoFuncionario,
    CargoFuncionarioJaExiste,
    CargoFuncionarioNaoExiste,
)

from .DaoBase import DaoBase


class DaoCargoFuncionario(DaoBase):
    arquivo_txt = 'cargo_funcionario.txt'

    @classmethod
    def salvar(cls, cargo: CargoFuncionario) -> None:
        try:
            cls.buscar(cargo.nome)
            raise CargoFuncionarioJaExiste
        except CargoFuncionarioNaoExiste:
            with open(cls.local_arquivo(), 'a') as arq:
                data = {
                    'nome': cargo.nome,
                }
                arq.writelines(json.dumps(data))
                arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[CargoFuncionario]:
        try:
            with open(cls.local_arquivo(), 'r') as arq:
                cargos = arq.readlines()

            cargos = list(map(lambda x: x.replace('\n', ''), cargos))
            cargos = list(map(lambda x: json.loads(x), cargos))

            return [CargoFuncionario(cargo['nome']) for cargo in cargos]
        except FileNotFoundError:
            cls.criar_arquivo()
            return cls.ler()

    @classmethod
    def buscar(cls, nome: str) -> CargoFuncionario:
        cargos = cls.ler()
        resultado = list(filter(lambda x: x.nome == nome, cargos))

        if len(resultado):
            return resultado[0]
        raise CargoFuncionarioNaoExiste

    @classmethod
    def excluir(cls, cargo: CargoFuncionario) -> None:
        lista = cls.ler()
        nova_lista = list(filter(lambda x: x.nome != cargo.nome, lista))

        cls.sobrepor_lista_salva(nova_lista)

    @classmethod
    def alterar(cls, cargo, nome) -> None:
        cls.buscar(cargo)

        if cargo != nome:
            try:
                cls.buscar(nome)
                raise CargoFuncionarioJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: CargoFuncionario(nome) if (x.nome == cargo) else (x),
                lista,
            )
        )

        cls.sobrepor_lista_salva(nova_lista)
