from rich.console import Console

console = Console()


class Mensagem:
    @classmethod
    def vermelha(cls, texto):
        cls.print_cor(texto, 'red')

    @classmethod
    def amarela(cls, texto):
        cls.print_cor(texto, 'yellow')

    @classmethod
    def verde(cls, texto):
        cls.print_cor(texto, 'green')

    @classmethod
    def input_amarelo(cls, texto):
        cls.input_cor(texto, 'amarelo')

    @classmethod
    def print_cor(cls, texto, cor):
        console.print(f'[{cor}]{texto}[{cor}]')

    @classmethod
    def input_cor(cls, texto, cor):
        console.print(f'[{cor}]{texto}[{cor}]')
