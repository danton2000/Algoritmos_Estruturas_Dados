from Conta import Conta

c = Conta()

print(c.saldo)

c.saldo = 2

print(c.saldo)
c.depositar(0.5)

print(c.saldo)
c.sacar(2)

print(c.saldo)