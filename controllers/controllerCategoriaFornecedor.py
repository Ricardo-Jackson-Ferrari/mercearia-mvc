from rich import print
from rich.table import Table

from daos import DaoCategoriaFornecedor
from models import (
    CategoriaFornecedor,
    CategoriaFornecedorJaExiste,
    CategoriaFornecedorNaoExiste,
)
from utils import message


class ControllerCategoriaFornecedor:
    @classmethod
    def cadastrar(cls, categoria: str):
        try:
            DaoCategoriaFornecedor.salvar(CategoriaFornecedor(categoria))
            message.verde('Categoria fornecedor cadastrada')
        except CategoriaFornecedorJaExiste:
            message.vermelha('Categoria fornecedor já existe')

    @classmethod
    def excluir(cls, categoria: str):
        try:
            DaoCategoriaFornecedor.buscar(categoria)
            message.amarela(
                f'Tem certeza que deseja excluir a categoria fornecedor "{categoria}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoCategoriaFornecedor.excluir(categoria)
                            message.verde(
                                'Categoria fornecedor excluída com sucesso!'
                            )
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except CategoriaFornecedorNaoExiste:
            message.vermelha('Categoria fornecedor não existe')

    @classmethod
    def alterar(cls, categoria: str, nome: str):
        try:
            DaoCategoriaFornecedor.alterar(categoria, nome)
            message.verde('Categoria fornecedor alterada com sucesso.')
        except CategoriaFornecedorNaoExiste:
            message.vermelha(
                'Categoria fornecedor que deseja alterar não existe.'
            )
        except CategoriaFornecedorJaExiste:
            message.vermelha(
                'Categoria fornecedor para qual deseja alterar já existe.'
            )

    @classmethod
    def listar(cls):
        lista = DaoCategoriaFornecedor.ler()

        if len(lista) < 1:
            message.amarela('Não existem categorias.')
        else:
            tabela = Table(title='Categorias fornecedor', show_lines=True)
            tabela.add_column('Categoria')
            for categoria in lista:
                tabela.add_row(categoria.nome)
            print(tabela)
