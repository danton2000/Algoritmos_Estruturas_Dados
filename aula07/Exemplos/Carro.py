from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, modelo, ano, qtd_portas):
        super().__init__(modelo, ano)

        self.qtd_portas = qtd_portas

    def ligar(self, chave):
        
        if(chave == "1234"):

            print("Carro ligado")

        else:
            print("Não foi possivel ligar o Carro")

    def imprimir(self):
        super().imprimir()
        print(f"Quantidade de Portas: {self.qtd_portas}")