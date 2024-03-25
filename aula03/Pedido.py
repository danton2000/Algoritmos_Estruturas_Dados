from Produto import Produto

from Pessoa import Pessoa

class Pedido:

    def __init__(self, endereco, cliente = Pessoa("Anônimo")):

        self.id = None

        self.endereco = endereco

        self.cliente = cliente

        self.produtos = []

    def __str__(self):

        texto = f"Endereço do Pedido:  {self.endereco} - {self.cliente.cidade.nome}"

        texto += f"\nCliente:  {self.cliente.nome}"

        texto += f"\nProdutos: \n"

        if len(self.produtos) == 0:

            texto += "Pedido Vazio"

        for produto in self.produtos:

            texto += produto.nome  + " . " + str(produto.preco) + " - Categoria: " + produto.categoria.nome + "\n"

        return texto

    def addProduto(self, produto):

        self.produtos.append(produto)

        soma = 0
        # Pegando 1 produto
        for produto in self.produtos:

            soma += produto.preco

        return soma


