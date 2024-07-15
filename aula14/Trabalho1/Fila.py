class Fila:

    def __init__(self):
        
        self.inicio = None

        self.fim = None

        self.tamanho = 0

    def adicionarNaFila(self, apartamento):

        # Nó guardado em memoria
        nodo = apartamento

        print(nodo.id_apartamento)

        if self.inicio == None:

            self.inicio = nodo

        else:

            self.fim.proximo = nodo

        self.fim = nodo

        self.tamanho += 1

    def imprimir(self):
        
        print("---------------------------------------------")
        
        #verificar se a Fila está vazia
        if self.inicio == None:
            
            print("Fila vazia.")
            
        else:
            
            print(f"Fila com {self.tamanho} Apartamento")
            
            valor_auxiliar = self.inicio

            texto = ""
            
            while valor_auxiliar:
                #imprimindo e indo para o proximo

                texto += "Id Apto: " + str(valor_auxiliar.id_apartamento) + " | " + "Vaga: " + str(valor_auxiliar.vaga_garagem) + " - "

                valor_auxiliar = valor_auxiliar.proximo

            print(texto)

    def remover(self):
        
        apto = self.inicio

        if self.inicio:

            self.inicio = self.inicio.proximo

            if self.inicio == None:

                self.fim = None
            
            self.tamanho -= 1
            
        return apto

            

                
                
        