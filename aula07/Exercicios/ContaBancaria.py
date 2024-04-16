from abc import ABC, abstractmethod
# Vamos consuir dizer que uma classe é abstrata

class ContaBancaria(ABC):

    def __init__(self, numero_conta, saldo_conta):

        self.numero_conta = numero_conta

        self.saldo_conta = saldo_conta

    #Metodo abstrato só tem a implementação
    @abstractmethod
    def cadastrar(self, tipo_conta):
        
        pass

    @abstractmethod
    def depositar(self, valor):
        
        pass
    
    def imprimir(self):

        print(f"Numero da Conta: {self.numero_conta}")
        print(f"Saldo da Conta: {self.saldo_conta}")