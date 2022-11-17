from rich import print
from rich.table import Table

from daos import DaoCargoFuncionario
from models import (
    CargoFuncionario,
    CargoFuncionarioJaExiste,
    CargoFuncionarioNaoExiste,
)
from utils import message


class ControllerCargoFuncionario:
    @classmethod
    def cadastrar(cls, cargo):
        try:
            DaoCargoFuncionario.salvar(CargoFuncionario(cargo))
            message.verde('Cargo funcionario cadastrado!')
        except CargoFuncionarioJaExiste:
            message.vermelha('Cargo funcionario já existe')

    @classmethod
    def excluir(cls, cargo):
        try:
            cargo = DaoCargoFuncionario.buscar(cargo)
            message.amarela(
                f'Tem certeza que deseja excluir o cargo funcionario "{cargo.nome}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoCargoFuncionario.excluir(cargo)
                            message.verde(
                                'Categoria produto excluída com sucesso!'
                            )
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except CargoFuncionarioNaoExiste:
            message.vermelha('Categoria produto não existe')

    @classmethod
    def alterar(cls, cargo: str, nome: str):
        try:
            DaoCargoFuncionario.alterar(cargo, nome)
            message.verde('Categoria produto alterada com sucesso.')
        except CargoFuncionarioNaoExiste:
            message.vermelha(
                'Categoria produto que deseja alterar não existe.'
            )
        except CargoFuncionarioJaExiste:
            message.vermelha(
                'Categoria produto para qual deseja alterar já existe.'
            )

    @classmethod
    def listar(cls):
        lista = DaoCargoFuncionario.ler()

        if len(lista) < 1:
            message.amarela('Não existem cargos funcionario.')
        else:
            tabela = Table(title='Cargos funcionário', show_lines=True)
            tabela.add_column('Cargo')
            for cargo in lista:
                tabela.add_row(cargo.nome)
            print(tabela)
