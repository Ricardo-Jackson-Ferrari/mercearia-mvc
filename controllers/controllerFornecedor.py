from rich import print
from rich.table import Table

from daos import DaoCategoriaFornecedor, DaoFornecedor
from models import (
    CategoriaFornecedorNaoExiste,
    Fornecedor,
    FornecedorJaExiste,
    FornecedorNaoExiste,
)
from utils import message


class ControllerFornecedor:
    @classmethod
    def cadastrar(cls, nome, cnpj, categoria, telefone):
        try:
            categoria = DaoCategoriaFornecedor.buscar(categoria)
            fornecedor = Fornecedor(
                nome=nome, cnpj=cnpj, categoria=categoria, telefone=telefone
            )
            DaoFornecedor.salvar(fornecedor)
            message.verde('Fornecedor cadastrado.')
        except CategoriaFornecedorNaoExiste:
            message.vermelha('Categoria fornecedor não existe.')
        except FornecedorJaExiste:
            message.vermelha('Fornecedor já existe.')

    @classmethod
    def excluir(cls, funcionario):
        try:
            funcionario = DaoFornecedor.buscar(funcionario)
            message.amarela(
                f'Tem certeza que deseja excluir o funcionario "{funcionario.nome}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoFornecedor.excluir(funcionario)
                            message.verde('Funcionario excluído com sucesso.')
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except FornecedorNaoExiste:
            message.vermelha('Funcionario não existe')

    @classmethod
    def alterar(cls, fornecedor, nome, cnpj, categoria, telefone):
        try:
            categoria = DaoCategoriaFornecedor.buscar(categoria)
            DaoFornecedor.alterar(fornecedor, nome, cnpj, telefone, categoria)
            message.verde('Funcionario alterado com sucesso.')
        except CategoriaFornecedorNaoExiste:
            message.vermelha('Cargo funcionario não existe.')
        except FornecedorNaoExiste:
            message.vermelha('Funcionario que deseja alterar não existe.')
        except FornecedorJaExiste:
            message.vermelha('Funcionario para qual deseja alterar já existe.')

    @classmethod
    def listar(cls):
        lista = DaoFornecedor.ler()

        if len(lista) < 1:
            message.amarela('Não existem produtos.')
        else:
            tabela = Table(title='Fornecedores')
            tabela.add_column('Fornecedor')
            tabela.add_column('Cnpj')
            tabela.add_column('Categoria')
            tabela.add_column('Telefone')
            for f in lista:
                tabela.add_row(f.nome, f.cnpj, f.categoria.nome, f.telefone)
            print(tabela)
