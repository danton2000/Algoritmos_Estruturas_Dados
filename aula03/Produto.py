from Categoria import Categoria

class Produto:

    def __init__(self, nome, preco=10.00, qtd=0, categoria=Categoria(None)):

        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categoria = categoria
        
    def __str__(self):

        texto = f"Produto: {self.nome}"
        texto += "\nPreço: {self.preco}"
        texto += "\nCategoria: {self.categoria}"

        return texto