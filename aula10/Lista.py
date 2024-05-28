from No import No

class Lista:
    
    def __init__(self):
        
        self.inicio  = None
        
        self.tamanho = 0
        
    """
    def adicionarNoInicio(self, valor):
        #Adicionando pelo momento de chegada
        
        #guardando em memoria e a referencia(instancia) do objeto
        nodo = No(valor)
        
        if self.inicio == None:
            #lista vazia
            self.inicio = nodo
            
        else:
            nodo.proximo = self.inicio
            
            self.inicio = nodo
            
        self.tamanho += 1
        
        self.imprimir()
    """
    
    def adicionarNoInicio(self, valor):
        #Adicionando pelo momento de chegada
        
        #guardando em memoria e a referencia(instancia) do objeto
        nodo = No(valor)
        
        if self.inicio != None:
            nodo.proximo = self.inicio

        self.inicio = nodo
            
        self.tamanho += 1
        
        self.imprimir()
        
    def adicionarNoFim(self, valor):
        #Adicionando pelo momento de chegada
        
        #guardando em memoria e a referencia(instancia) do objeto
        nodo = No(valor)
        
        if self.inicio == None:
            #lista vazia
            self.inicio = nodo
            
        else:
            #percorrer a lista para saber quem é o ultimo
            #var_aux tem as caracterias de No
            var_aux = self.inicio
            
            while var_aux.proximo:
                #chegou no ultimo elemento
                #quando o proximo for None ele sai do laço, pq achou o ultimo nó
                var_aux = var_aux.proximo
                
            var_aux.proximo = nodo
            
        self.tamanho += 1
        
        self.imprimir()
    
    """
    def removerDoInicio(self):
        
        #verificar se lista não está vazia
        if self.inicio == None:
            # vazia
            print("Lista vazia.")
            
        elif self.inicio.proximo == None:
            #Só tem um elemento
            self.inicio = None
            
            self.tamanho = 0
            
        else:
            #pelo menos 2 elementos
            self.inicio = self.inicio.proximo
            
            self.tamanho -= 1
            
        self.imprimir()
    """
    def removerDoInicio(self):
        
        #verificar se lista não está vazia
        if self.inicio != None:
            #Não está vazia
            self.inicio = self.inicio.proximo
            
            self.tamanho -= 1
            
        self.imprimir()
        
    def removerDoFim(self):
        
        if self.inicio == None:
            
            print("Lista vazia.")
            
        elif self.inicio.proximo == None:
            # 1 elemento só
            self.inicio = None
            
            self.tamanho = 0
            
        else:
            # Mais de 1 elemento
            # percorrer a lista, no ultimo elemento, te, que apontar para mais ninguem
            
            anterior = self.inicio
            
            aux = self.inicio.proximo
            
            #quando chegar no ultimo elemento, ele sai do laço
            while aux.proximo:
                
                #pegando o elemento atual e fazendo ele ser o anterior
                
                anterior = aux
                
                aux = aux.proximo
                
            anterior.proximo = None
            
            self.tamanho -= 1
            
        self.imprimir()
            
            
    def imprimir(self):
        
        print("---------------------------------------------")
        
        #verificar se a lista está vazia
        if self.inicio == None:
            
            print("Lista vazia.")
            
        else:
            
            print(f"Lista Encadeada com {self.tamanho} elementos")
            
            var_aux = self.inicio
            
            while var_aux:
                #imprimindo e indo para o proximo
                print(var_aux.dado)
                
                var_aux = var_aux.proximo  
            
                
#criar metodo para armazenar na ordem crescer
# No momento de armazenar o dado, validar se o dado é maior ou menor com os outros da lista.

