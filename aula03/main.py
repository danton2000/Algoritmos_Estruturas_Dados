from Cidade import Cidade

from Pessoa import Pessoa

c1 = Cidade()

c2 = Cidade(1, "Porto Alegre")

c3 = Cidade(2, "Lajeado")

print(c1)

print(c2)

print(c3)

p1 = Pessoa(
    nome = "Danton"
)

p2 = Pessoa(
    nome = "Maria",
    idade = 20
)

p3 = Pessoa(
    nome = "Daniel",
    idade = 21,
    cid= c1
)

p4 = Pessoa(
    nome = "Daniel",
    cid= c2
)

p4 = Pessoa(
    nome = "Luffy",
    idade = 30
)

print(p4.idade)
