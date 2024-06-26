from Automovel import Automovel

class Carro(Automovel):

    def __init__(self, marca_veiculo, qtd_rodas, modelo_veiculo, velocidade_veiculo, categoria, potencia_motor, qtd_portas):

        super().__init__(
            marca_veiculo = marca_veiculo,
            qtd_rodas = qtd_rodas,
            modelo_veiculo = modelo_veiculo,
            velocidade_veiculo = velocidade_veiculo,
            potencia_motor = potencia_motor,
            categoria = categoria
        )

        self.qtd_portas = qtd_portas

    def __str__(self):

        resultado = f"{super().__str__()}\n Qtd Portas: {self.qtd_portas}"

        return resultado

    def imprimirInformacoes(self):
        #Aproveitando a classe Pai Veiculo
        print("Carro:")
        super().imprimirInformacoes()




