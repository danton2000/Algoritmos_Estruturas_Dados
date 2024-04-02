from Automovel import Automovel

class Moto(Automovel):

    def __init__(self, marca_veiculo, qtd_rodas, modelo_veiculo, velocidade_veiculo, categoria, potencia_motor, partida_eletrica):

        super().__init__(
            marca_veiculo = marca_veiculo,
            qtd_rodas = qtd_rodas,
            modelo_veiculo = modelo_veiculo,
            velocidade_veiculo = velocidade_veiculo,
            potencia_motor = potencia_motor,
            categoria = categoria
        )

        self.partida_eletrica = partida_eletrica

    def __str__(self):

        resultado = f"{super().__str__()}\n Partida Eletrica: {self.partida_eletrica}"

        return resultado

    def imprimirInformacoes(self):
        
        print(f"Moto:\n {self}")




