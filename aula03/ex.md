# Classe Pedido:
+ id: Int
+ ano: String
+ produto: [Produto]
+ cliente: [Pessoa]

# Classe Produto:
+ id: Int
+ nome: String
+ preco: double
+ qtd: double
+ cat: [Categoria]

# Classe Categoria:
+ id: Int
+ nome: String
