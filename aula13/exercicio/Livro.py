class Livro:
    
    def __init__(self, titulo_livro, resumo_livro, qtd_paginas_livro):
        
        self.titulo_livro = titulo_livro

        self.resumo_livro = resumo_livro

        self.qtd_paginas_livro = qtd_paginas_livro
        
        self.proximo = None
        
        