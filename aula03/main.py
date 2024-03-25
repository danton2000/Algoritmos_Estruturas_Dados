from Cidade import Cidade

from Pessoa import Pessoa

from Produto import Produto

from Categoria import Categoria

from Pedido import Pedido

Cidade1 = Cidade()

Cidade2 = Cidade(1, "Porto Alegre")

cidade3 = Cidade(2, "Lajeado")

print(Cidade1)

print(Cidade2)

print(cidade3)

pessoa1 = Pessoa(
    nome = "Danton"
)

pessoa2 = Pessoa(
    nome = "Maria",
    idade = 20
)

pessoa3 = Pessoa(
    nome = "Daniel",
    idade = 21,
    cid= Cidade1
)

pessoa4 = Pessoa(
    nome = "Daniel",
    cid= Cidade2
)

pessoa5 = Pessoa(
    nome = "Luffy",
    idade = 30
)

print(pessoa5.idade)

print("-------- Retirar Pedido --------")

categoria = Categoria(nome = "Bebidas")

produto1 = Produto("Coca-Cola", 7.99, 100, categoria)

produto2 = Produto("Pepsi", 5.99, categoria = categoria)

produto3 = Produto("Amendoin")

pedido1 = Pedido("Rua A, 100", pessoa4)

print(pedido1)

# Adicionando produtos no pedido
total = pedido1.addProduto(produto1)
total = pedido1.addProduto(produto2)
total = pedido1.addProduto(produto3)

print(f"Total do Pedido: {total}")

print(pedido1)