from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, idade = 18, cid = Cidade(nome="Tangamandápio")):

        self.nome = nome
        self.idade = idade
        self.cidade = cid

    def __str__(self):

        return f"Pessoa: {self.nome}"