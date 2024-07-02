class ListaEncadeada:
    
    def __init__(self):
        
        self.inicio  = None
        
        self.tamanho = 0
        
    def adicionar(self, apartamento):
        nodo = apartamento
        
        if self.inicio == None:
            #Lista vazia
            self.inicio = nodo
            
        else:
            #Verifica se o vaga_garagem que acabou de chegar é menor que o inicio da lista
            if nodo.vaga_garagem > self.inicio.vaga_garagem:
                
                nodo.proximo = self.inicio
                
                self.inicio = nodo
                
            else:
                # Percorrer todos os elementos da lista para colocar na posição 
                
                ant = self.inicio
                
                aux = self.inicio.proximo
                
                while aux:
                    
                    if nodo.vaga_garagem > aux.vaga_garagem:
                        
                        nodo.proximo = ant.proximo
                        
                        ant.proximo = nodo
                        
                        #para laço
                        break 
                    else:
                        
                        ant = aux
                        
                        aux = aux.proximo
                    
                
                #verificar se o aux é None já percorreu tudo
                if aux == None and nodo.vaga_garagem >= ant.vaga_garagem:
                    
                    ant.proximo = nodo
                    
        self.tamanho += 1
        
    def remover(self):
        
        #verificar se lista não está vazia
        if self.inicio != None:
            #Não está vazia
            self.inicio = self.inicio.proximo
            
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
                print(f"Numero da vaga: {var_aux.vaga_garagem}")
                
                var_aux = var_aux.proximo  
            
                
