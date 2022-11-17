from rich import print
from rich.table import Table

from daos import DaoEstoque, DaoProduto
from models import Estoque, EstoqueJaExiste, EstoqueNaoExiste, ProdutoNaoExiste
from utils import message


class ControllerEstoque:
    @classmethod
    def cadastrar(cls, produto_nome, quantidade):
        try:
            DaoEstoque.buscar(produto_nome)
            message.vermelha('Estoque já existe')
        except EstoqueNaoExiste:
            try:
                produto = DaoProduto.buscar(produto_nome)

                estoque = Estoque(produto, quantidade)
                DaoEstoque.salvar(estoque)
                message.verde('Estoque cadastrado.')
            except ProdutoNaoExiste:
                message.vermelha('Produto não existe')

    @classmethod
    def excluir(cls, produto_nome):
        try:
            DaoEstoque.buscar(produto_nome)
            message.amarela(
                f'Tem certeza que deseja excluir o estoque de "{produto_nome}"?\[S]sim/\[N]não '
            )
            while True:
                decisao = input()
                if decisao in 'sSnN':
                    match decisao.lower():
                        case 's':
                            DaoEstoque.excluir(produto_nome)
                            message.verde('Estoque excluído com sucesso.')
                            break
                        case 'n':
                            message.amarela('Operação abortada.')
                            break
                else:
                    message.vermelha('valor inválido.')

        except ProdutoNaoExiste:
            message.vermelha('Produto não existe')

    @classmethod
    def alterar(cls, estoque, produto_nome, quantidade):
        try:
            produto = DaoProduto.buscar(produto_nome)
            DaoEstoque.alterar(estoque, produto, quantidade)
            message.verde('Estoque alterado com sucesso.')
        except EstoqueNaoExiste:
            message.vermelha('Estoque que deseja alterar não existe.')
        except EstoqueJaExiste:
            message.vermelha('Estoque para o qual deseja alterar já existe.')
        except ProdutoNaoExiste:
            message.vermelha('Produto não existe')

    @classmethod
    def listar(cls):
        lista = DaoEstoque.ler()

        if len(lista) < 1:
            message.amarela('Não existem estoques.')
        else:
            tabela = Table(title='Estoques', show_lines=True)
            tabela.add_column('Produto')
            tabela.add_column('Quantidade')
            for estoque in lista:
                tabela.add_row(estoque.produto.nome, str(estoque.quantidade))
            print(tabela)
