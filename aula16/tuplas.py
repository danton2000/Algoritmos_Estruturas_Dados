carros = "Uno", "Doblo", "Toro", "Jeep", "Hilux"

print(carros)

print(

    carros[1:-2]

)

print(

    carros[2:]

)

print(sorted(carros))

carrosOrdenados = sorted(carros)

carrosOrdenados[0] = "Fusca"

print(carrosOrdenados)

def calcular(x,y):

    return x+y, x-y, x*y, x/y

resultado = calcular(10,2)

print(resultado)

print(resultado[1])