precos = [
    4,
    10,
    15
]

def aumentarPreco(x):

    return x * 1.1

novosPrecos = map(
    aumentarPreco, 
    precos
)

print(list(novosPrecos))

valores = (
    (10,20),
    [30,40]
)

def somar(x):

    return x[0] + x[1]

print("Soma:", list(map(somar, valores)))

def somarValores(valores):

    soma = 0

    for v in valores:

        soma += v

    return soma

v1 = [1,2,3]

v2 = [4,5,6,7]

print("Soma dos valores:", list(map(somarValores, [v1, v2])))

def multiplicar(x,y):

    return x * y

# x = 2,3,4

# y = 5,6,7

numeros = (2,3,4), (5,6,7)

print("Multiplicando os valores:", list(map(multiplicar, numeros[0], numeros[1])))