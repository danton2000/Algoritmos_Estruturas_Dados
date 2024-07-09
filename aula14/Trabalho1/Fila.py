class Fila:

    def __init__(self):
        
        self.inicio = None

        self.fim = None

        self.tamanho = 0

    def adicionarNaFila(self, apartamento):

        # Nó guardado em memoria
        nodo = apartamento

        print(nodo)

        if self.inicio == None:

            self.inicio = nodo

        else:

            self.fim.proximo = nodo

        self.fim = nodo

        self.tamanho += 1

        self.imprimir()

    def imprimir(self):
        
        print("---------------------------------------------")
        
        #verificar se a Fila está vazia
        if self.inicio == None:
            
            print("Fila vazia.")
            
        else:
            
            print(f"Fila com {self.tamanho} elementos")
            
            valor_auxiliar = self.inicio

            texto = ""
            
            while valor_auxiliar:
                #imprimindo e indo para o proximo

                texto += str(valor_auxiliar.id_apartamento) + " - "

                valor_auxiliar = valor_auxiliar.proximo

            print(texto)

    def remover(self):

        if self.inicio:

            self.inicio = self.inicio.proximo

            if self.inicio == None:

                self.fim = None
            
            self.tamanho -= 1

            

                
                
        