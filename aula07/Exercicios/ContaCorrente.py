from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):

    def __init__(self, numero_conta, saldo_conta):
        super().__init__(numero_conta, saldo_conta)

        self.tipo_conta = None


    def cadastrar(self, tipo_conta):
        
        self.tipo_conta = tipo_conta
        
    def depositar(self, valor):
        
        self.saldo_conta += valor
        print(f"Valor Depositado: {valor}")

    def imprimir(self):

        super().imprimir()
        print(f"Tipo Conta: {self.tipo_conta}")