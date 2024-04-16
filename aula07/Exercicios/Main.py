"""
Implementar a classe abstrata
ContaBancaria com os
métodos cadastrar e
depositar e as respectivas
classes concretas.
"""
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente

contaPoupanca1 = ContaPoupanca(1234, 0)

contaPoupanca1.cadastrar("conta-poupança")

contaPoupanca1.depositar(100)

contaPoupanca1.imprimir()

print("---")

contaCorrente1 = ContaCorrente(4321, 0)

contaCorrente1.cadastrar("conta-corrente")

contaCorrente1.depositar(50)

contaCorrente1.imprimir()