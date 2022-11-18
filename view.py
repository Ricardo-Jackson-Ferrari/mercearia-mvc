import os
from time import sleep

import controllers
from utils.mensagens import Mensagem

if __name__ == '__main__':
    while True:
        while True:
            try:
                menu = int(
                    input(
                        """Escolha uma opção de acordo com o número a esquerda
[1] acessar (Categoria produto)
[2] acessar (Produto)
[3] acessar (Estoque)
[4] acessar (Categoria fornecedor)
[5] acessar (Fornecedor)
[6] acessar (Cliente)
[7] acessar (Cargo Funcionário)
[8] acessar (Funcionario)
[9] acessar (Venda)
[0] para sair
"""
                    )
                )
                break
            except ValueError:
                sleep(1)
                Mensagem.vermelha('Opção inválida.')
        if 0 < menu > 9:
            Mensagem.vermelha('Opção inválida.')
            sleep(1)
        else:
            if menu == 1:
                controller = controllers.ControllerCategoriaProduto
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Categoria produto)
[2] remover (Categoria produto)
[3] alterar (Categoria produto)
[4] mostrar (Categoria produto)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')
                    os.system('cls||clear')
                    match opcao:
                        case 1:
                            controller.cadastrar(
                                input('Informe o nome da nova categoria: ')
                            )
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome da categoria a ser removida: '
                                )
                            )
                        case 3:
                            cargo = input(
                                'Informe o nome da categoria a ser alterada: '
                            )
                            nome = input('Informe o novo nome da categoria: ')
                            controller.alterar(categoria=cargo, nome=nome)
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 2:
                controller = controllers.ControllerProduto
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Produto)
[2] remover (Produto)
[3] alterar (Produto)
[4] mostrar (Produto)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')
                    match opcao:
                        case 1:
                            nome = input('Informe o nome do novo produto: ')
                            cargo = input('Informe a categoria: ')
                            preco = input('Informe o preço: ')
                            controller.cadastrar(
                                nome=nome,
                                categoria_nome=cargo,
                                preco=preco,
                            )
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome do produto a ser removido: '
                                )
                            )
                        case 3:
                            produto = input('Informe o nome do produto: ')
                            nome = input('Informe o novo nome do produto: ')
                            cargo = input('Informe a nova categoria: ')
                            preco = input('Informe o novo preço: ')
                            controller.alterar(
                                produto=produto,
                                nome=nome,
                                categoria=cargo,
                                preco=preco,
                            )
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 3:
                controller = controllers.ControllerEstoque
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Estoque)
[2] remover (Estoque)
[3] alterar (Estoque)
[4] mostrar (Estoque)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')
                    match opcao:
                        case 1:
                            produto = input('Informe o produto: ')
                            quantidade = input('Informe a quantidade: ')
                            controller.cadastrar(produto, quantidade)
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome do produto para remover o estoque: '
                                )
                            )
                        case 3:
                            estoque = input(
                                'Informe o nome do produto para alterar o estoque: '
                            )
                            produto = input('Informe o novo nome do produto: ')
                            quantidade = input('Informe a nova quantidade: ')
                            controller.alterar(estoque, produto, quantidade)
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 4:
                controller = controllers.ControllerCategoriaFornecedor
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Categoria fornecedor)
[2] remover (Categoria fornecedor)
[3] alterar (Categoria fornecedor)
[4] mostrar (Categoria fornecedor)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')
                    match opcao:
                        case 1:
                            controller.cadastrar(
                                input('Informe o nome da nova categoria: ')
                            )
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome da categoria a ser removida: '
                                )
                            )
                        case 3:
                            cargo = input(
                                'Informe o nome da categoria a ser alterada: '
                            )
                            nome = input('Informe o novo nome da categoria: ')
                            controller.alterar(categoria=cargo, nome=nome)
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 5:
                controller = controllers.ControllerFornecedor
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Fornecedor)
[2] remover (Fornecedor)
[3] alterar (Fornecedor)
[4] mostrar (Fornecedor)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')

                    match opcao:
                        case 1:
                            nome = input('Informe o nome fornecedor: ')
                            cnpj = input('Informe o cnpj: ')
                            cargo = input('Informe a categoria: ')
                            telefone = input('Informe o telefone: ')
                            controller.cadastrar(
                                nome=nome,
                                cnpj=cnpj,
                                categoria=cargo,
                                telefone=telefone,
                            )
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome do fornecedor a ser excluído: '
                                )
                            )
                        case 3:
                            fornecedor = input(
                                'Informe o nome do fornecedor a ser alterado: '
                            )
                            nome = input('Informe o novo nome: ')
                            cnpj = input('Informe o novo cnpj: ')
                            cargo = input('Informe a nova categoria: ')
                            telefone = input('Informe o novo telefone: ')
                            controller.alterar(
                                fornecedor=fornecedor,
                                nome=nome,
                                cnpj=cnpj,
                                categoria=cargo,
                                telefone=telefone,
                            )
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 6:
                controller = controllers.ControllerCliente
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Cliente)
[2] remover (Cliente)
[3] alterar (Cliente)
[4] mostrar (Cliente)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')

                    match opcao:
                        case 1:
                            nome = input('Informe o nome: ')
                            cpf = input('Informe o cpf: ')
                            telefone = input('Informe o telefone: ')
                            controller.cadastrar(
                                nome=nome,
                                cpf=cpf,
                                telefone=telefone,
                            )
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome do cliente para o remover: '
                                )
                            )
                        case 3:
                            cliente = input(
                                'Informe o nome do cliente para alterar o estoque: '
                            )
                            nome = input('Informe o novo nome do cliente: ')
                            cpf = input('Informe o novo cpf: ')
                            telefone = input('Informe o novo telefone: ')
                            controller.alterar(
                                cliente=cliente,
                                nome=nome,
                                cpf=cpf,
                                telefone=telefone,
                            )
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 7:
                controller = controllers.ControllerCargoFuncionario
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Cargo funcionário)
[2] remover (Cargo funcionário)
[3] alterar (Cargo funcionário)
[4] mostrar (Cargo funcionário)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')
                    match opcao:
                        case 1:
                            controller.cadastrar(
                                input('Informe o nome do cargo funcionário: ')
                            )
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome do cargo a ser removida: '
                                )
                            )
                        case 3:
                            cargo = input(
                                'Informe o nome da cargo a ser alterada: '
                            )
                            nome = input('Informe o novo nome da categoria: ')
                            controller.alterar(cargo=cargo, nome=nome)
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 8:
                controller = controllers.ControllerFuncionario
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Funcionario)
[2] remover (Funcionario)
[3] alterar (Funcionario)
[4] mostrar (Funcionario)
[5] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')

                    match opcao:
                        case 1:
                            nome = input('Informe o nome: ')
                            cpf = input('Informe o cpf: ')
                            cargo = input('Informe o cargo: ')
                            telefone = input('Informe o telefone: ')
                            controller.cadastrar(
                                nome=nome,
                                cpf=cpf,
                                cargo=cargo,
                                telefone=telefone,
                            )
                        case 2:
                            controller.excluir(
                                input(
                                    'Informe o nome do funcionario para o remover: '
                                )
                            )
                        case 3:
                            funcionario = input(
                                'Informe o nome do funcionario para alterar o estoque: '
                            )
                            nome = input(
                                'Informe o novo nome do funcionario: '
                            )
                            cpf = input('Informe o novo cpf: ')
                            cargo = input('Informe o novo cargo: ')
                            telefone = input('Informe o novo telefone: ')
                            controller.alterar(
                                funcionario=funcionario,
                                nome=nome,
                                cargo=cargo,
                                cpf=cpf,
                                telefone=telefone,
                            )
                        case 4:
                            controller.listar()
                        case 5:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 9:
                controller = controllers.ControllerVenda
                while True:
                    while True:
                        try:
                            opcao = int(
                                input(
                                    """Escolha uma opção de acordo com o número a esquerda
[1] cadastrar (Venda)
[2] mostrar (Venda)
[3] mostrar relatório (Venda)
[4] para sair
"""
                                )
                            )
                            break
                        except ValueError:
                            Mensagem.vermelha('Opção inválida.')

                    match opcao:
                        case 1:
                            cliente = input('Informe o cliente: ')
                            vendedor = input('Informe o vendedor: ')
                            itens = []
                            while True:
                                produto = input('Informe o produto: ')
                                while True:
                                    try:
                                        quantidade = int(
                                            input('Informe a quantidade: ')
                                        )
                                        break
                                    except ValueError:
                                        Mensagem.vermelha('Valor inválido.')
                                itens.append(
                                    {
                                        'produto': produto,
                                        'quantidade': quantidade,
                                    }
                                )
                                while True:
                                    decisao = input(
                                        'Adicionar mais ? [S]Sim / [N]Não '
                                    )
                                    if decisao not in ['S', 's', 'N', 'n']:
                                        Mensagem.vermelha('Opção inválida.')
                                    else:
                                        break
                                if decisao.lower() == 'n':
                                    break
                            controller.cadastrar(
                                itens=itens, vendedor=vendedor, cliente=cliente
                            )

                        case 2:
                            controller.listar()
                        case 3:
                            controller.relatorio_produtos()
                        case 4:
                            break
                        case _:
                            Mensagem.vermelha('Opção inválida.')

            if menu == 0:
                Mensagem.verde('Programa encerrado.')
                break
