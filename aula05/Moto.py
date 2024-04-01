from Veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca_veiculo, ano_veiculo, categoria, cilindradas):

        super().__init__(
            marca_veiculo = marca_veiculo,
            ano_veiculo = ano_veiculo,
            categoria = categoria
        )

        self.cilindradas = cilindradas

    def __str__(self):

        resultado = f"{super().__str__()}\n Cilindradas: {self.cilindradas}"

        return resultado

    def imprimir(self):
        
        print(f"Moto:\n {self}")




