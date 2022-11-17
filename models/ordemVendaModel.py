from datetime import datetime
from functools import reduce
from typing import Dict, List

from .clienteModel import Cliente
from .funcionarioModel import Funcionario
from .produtoModel import Produto


class Venda:
    def __init__(
        self,
        itens: List[Dict['produto':Produto, 'quantidade':int]],
        vendedor: Funcionario,
        cliente: Cliente,
        data: str = datetime.now().strftime('%d/%m/%Y'),
    ) -> None:
        self.itens = itens
        self.vendedor = vendedor
        self.cliente = cliente
        self.data = data

    def total_venda(self):
        total = reduce(
            lambda a, ordem: a + ordem['produto'].preco * ordem['quantidade'],
            self.itens,
            0,
        )
        return round(total, 2)


class VendaNaoExiste(Exception):
    pass


class VendaJaExiste(Exception):
    pass
