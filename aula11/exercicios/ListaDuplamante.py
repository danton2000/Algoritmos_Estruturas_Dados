from No import No

#criar metodo para armazenar na ordem crescente
# No momento de armazenar o dado, validar se o dado é maior ou menor com os outros da lista.

class ListaDuplamante:
    
    def __init__(self):
        
        self.inicio  = None

        self.fim = None
        
        self.tamanho = 0
        
    def addCrescente(self, valor):
        #Elemento que acabou de chegar
        nodo = No(valor)
        
        if self.inicio == None:
            #Lista vazia
            self.inicio = nodo

            self.fim = nodo
            
        else:
            # Verifica se o dado que acabou de chegar é menor que o inicio da lista
            # Verificando se o dado que acabou de cehgar é menor que o primeiro elemento
            if nodo.dado < self.inicio.dado:
                
                nodo.proximo = self.inicio
                
                # elemento que era o primeiro vai apontar para o dado que acabou de chegar
                self.inicio.valor_anteriorerior = nodo
                
                self.inicio = nodo
                
            else:
                # Percorrer todos os elementos da lista para colocar na posição 
                
                #Segundo valor
                valor_anterior = self.inicio
                
                #Terceiro valor
                valor_auxiliar = self.inicio.proximo
                # Só entra no laço se o valor_auxiliar não for nullo
                while valor_auxiliar:
                    
                    if nodo.dado < valor_auxiliar.dado:
                        
                        nodo.proximo = valor_anterior.proximo
                        
                        valor_anterior.proximo = nodo

                        valor_auxiliar.anterior = nodo

                        nodo.anterior = valor_anterior
                        
                        #para laço
                        break 
                    else:
                        
                        valor_anterior = valor_auxiliar
                        
                        valor_auxiliar = valor_auxiliar.proximo
                    
                
                #verificar se o valor_auxiliar é None já percorreu tudo
                if valor_auxiliar == None and nodo.dado >= valor_anterior.dado:
                    
                    valor_anterior.proximo = nodo

                    nodo.valor_anteriorerior = valor_anterior

                    self.fim = nodo
                    
            self.tamanho += 1
            
            self.imprimir()
            
    def imprimir(self):
        
        print("---------------------------------------------")
        
        #verificar se a lista está vazia
        if self.inicio == None:
            
            print("Lista vazia.")
            
        else:
            
            print(f"Lista Encadeada com {self.tamanho} elementos")
            
            valor_auxiliar = self.inicio
            
            while valor_auxiliar:
                #imprimindo e indo para o proximo
                print(valor_auxiliar.dado)
                
                valor_auxiliar = valor_auxiliar.proximo

    def imprimirReverso(self):
        
        print("---------------------------------------------")
        
        #verificar se a lista está vazia
        if self.inicio == None:
            
            print("Lista vazia.")
            
        else:
            
            print(f"Lista Encadeada com {self.tamanho} elementos na Ordem Inversa")
            
            valor_auxiliar = self.fim
            
            while valor_auxiliar:
                #imprimindo e indo para o proximo
                print(valor_auxiliar.dado)
                
                valor_auxiliar = valor_auxiliar.proximo
                
    def remover(self, valor):

        tamanho_inicial = self.tamanho

        if self.inicio != None:

            if self.inicio.proximo == None and self.inicio.dado == valor:

                self.inicio = None

                self.fim = None

                self.tamanho = 0

            elif self.inicio.dado == valor:

                #Pegando o anterior do 'segundo' elemento
                self.inicio.proximo.anterior = None

                self.inicio = self.inicio.proximo

                #self.inicio.anterior = None

                self.tamanho -= 1

            else:

                valor_anterior = self.inicio

                valor_auxiliar = self.inicio.proximo

                while valor_auxiliar:

                    if valor_auxiliar.dado == valor:

                        valor_anterior = valor_auxiliar.proximo

                        if valor_auxiliar.proximo:

                            valor_anterior.proximo.anterior = valor_anterior

                            #valor_auxiliar.proximo.anterior

                        self.tamanho -= 1

                        break
                    else:
                        valor_anterior = valor_auxiliar

                        valor_auxiliar = valor_auxiliar.proximo

                if tamanho_inicial == self.tamanho:
                    print( "Valor não encontrado")
                    
                self.imprimir()

            




                    

            
        
