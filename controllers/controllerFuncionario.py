from rich import print
from rich.table import Table

from daos import DaoCargoFuncionario, DaoFuncionario
from models import (
    CargoFuncionarioNaoExiste,
    Funcionario,
    FuncionarioJaExiste,
    FuncionarioNaoExiste,
)
from utils import message


class ControllerFuncionario:
    @classmethod
    def cadastrar(cls, nome, cpf, cargo, telefone):
        try:
            cargo = DaoCargoFuncionario.buscar(cargo)
            funcionario = Funcionario(nome, cpf, cargo, telefone)
            DaoFuncionario.salvar(funcionario)
            message.verde('Funcionario cadastrado')
        except FuncionarioJaExiste:
            message.vermelha('Funcionario já existe')

    @classmethod
    def excluir(cls, funcionario):
        try:
            funcionario = DaoFuncionario.buscar(funcionario)
            message.amarela(
                f'Tem certeza que deseja excluir o funcionario "{funcionario.nome}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoFuncionario.excluir(funcionario)
                            message.verde('Funcionario excluído com sucesso.')
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except FuncionarioNaoExiste:
            message.vermelha('Funcionario não existe')

    @classmethod
    def alterar(cls, funcionario, nome, cpf, cargo, telefone):
        try:
            cargo = DaoCargoFuncionario.buscar(cargo)
            DaoFuncionario.alterar(funcionario, nome, cpf, cargo, telefone)
            message.verde('Funcionario alterado com sucesso.')
        except CargoFuncionarioNaoExiste:
            message.vermelha('Cargo funcionario não existe.')
        except FuncionarioNaoExiste:
            message.vermelha('Funcionario que deseja alterar não existe.')
        except FuncionarioJaExiste:
            message.vermelha('Funcionario para qual deseja alterar já existe.')

    @classmethod
    def listar(cls):
        lista = DaoFuncionario.ler()

        if len(lista) < 1:
            message.amarela('Não existem produtos.')
        else:
            tabela = Table(title='Funcionários', show_lines=True)
            tabela.add_column('Nome')
            tabela.add_column('Cargo')
            tabela.add_column('CPF')
            tabela.add_column('Telefone')

            for funcionario in lista:
                tabela.add_row(
                    funcionario.nome,
                    funcionario.cargo.nome,
                    funcionario.cpf,
                    funcionario.telefone,
                )
            print(tabela)
