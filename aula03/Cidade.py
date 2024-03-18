class Cidade:

    def __init__(self, id = 0, nome = "Itaiti"):

        self.id = id
        self.nome = nome

    def __str__(self):

        return f"Cidade: {self.nome}"