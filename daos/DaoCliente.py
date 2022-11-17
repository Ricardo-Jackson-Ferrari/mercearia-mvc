import json
from typing import List

from models import Cliente, ClienteJaExiste, ClienteNaoExiste

from .DaoBase import DaoBase


class DaoCliente(DaoBase):
    arquivo_txt: str = 'cliente.txt'

    @classmethod
    def salvar(cls, cliente: Cliente) -> None:
        try:
            cls.buscar(cliente.nome)
            raise ClienteJaExiste
        except ClienteNaoExiste:
            with open(cls.local_arquivo(), 'a') as arq:
                data = {
                    'nome': cliente.nome,
                    'cpf': cliente.cpf,
                    'telefone': cliente.telefone,
                }
                arq.writelines(json.dumps(data))
                arq.writelines('\n')

    @classmethod
    def ler(cls) -> List[Cliente]:
        with open(cls.local_arquivo(), 'r') as arq:
            clientes = arq.readlines()

        clientes = list(map(lambda x: x.replace('\n', ''), clientes))
        clientes = list(map(lambda x: json.loads(x), clientes))

        return [
            Cliente(
                nome=cliente['nome'],
                cpf=cliente['cpf'],
                telefone=cliente['telefone'],
            )
            for cliente in clientes
        ]

    @classmethod
    def buscar(cls, nome) -> Cliente:
        clientes = cls.ler()
        resultado = list(filter(lambda x: x.nome == nome, clientes))

        if len(resultado):
            return resultado[0]
        raise ClienteNaoExiste

    @classmethod
    def excluir(cls, cliente: Cliente) -> None:
        lista = cls.ler()
        nova_lista = list(filter(lambda x: x.nome != cliente.nome, lista))

        cls.sobrepor_lista_salva(nova_lista)

    @classmethod
    def alterar(cls, nome_alterar, nome, cpf, telefone) -> None:
        DaoCliente.buscar(nome_alterar)

        if nome_alterar != nome:
            try:
                cls.buscar(nome)
                raise ClienteJaExiste
            except:
                pass

        lista = cls.ler()
        nova_lista = list(
            map(
                lambda x: Cliente(nome, cpf, telefone)
                if (x.nome == nome_alterar)
                else (x),
                lista,
            )
        )

        cls.sobrepor_lista_salva(nova_lista)
