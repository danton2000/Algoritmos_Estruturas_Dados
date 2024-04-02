from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self, marca_veiculo, qtd_rodas, modelo_veiculo, velocidade_veiculo, categoria, potencia_motor = 100):

        super().__init__(
            marca_veiculo = marca_veiculo,
            qtd_rodas = qtd_rodas,
            modelo_veiculo = modelo_veiculo,
            velocidade_veiculo = velocidade_veiculo,
            categoria = categoria
        )

        self.potencia_motor = potencia_motor

    def __str__(self):

        resultado = f"{super().__str__()}\n Potencia do Motor: {self.potencia_motor}"

        return resultado

    def imprimirInformacoes(self):
        #Aproveitando a classe Pai Veiculo
        print("Automóvel:")
        super().imprimirInformacoes()




