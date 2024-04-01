from Categoria import Categoria 

from Veiculo import Veiculo 

from Carro import Carro

from Moto import Moto

categoria1 = Categoria("SUV")

categoria2 = Categoria("Estradeiras")

categoria3 = Categoria("Sedan")

veiculo1 = Veiculo()

veiculo1.imprimir()
print("---")

carro1 = Carro("Jepp", 2023, categoria1, 4)

carro1.imprimir()
print("---")

moto1 = Moto("BMW", 2022, categoria2, 1000)

moto1.imprimir()