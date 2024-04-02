from Categoria import Categoria 

from Veiculo import Veiculo

from Automovel import Automovel

from Carro import Carro

from Moto import Moto

categoria1 = Categoria("SUV")

categoria2 = Categoria("Estradeiras")

categoria3 = Categoria("Sedan")

veiculo1 = Veiculo()

veiculo1.imprimirInformacoes()
print("---")

automovel1 = Automovel(
    marca_veiculo=veiculo1.marca_veiculo,
    qtd_rodas=veiculo1.qtd_rodas,
    modelo_veiculo=veiculo1.modelo_veiculo,
    velocidade_veiculo=veiculo1.velocidade_veiculo,
    categoria=veiculo1.categoria,
    potencia_motor=100
)

automovel1.imprimirInformacoes()

print("---")

moto1 = Moto(
    marca_veiculo=automovel1.marca_veiculo,
    qtd_rodas=automovel1.qtd_rodas,
    modelo_veiculo=automovel1.modelo_veiculo,
    velocidade_veiculo=automovel1.velocidade_veiculo,
    categoria=automovel1.categoria,
    potencia_motor=automovel1.potencia_motor,
    partida_eletrica=250
)

moto1.imprimirInformacoes()

print("---")

carro1 = Carro(
    marca_veiculo=automovel1.marca_veiculo,
    qtd_rodas=automovel1.qtd_rodas,
    modelo_veiculo=automovel1.modelo_veiculo,
    velocidade_veiculo=automovel1.velocidade_veiculo,
    categoria=automovel1.categoria,
    potencia_motor=automovel1.potencia_motor,
    qtd_portas=6
)

carro1.acelerarVeiculo(300)

carro1.frearVeiculo(150)

carro1.imprimirInformacoes()