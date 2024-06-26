from No import No

#criar metodo para armazenar na ordem crescente
# No momento de armazenar o dado, validar se o dado é maior ou menor com os outros da lista.

class Lista:
    
    def __init__(self):
        
        self.inicio  = None
        
        self.tamanho = 0
        
    def addCrescente(self, valor):
        
        nodo = No(valor)
        
        if self.inicio == None:
            #Lista vazia
            self.inicio = nodo
            
        else:
            #Verifica se o dado que acabou de chegar é menor que o inicio da lista
            if nodo.dado < self.inicio.dado:
                
                nodo.proximo = self.inicio
                
                self.nodo.anterior = nodo
                
                self.inicio = nodo
                
            else:
                # Percorrer todos os elementos da lista para colocar na posição 
                
                ant = self.inicio
                
                aux = self.inicio.proximo
                
                while aux:
                    
                    if nodo.dado < aux.dado:
                        
                        nodo.proximo = ant.proximo
                        
                        ant.proximo = nodo
                        
                        #para laço
                        break 
                    else:
                        
                        ant = aux
                        
                        aux = aux.proximo
                    
                
                #verificar se o aux é None já percorreu tudo
                if aux == None and nodo.dado >= ant.dado:
                    
                    ant.proximo = nodo
                    
            self.tamanho += 1
            
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
                
                    
                    

            
        
