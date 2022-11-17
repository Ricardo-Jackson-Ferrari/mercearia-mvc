from rich import print
from rich.table import Table

from daos import DaoCategoriaProduto
from models import (
    CategoriaProduto,
    CategoriaProdutoJaExiste,
    CategoriaProdutoNaoExiste,
)
from utils import message


class ControllerCategoriaProduto:
    @classmethod
    def cadastrar(cls, categoria):
        try:
            DaoCategoriaProduto.salvar(CategoriaProduto(categoria))
            message.verde('Categoria produto cadastrada')
        except CategoriaProdutoJaExiste:
            message.vermelha('Categoria produto já existe')

    @classmethod
    def excluir(cls, categoria):
        try:
            DaoCategoriaProduto.buscar(categoria)
            message.amarela(
                f'Tem certeza que deseja excluir a categoria produto "{categoria}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoCategoriaProduto.excluir(categoria)
                            message.verde(
                                'Categoria produto excluída com sucesso!'
                            )
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except CategoriaProdutoNaoExiste:
            message.vermelha('Categoria produto não existe')

    @classmethod
    def alterar(cls, categoria, nome):
        try:
            DaoCategoriaProduto.alterar(categoria, nome)
            message.verde('Categoria produto alterada com sucesso.')
        except CategoriaProdutoNaoExiste:
            message.vermelha(
                'Categoria produto que deseja alterar não existe.'
            )
        except CategoriaProdutoJaExiste:
            message.vermelha(
                'Categoria produto para qual deseja alterar já existe.'
            )

    @classmethod
    def listar(cls):
        lista = DaoCategoriaProduto.ler()

        if len(lista) < 1:
            message.amarela('Não existem categorias.')
        else:
            tabela = Table(title='Categorias', show_lines=True)
            tabela.add_column('Categoria')

            for categoria in lista:
                tabela.add_row(categoria.nome)
            print(tabela)
