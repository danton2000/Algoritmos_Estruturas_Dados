from abc import ABC, abstractmethod
# Vamos consuir dizer que uma classe é abstrata

# Não pode intanciar essa classe, só as suas "sub classes"
class Veiculo(ABC):

    def __init__(self, modelo, ano):

        self.modelo = modelo

        self.ano = ano

    #proximo método será obrigatório
    #Metodo abstrato só tem a implementação
    @abstractmethod
    def ligar(self, chave):
        pass

    #Metodo comum
    def imprimir(self):

        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

    def desligar(self):

        print("Veiculo desligado")