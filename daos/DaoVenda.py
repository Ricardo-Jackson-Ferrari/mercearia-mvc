import json
from typing import List

from models import Venda, VendaNaoExiste

from .DaoBase import DaoBase
from .DaoCliente import DaoCliente
from .DaoFuncionario import DaoFuncionario
from .DaoProduto import DaoProduto


class DaoVenda(DaoBase):
    arquivo_txt: str = 'vendas.txt'

    @classmethod
    def salvar(cls, venda: Venda) -> None:
        DaoFuncionario.buscar(venda.vendedor.nome)
        DaoCliente.buscar(venda.cliente.nome)
        for item in venda.itens:
            DaoProduto.buscar(item['produto'].nome)
        try:
            with open(cls.local_arquivo(), 'a') as arq:
                itens = [
                    {
                        'produto': {
                            'nome': item['produto'].nome,
                            'preco': item['produto'].preco,
                        },
                        'quantidade': item['quantidade'],
                    }
                    for item in venda.itens
                ]

                data = {
                    'itens': itens,
                    'vendedor': venda.vendedor.nome,
                    'cliente': venda.cliente.nome,
                    'data': venda.data,
                }

                data_json = json.dumps(data)

                arq.writelines(data_json)
                arq.writelines('\n')
        except FileNotFoundError:
            cls.criar_arquivo()
            cls.salvar(venda)

    @classmethod
    def ler(cls) -> List[Venda]:
        try:
            with open(cls.local_arquivo(), 'r') as arq:
                vendas = arq.readlines()

            vendas = list(map(lambda x: x.replace('\n', ''), vendas))
            vendas = list(map(lambda x: json.loads(x), vendas))

            listagem = []

            # return [
            #     Venda(
            #         itens=venda['itens'],
            #         vendedor=DaoFuncionario.buscar(venda['vendedor']),
            #         cliente=DaoCliente.buscar(venda['cliente']),
            #         data=venda['data'],
            #     )
            #     for venda in vendas
            # ]

            for venda in vendas:
                produtos = []
                for item in venda['itens']:
                    data = {
                        'produto': DaoProduto.buscar(item['produto']['nome']),
                        'quantidade': item['quantidade'],
                    }
                    produtos.append(data)
                venda = Venda(
                    itens=produtos,
                    vendedor=DaoFuncionario.buscar(venda['vendedor']),
                    cliente=DaoCliente.buscar(venda['cliente']),
                    data=venda['data'],
                )
                listagem.append(venda)

            return listagem
        except FileNotFoundError:
            cls.criar_arquivo()
            return cls.ler()

    @classmethod
    def buscar(cls, id) -> Venda:
        ordem_vendas = cls.ler()
        resultado = list(filter(lambda x: x.id == id, ordem_vendas))

        if len(resultado):
            return resultado[0]
        else:
            raise VendaNaoExiste
