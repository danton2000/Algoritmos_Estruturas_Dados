# Classe Pedido:
+ id: Int
+ end: String
+ produto: [Produto]
+ cliente: [Pessoa]

+ addProduto()

# Classe Produto:
+ id: Int
+ nome: String
+ preco: double
+ qtd: double
+ cat: [Categoria]

# Classe Categoria:
+ id: Int
+ nome: String
