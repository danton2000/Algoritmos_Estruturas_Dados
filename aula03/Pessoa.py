from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, idade = 18, cid = Cidade(nome="Tangamandápio")):

        self.nome = nome
        self.idade = idade
        self.cidade = cid
        print(f"Pessoa {self.nome} construida.")