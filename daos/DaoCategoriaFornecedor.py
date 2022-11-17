import json
from typing import List

from models import (
    CategoriaFornecedor,
    CategoriaFornecedorJaExiste,
    CategoriaFornecedorNaoExiste,
)

from .DaoBase import DaoBase


class DaoCategoriaFornecedor(DaoBase):
    arquivo_txt: str = 'categoria_fornecedor.txt'

    @classmethod
    def salvar(cls, categoria_fornecedor: CategoriaFornecedor) -> None:
        with open(cls.local_arquivo(), 'a') as arq:
            data = {
                'nome': categoria_fornecedor.nome,
            }
            arq.writelines(json.dumps(data))
            arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[CategoriaFornecedor]:
        with open(cls.local_arquivo(), 'r') as arq:
            fornecedores = arq.readlines()

        fornecedores = map(lambda x: x.replace('\n', ''), fornecedores)
        fornecedores = map(lambda x: json.loads(x), fornecedores)
        return [
            CategoriaFornecedor(fornecedor['nome'])
            for fornecedor in fornecedores
        ]

    @classmethod
    def buscar(cls, nome: str) -> CategoriaFornecedor:
        categorias = cls.ler()
        resultado = list(filter(lambda x: x.nome == nome, categorias))

        if len(resultado):
            return resultado[0]
        raise CategoriaFornecedorNaoExiste

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
                DaoCategoriaFornecedor.buscar(nome)
                raise CategoriaFornecedorJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: CategoriaFornecedor(nome)
                if (x.nome == categoria)
                else (x),
                lista,
            )
        )

        cls.sobrepor_lista_salva(nova_lista)
