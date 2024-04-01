from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca_veiculo, ano_veiculo, categoria, qtd_portas):

        super().__init__(
            marca_veiculo = marca_veiculo,
            ano_veiculo = ano_veiculo,
            categoria = categoria
        )

        self.qtd_portas = qtd_portas

    def __str__(self):

        resultado = f"{super().__str__()}\n Qtd Portas: {self.qtd_portas}"

        return resultado

    def imprimir(self):
        #Aproveitando a classe Pai Veiculo
        print("Carro:")
        super().imprimir()




