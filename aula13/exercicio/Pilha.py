from Livro import Livro

class Pilha:

    def __init__(self):
        
        self.topo = None

        self.tamanho = 0

    def adicionarLivroNaPilha(self, titulo_livro, resumo_livro, qtd_paginas_livro):
        # Nó guardado em memoria
        nodo_livro = Livro(titulo_livro, resumo_livro, qtd_paginas_livro)
        #print(f"obj do livro criado: {nodo_livro}")
       
        # if self.topo == None:
        #     self.topo = nodo_livro
        # else:
        #     nodo_livro.proximo = self.topo 
        #     self.topo = nodo_livro
        if self.topo != None:
            # Proximo livro que acabou de chegar vira o topo da pilha
            nodo_livro.proximo = self.topo 
        # o topo vira o elemento anteriror
        self.topo = nodo_livro
                    
        #print(f"Obj: {nodo_livro.proximo} está no topo.")

        self.tamanho += 1

    def imprimirPilha(self):
        
        print("---------------------------------------------")
        
        #verificar se a Fila está vazia
        if self.topo == None:
            
            print("Fila vazia.")
            
        else:
            
            print(f"Pilha com {self.tamanho} elementos")
            
            valor_auxiliar = self.topo

            texto = ""

            while valor_auxiliar:
                #imprimindo e indo para o proximo

                texto += valor_auxiliar.titulo_livro + " \n"

                valor_auxiliar = valor_auxiliar.proximo
                
            print(texto)
        
        print("---------------------------------------------")
    """
    def remover(self):

        if self.topo:

            if self.topo.proximo == None:

                self.topo = None

                self.fim = None

            else:
                self.topo = self.topo.proximo

            self.tamanho -= 1
        self.imprimirPilha()
    """

    def removerLivroTopoPilha(self):

        if self.topo:

            self.topo = self.topo.proximo

            if self.topo == None:

                self.fim = None
            
            self.tamanho -= 1

            

                
                
        