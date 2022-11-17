import os


class DaoBase:
    diretorio: str = 'data'
    arquivo_txt: str
    parametros_busca: list
    classe_model_nao_existe: object

    @classmethod
    def local_arquivo(cls):
        return os.path.join(cls.diretorio, cls.arquivo_txt)

    @classmethod
    def buscar(cls, value):
        lista = cls.ler()
        for parametro in cls.parametros_busca:
            resultado = list(
                filter(lambda x: x.__getattribute__(parametro) == value, lista)
            )
            if len(resultado):
                return resultado[0]

        raise cls.classe_model_nao_existe

    @classmethod
    def sobrepor_lista_salva(cls, nova_lista):
        with open(cls.local_arquivo(), 'w'):
            pass

        for item in nova_lista:
            cls.salvar(item)

    @classmethod
    def criar_arquivo(cls) -> None:
        if not os.path.exists(cls.local_arquivo()):
            with open(cls.local_arquivo(), 'w'):
                pass
