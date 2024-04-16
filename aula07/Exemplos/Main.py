from Carro import Carro 
from Moto import Moto
#from Veiculo import Veiculo
# Não podemos instanciar de classes abstratas
# veiculo1 = Veiculo("Doblo", 2005)

carro1 = Carro("Doblo", 2005, 4)
carro1.ligar("1234")
carro1.imprimir()
carro1.desligar()

print("----------")

moto1 = Moto("Titan 150", 2003, 150)
moto1.ligar("1234")
moto1.imprimir()
moto1.desligar()
