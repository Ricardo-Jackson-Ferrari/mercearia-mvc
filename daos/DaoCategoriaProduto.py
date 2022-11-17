import json
from typing import List

from models import (
    CategoriaProduto,
    CategoriaProdutoJaExiste,
    CategoriaProdutoNaoExiste,
)

from .DaoBase import DaoBase


class DaoCategoriaProduto(DaoBase):
    arquivo_txt = 'categoria_produto.txt'
    parametros_busca = [
        'nome',
    ]
    classe_model_nao_existe = CategoriaProdutoNaoExiste

    @classmethod
    def salvar(cls, categoria_produto: CategoriaProduto) -> None:
        try:
            cls.buscar(categoria_produto.nome)
            raise CategoriaProdutoJaExiste
        except CategoriaProdutoNaoExiste:
            with open(cls.local_arquivo(), 'a') as arq:
                data = {
                    'nome': categoria_produto.nome,
                }
                arq.writelines(json.dumps(data))
                arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[CategoriaProduto]:
        try:
            with open(cls.local_arquivo(), 'r') as arq:
                categorias = arq.readlines()

            categorias = list(map(lambda x: x.replace('\n', ''), categorias))
            categorias = list(map(lambda x: json.loads(x), categorias))

            return [
                CategoriaProduto(categoria['nome']) for categoria in categorias
            ]
        except FileNotFoundError:
            cls.criar_arquivo()
            return cls.ler()

    @classmethod
    def buscar(cls, value) -> CategoriaProduto:
        return super().buscar(value)

    @classmethod
    def excluir(cls, value) -> None:
        obj = cls.buscar(value)
        lista = cls.ler()
        nova_lista = list(filter(lambda x: x.nome != obj.nome, lista))

        cls.sobrepor_lista_salva(nova_lista)

    @classmethod
    def alterar(cls, categoria, nome) -> None:
        cls.buscar(categoria)

        if categoria != nome:
            try:
                DaoCategoriaProduto.buscar(nome)
                raise CategoriaProdutoJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: CategoriaProduto(nome)
                if (x.nome == categoria)
                else (x),
                lista,
            )
        )

        cls.sobrepor_lista_salva(nova_lista)
