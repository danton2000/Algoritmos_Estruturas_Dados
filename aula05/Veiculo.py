from Categoria import Categoria

class Veiculo:
# Se não for passada a categoria é instanciado a Categoria com um valor default
    def __init__(self, marca_veiculo = "Honda", qtd_rodas = 0, modelo_veiculo = "Padrão", velocidade_veiculo = 0, categoria = Categoria(None)):

        self.id = None

        self.marca_veiculo = marca_veiculo
        
        self.qtd_rodas = qtd_rodas

        self.modelo_veiculo = modelo_veiculo

        self.velocidade_veiculo = velocidade_veiculo

        self.categoria = categoria

    def __str__(self):

        resultado = f"Marca: {self.marca_veiculo}\n Qtd Rodas: {self.qtd_rodas}\n Modelo: {self.modelo_veiculo}\n Velocidade {self.velocidade_veiculo}\n Cateogira: {self.categoria.nome_categoria}"

        return resultado

    def imprimirInformacoes(self):

        print(f"Veiculo:\n {self}")

        #print(f"Veiculo:\n {self.__str__()}")

        #print(f"Veiculo:\n {str(self)}")

    def acelerarVeiculo(self, valor):

        self.velocidade_veiculo += valor

    def frearVeiculo(self, valor):

        self.velocidade_veiculo -= valor

