import json
from typing import List

from models import Produto, ProdutoJaExiste, ProdutoNaoExiste

from .DaoBase import DaoBase
from .DaoCategoriaProduto import DaoCategoriaProduto


class DaoProduto(DaoBase):
    arquivo_txt: str = 'produto.txt'
    parametros_busca = [
        'nome',
    ]
    classe_model_nao_existe = ProdutoNaoExiste

    @classmethod
    def salvar(cls, produto: Produto) -> None:
        try:
            cls.buscar(produto.nome)
            raise ProdutoJaExiste
        except ProdutoNaoExiste:
            with open(cls.local_arquivo(), 'a') as arq:
                data = {
                    'nome': produto.nome,
                    'categoria': produto.categoria.nome,
                    'preco': produto.preco,
                }
                arq.writelines(json.dumps(data))
                arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[Produto]:
        try:
            with open(cls.local_arquivo(), 'r') as arq:
                produtos = arq.readlines()

            produtos = list(map(lambda x: x.replace('\n', ''), produtos))
            produtos = list(map(lambda x: json.loads(x), produtos))

            return [
                Produto(
                    produto['nome'],
                    DaoCategoriaProduto.buscar(produto['categoria']),
                    float(produto['preco']),
                )
                for produto in produtos
            ]
        except FileNotFoundError:
            cls.criar_arquivo()
            return cls.ler()

    @classmethod
    def buscar(cls, value) -> Produto:
        return super().buscar(value)

    @classmethod
    def excluir(cls, produto: Produto) -> None:
        lista = cls.ler()
        nova_lista = list(filter(lambda x: x.nome != produto.nome, lista))

        cls.sobrepor_lista_salva(nova_lista)

    @classmethod
    def alterar(cls, produto, nome, categoria, preco) -> None:
        cls.buscar(produto)

        if produto != nome:
            try:
                cls.buscar(nome)
                raise ProdutoJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: Produto(nome, categoria, preco)
                if (x.nome == produto)
                else (x),
                lista,
            )
        )

        cls.sobrepor_lista_salva(nova_lista)
