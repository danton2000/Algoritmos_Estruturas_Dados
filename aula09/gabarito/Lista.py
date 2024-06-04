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
                
    def remover(self, valor):
        
        #Saber se foi removido
        tamInicial = self.tamanho
        
        if self.inicio != None:
            # Se a lista contem  só 1 elemento e achou o valor para deletar
            if self.inicio.proximo == None and self.inicio.dado == valor:
                
                self.inicio = None
                
                self.tamanho = 0
            
            # Se a lista contem vários elementos e o valor é igual ao primeiro   
            elif self.inicio.dado == valor:
                
                self.inicio = self.inicio.proximo
                
                self.tamanho -= 1
                
            else:
            #Se a lista contem vários elementos e o valor NÃO é igual ao primeiro   
            
                ant = self.inicio
                
                aux = self.inicio.proximo
                
                while aux:
                    
                    if aux.dado == valor:
                        
                        ant.proximo = aux.proximo
                        
                        self.tamanho -= 1
                        
                        break
                    
                    else:
                        ant = aux
                        
                        aux = aux.proximo

        if tamInicial == self.tamanho:
            
            print("Valor não encontrado.")

        self.imprimir()
                    
                    

            
        
