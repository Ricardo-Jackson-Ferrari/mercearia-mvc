from rich import print
from rich.table import Table

from daos import DaoCliente, DaoEstoque, DaoFuncionario, DaoProduto, DaoVenda
from models import (
    ClienteNaoExiste,
    FuncionarioNaoExiste,
    ProdutoNaoExiste,
    Venda,
)
from utils import message


class EstoqueInsuficiente(Exception):
    pass


class ControllerVenda:
    @classmethod
    def cadastrar(cls, itens, vendedor, cliente):
        try:
            vendedor = DaoFuncionario.buscar(vendedor)
            cliente = DaoCliente.buscar(cliente)
            produtos = []

            for item in itens:
                estoque = DaoEstoque.buscar(item['produto'])
                if estoque.quantidade < item['quantidade']:
                    raise EstoqueInsuficiente
                data = {
                    'produto': DaoProduto.buscar(item['produto']),
                    'quantidade': item['quantidade'],
                }
                produtos.append(data)

            venda = Venda(produtos, vendedor, cliente)
            DaoVenda.salvar(venda)
            for item in produtos:
                qtd_estoque = DaoEstoque.buscar(
                    item['produto'].nome
                ).quantidade
                DaoEstoque.alterar(
                    item['produto'].nome,
                    item['produto'],
                    (qtd_estoque - item['quantidade']),
                )
            message.verde('Venda cadastrada')
            print(f'Valor total: {venda.total_venda()}')
        except FuncionarioNaoExiste:
            message.vermelha('Funcionario não existe')
        except ClienteNaoExiste:
            message.vermelha('Cliente não existe')
        except ProdutoNaoExiste:
            message.vermelha('Produto não existe')
        except EstoqueInsuficiente:
            message.amarela('Estoque do produto insuficiente')

    @classmethod
    def listar(cls):
        lista = DaoVenda.ler()

        if len(lista) < 1:
            message.amarela('Não existem produtos.')
        else:
            for venda in lista:
                print(f'Venda: {venda.total_venda()}')

            tabela = Table(title='Relatório venda produtos', show_lines=True)
            tabela.add_column('Cliente')
            tabela.add_column('Funcionario')
            tabela.add_column('Total')
            tabela.add_column('Data')

            for venda in lista:
                tabela.add_row(
                    venda.cliente.nome,
                    venda.vendedor.nome,
                    str(venda.total_venda()),
                    venda.data,
                )
            print(tabela)

    @classmethod
    def relatorio_produtos(cls):
        lista = DaoVenda.ler()
        if not len(lista):
            message.amarela('Não existem vendas para gerar relatório')
            return
        vendas = []
        for venda in lista:
            vendas += venda.itens

        relatorio = []
        for item in vendas:
            contem = bool(
                len(
                    list(
                        filter(
                            lambda x: x['produto'].nome
                            == item['produto'].nome,
                            relatorio,
                        )
                    )
                )
            )
            if not contem:
                data = {
                    'produto': item['produto'],
                    'quantidade': item['quantidade'],
                }
                relatorio.append(data)
            else:
                relatorio = list(
                    map(
                        lambda x: {
                            'produto': x['produto'],
                            'quantidade': x['quantidade'] + item['quantidade'],
                        }
                        if (x['produto'].nome == item['produto'].nome)
                        else x,
                        relatorio,
                    )
                )
        relatorio_ordenado = sorted(relatorio, key=lambda k: k['produto'].nome)

        tabela = Table(title='Relatório venda produtos', show_lines=True)
        tabela.add_column('Produto')
        tabela.add_column('Quantidade')

        for item in relatorio_ordenado:
            tabela.add_row(item['produto'].nome, str(item['quantidade']))
        print(tabela)
