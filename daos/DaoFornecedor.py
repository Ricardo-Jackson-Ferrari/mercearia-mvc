import json
from typing import List

from models import Fornecedor, FornecedorJaExiste, FornecedorNaoExiste

from .DaoBase import DaoBase
from .DaoCategoriaFornecedor import DaoCategoriaFornecedor


class DaoFornecedor(DaoBase):
    arquivo_txt: str = 'fornecedores.txt'

    @classmethod
    def salvar(cls, fornecedor: Fornecedor) -> None:
        try:
            cls.buscar(fornecedor.nome)
            raise FornecedorJaExiste
        except FornecedorNaoExiste:

            with open(cls.local_arquivo(), 'a') as arq:
                data = {
                    'nome': fornecedor.nome,
                    'cnpj': fornecedor.cnpj,
                    'categoria': fornecedor.categoria.nome,
                    'telefone': fornecedor.telefone,
                }
                arq.writelines(json.dumps(data))
                arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[Fornecedor]:
        try:
            with open(cls.local_arquivo(), 'r') as arq:
                fornecedores = arq.readlines()

            fornecedores = list(
                map(lambda x: x.replace('\n', ''), fornecedores)
            )
            fornecedores = list(map(lambda x: json.loads(x), fornecedores))
            return [
                Fornecedor(
                    nome=fornecedor['nome'],
                    categoria=DaoCategoriaFornecedor.buscar(
                        fornecedor['categoria']
                    ),
                    telefone=fornecedor['telefone'],
                    cnpj=fornecedor['cnpj'],
                )
                for fornecedor in fornecedores
            ]
        except FileNotFoundError:
            cls.criar_arquivo()
            return cls.ler()

    @classmethod
    def buscar(cls, nome) -> Fornecedor:
        funcionarios = cls.ler()
        resultado = list(filter(lambda x: x.nome == nome, funcionarios))

        if len(resultado):
            return resultado[0]
        raise FornecedorNaoExiste

    @classmethod
    def excluir(cls, fornecedor: Fornecedor) -> None:
        lista = cls.ler()
        nova_lista = list(filter(lambda x: x.nome != fornecedor.nome, lista))

        cls.sobrepor_lista_salva(nova_lista)

    @classmethod
    def alterar(cls, fornecedor, nome, cnpj, telefone, categoria) -> None:
        cls.buscar(fornecedor)

        if fornecedor != nome:
            try:
                cls.buscar(nome)
                raise FornecedorJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: Fornecedor(nome, cnpj, telefone, categoria)
                if (x.nome == fornecedor)
                else (x),
                lista,
            )
        )

        cls.sobrepor_lista_salva(nova_lista)
