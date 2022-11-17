from rich import print
from rich.table import Table

from daos import DaoCategoriaProduto, DaoProduto
from models import (
    CategoriaProdutoNaoExiste,
    Produto,
    ProdutoJaExiste,
    ProdutoNaoExiste,
)
from utils import message


class ControllerProduto:
    @classmethod
    def cadastrar(cls, nome: str, categoria_nome: str, preco: float):
        try:
            categoria = DaoCategoriaProduto.buscar(categoria_nome)
            produto = Produto(nome, categoria, preco)
            DaoProduto.salvar(produto)
            message.verde('Produto cadastrada')
        except CategoriaProdutoNaoExiste:
            message.vermelha('Categoria produto não existe')
        except ProdutoJaExiste:
            message.vermelha('Produto já existe')

    @classmethod
    def excluir(cls, produto: str):
        try:
            produto = DaoProduto.buscar(produto)
            message.amarela(
                f'Tem certeza que deseja excluir o produto "{produto.nome}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoProduto.excluir(produto)
                            message.verde('Produto excluído com sucesso.')
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except ProdutoNaoExiste:
            message.vermelha('Produto não existe')

    @classmethod
    def alterar(cls, produto: str, nome: str, categoria: str, preco: float):
        try:
            categoria = DaoCategoriaProduto.buscar(categoria)
            DaoProduto.alterar(produto, nome, categoria, preco)
            message.verde('Produto alterado com sucesso.')
        except ProdutoNaoExiste:
            message.vermelha('Produto que deseja alterar não existe.')
        except ProdutoJaExiste:
            message.vermelha('Produto para qual deseja alterar já existe.')
        except CategoriaProdutoNaoExiste:
            message.vermelha('Categoria produto não existe')

    @classmethod
    def listar(cls):
        lista = DaoProduto.ler()

        if len(lista) < 1:
            message.amarela('Não existem produtos.')
        else:
            tabela = Table(title='Produtos', show_lines=True)
            tabela.add_column('Produto')
            tabela.add_column('Categoria')
            tabela.add_column('Preço')

            for produto in lista:
                tabela.add_row(
                    produto.nome, produto.categoria.nome, str(produto.preco)
                )
            print(tabela)
