class Pessoa:

    def __init__(self):

        self.__codigo = None

        self.nome = None

        self._endereco = None

    @property
    def codigo(self):

        return self.__codigo

    @property
    def nome(self):

        return self.nome

    @property
    def endereco(self):

        return self._endereco

    @codigo.setter
    def codigo(self, codigo):

        self.__codigo = codigo

    @nome.setter
    def nome(self, nome):

        self.nome = nome

    @endereco.setter
    def endereco(self, endereco):

        self._endereco = endereco

    def ImprimeNome(self):

        self.nome

    def __ImprimeTelefone(self):

        print(f"Telefone: {self._telefone}")


