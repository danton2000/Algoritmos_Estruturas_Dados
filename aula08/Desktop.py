from Computador import Computador

class Desktop(Computador):

    def __init__(self):
        self._potenciaDaFonte = None

    def getInformacoes(self):
        texto = "Desktop:\n"
        texto += super().getInformacoes()
        texto += f"\nPotencia da Fonte: {self._potenciaDaFonte}"
        return texto


    def cadastrar(self, modelo, cor, preco, potenciaDaFonte):
        # Construindo na classe Pai
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte