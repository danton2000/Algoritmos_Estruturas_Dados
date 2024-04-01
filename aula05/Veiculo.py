from Categoria import Categoria

class Veiculo:
# Se não for passada a categoria é instanciado a Categoria com um valor default
    def __init__(self, marca_veiculo = "Honda", ano_veiculo = 2014, categoria = Categoria(None)):

        self.id = None

        self.marca_veiculo = marca_veiculo
        
        self.ano_veiculo = ano_veiculo

        self.categoria = categoria

    def __str__(self):

        resultado = f"Marca: {self.marca_veiculo}\n Ano Veiculo: {self.ano_veiculo}\n Cateogira: {self.categoria.nome_categoria}"

        return resultado

    def imprimir(self):

        print(f"Veiculo:\n {self}")

        #print(f"Veiculo:\n {self.__str__()}")

        #print(f"Veiculo:\n {str(self)}")

