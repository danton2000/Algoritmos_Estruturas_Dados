class ListaEncadeada:
    
    def __init__(self):
        
        self.inicio  = None
        
        self.tamanho = 0
        
    def adicionar(self, apartamento):
        nodo = apartamento
        
        # print(nodo.id_apartamento)
        
        if self.inicio == None:
            #Lista vazia
            self.inicio = nodo
            
        else:
            #Verifica se o vaga_garagem que acabou de chegar é menor que o inicio da lista
            if nodo.vaga_garagem < self.inicio.vaga_garagem:
                
                nodo.proximo = self.inicio
                
                self.inicio = nodo
                
            else:
                # Percorrer todos os elementos da lista para colocar na posição 
                
                ant = self.inicio
                
                aux = self.inicio.proximo
                
                while aux:
                    
                    if nodo.vaga_garagem < aux.vaga_garagem:
                        
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
    
    def remover(self, vaga_garagem):
        tamInicial = self.tamanho
        if self.inicio != None:

            #Lista contendo só um elemente e este é igual ao vaga_garagem
            if self.inicio.proximo == None and self.inicio.vaga_garagem == vaga_garagem:
                self.inicio = None
                self.tamanho = 0

            #Lista contendo vários elementos e o vaga_garagem é igual ao primeiro
            elif self.inicio.vaga_garagem == vaga_garagem:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1

            # Lista com vários elementos e o vaga_garagem não está no primeiro
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if aux.vaga_garagem == vaga_garagem:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
        if tamInicial == self.tamanho:
            print( "Valor não encontrado")

        print("Vaga Liberada!")

    def imprimir(self):
        
        print("---------------------------------------------")
        
        #verificar se a lista está vazia
        if self.inicio == None:
            
            print("Lista vazia.")
            
        else:
            
            print(f"Lista Encadeada com {self.tamanho} Apartamentos com Vagas:")
            
            var_aux = self.inicio
            
            while var_aux:
                #imprimindo e indo para o proximo
                print(f"Numero da vaga: {var_aux.vaga_garagem}")
                
                var_aux = var_aux.proximo  
            
                
