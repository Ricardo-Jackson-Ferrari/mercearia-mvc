import json
from typing import List

from models import Estoque, EstoqueJaExiste, EstoqueNaoExiste, Produto

from .DaoBase import DaoBase
from .DaoProduto import DaoProduto


class DaoEstoque(DaoBase):
    arquivo_txt: str = 'estoques.txt'

    @classmethod
    def salvar(cls, estoque: Estoque) -> None:
        try:
            cls.buscar(estoque.produto)
            raise EstoqueJaExiste
        except EstoqueNaoExiste:
            with open(cls.local_arquivo(), 'a') as arq:
                data = {
                    'produto': estoque.produto.nome,
                    'quantidade': estoque.quantidade,
                }
                arq.writelines(json.dumps(data))
                arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[Estoque]:
        try:
            with open(cls.local_arquivo(), 'r') as arq:
                estoques = arq.readlines()

            estoques = list(map(lambda x: x.replace('\n', ''), estoques))
            estoques = list(map(lambda x: json.loads(x), estoques))

            return [
                Estoque(
                    produto=DaoProduto.buscar(estoque['produto']),
                    quantidade=int(estoque['quantidade']),
                )
                for estoque in estoques
            ]
        except FileNotFoundError:
            cls.criar_arquivo()
            return cls.ler()

    @classmethod
    def buscar(cls, produto) -> Estoque:
        estoques = cls.ler()
        resultado = list(filter(lambda x: x.produto.nome == produto, estoques))
        if len(resultado):
            return resultado[0]
        raise EstoqueNaoExiste

    @classmethod
    def excluir(cls, value) -> None:
        obj = cls.buscar(value)
        lista = cls.ler()
        nova_lista = list(
            filter(lambda x: x.produto.nome != obj.produto.nome, lista)
        )

        cls.sobrepor_lista_salva(nova_lista)

    @classmethod
    def alterar(cls, estoque_produto, produto: Produto, quantidade) -> None:
        cls.buscar(estoque_produto)

        if estoque_produto != produto.nome:
            try:
                cls.buscar(produto)
                raise EstoqueJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: Estoque(produto, quantidade)
                if (x.produto.nome == produto.nome)
                else (x),
                lista,
            )
        )
        cls.sobrepor_lista_salva(nova_lista)
