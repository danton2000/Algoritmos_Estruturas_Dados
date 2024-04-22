from Computador import Computador

class Notebook(Computador):

    def __init__(self):
        
        self.__tempoDeBateria = None

    def getInformacoes(self):
        texto = "Notebook:\n"
        texto += super().getInformacoes()
        texto += f"\nTempo de Bateria: {self.__tempoDeBateria}"
        return texto

    def cadastrar(self, modelo, cor, preco, tempoDeBateria):
        # Construindo na classe Pai
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria    