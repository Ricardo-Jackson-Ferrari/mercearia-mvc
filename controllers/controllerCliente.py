from rich import print
from rich.table import Table

from daos import DaoCliente
from models import Cliente, ClienteJaExiste, ClienteNaoExiste
from utils import message


class ControllerCliente:
    @classmethod
    def cadastrar(cls, nome: str, cpf: str, telefone: str):
        try:
            cliente = Cliente(nome, cpf, telefone)
            DaoCliente.salvar(cliente)
            message.verde('Cliente cadastrado')
        except ClienteJaExiste:
            message.vermelha('Cliente já existe')

    @classmethod
    def excluir(cls, cliente: str):
        try:
            cliente = DaoCliente.buscar(cliente)
            message.amarela(
                f'Tem certeza que deseja excluir o cliente "{cliente.nome}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoCliente.excluir(cliente)
                            message.verde('Cliente excluído com sucesso!')
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except ClienteNaoExiste:
            message.vermelha('Cliente não existe')

    @classmethod
    def alterar(cls, cliente: str, nome: str, cpf: str, telefone: str):
        try:
            DaoCliente.alterar(cliente, nome, cpf, telefone)
            message.verde('Cliente alterado com sucesso.')
        except ClienteNaoExiste:
            message.vermelha('Cliente que deseja alterar não existe.')
        except ClienteJaExiste:
            message.vermelha('Cliente para qual deseja alterar já existe.')

    @classmethod
    def listar(cls):
        lista = DaoCliente.ler()

        if len(lista) < 1:
            message.amarela('Não existem produtos.')
        else:
            tabela = Table(title='Clientes', show_lines=True)
            tabela.add_column('Nome')
            tabela.add_column('CPF')
            tabela.add_column('Telefone')

            for cliente in lista:
                tabela.add_row(cliente.nome, cliente.cpf, cliente.telefone)
            print(tabela)
