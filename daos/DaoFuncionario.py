import json
from typing import List

from models import Funcionario, FuncionarioJaExiste, FuncionarioNaoExiste

from .DaoBase import DaoBase
from .DaoCargoFuncionario import DaoCargoFuncionario


class DaoFuncionario(DaoBase):
    arquivo_txt: str = 'funcionarios.txt'

    @classmethod
    def salvar(cls, funcionario: Funcionario) -> None:
        try:
            DaoFuncionario.buscar(funcionario.nome)
            raise FuncionarioJaExiste
        except FuncionarioNaoExiste:
            with open(cls.local_arquivo(), 'a') as arq:
                data = {
                    'nome': funcionario.nome,
                    'cargo': funcionario.cargo.nome,
                    'cpf': funcionario.cpf,
                    'telefone': funcionario.telefone,
                }
                arq.writelines(json.dumps(data))
                arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[Funcionario]:
        try:
            with open(cls.local_arquivo(), 'r') as arq:
                funcionarios = arq.readlines()

            funcionarios = list(
                map(lambda x: x.replace('\n', ''), funcionarios)
            )
            funcionarios = list(map(lambda x: json.loads(x), funcionarios))

            return [
                Funcionario(
                    nome=funcionario['nome'],
                    cargo=DaoCargoFuncionario.buscar(funcionario['cargo']),
                    cpf=funcionario['cpf'],
                    telefone=funcionario['telefone'],
                )
                for funcionario in funcionarios
            ]
        except FileNotFoundError:
            cls.criar_arquivo()
            return cls.ler()

    @classmethod
    def buscar(cls, nome) -> Funcionario:
        funcionarios = cls.ler()
        resultado = list(filter(lambda x: x.nome == nome, funcionarios))

        if len(resultado):
            return resultado[0]
        raise FuncionarioNaoExiste

    @classmethod
    def excluir(cls, funcionario: Funcionario) -> None:
        lista = cls.ler()
        nova_lista = list(filter(lambda x: x.nome != funcionario.nome, lista))

        cls.sobrepor_lista_salva(nova_lista)

    @classmethod
    def alterar(cls, funcionario, nome, cpf, cargo, telefone) -> None:
        cls.buscar(funcionario)

        if funcionario != nome:
            try:
                cls.buscar(nome)
                raise FuncionarioJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: Funcionario(nome, cpf, cargo, telefone)
                if (x.nome == funcionario)
                else (x),
                lista,
            )
        )

        cls.sobrepor_lista_salva(nova_lista)
