class ListaEncadeada:
    
    def __init__(self):
        
        self.inicio  = None
        
        self.tamanho = 0
        
    def adicionar(self, apartamento):
        #Adicionando pelo momento de chegada
        
        #guardando em memoria e a referencia(instancia) do objeto
        nodo = apartamento
        
        #Se lista não está vazia
        if self.inicio != None:
            nodo.proximo = self.inicio
        
        # O atributo inicio recebe o objeto nodo contendo o dado atual e o proximo dado
        self.inicio = nodo
        
        # incremetando o tamanho + 1
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
                print(var_aux)
                
                var_aux = var_aux.proximo  
            
                
