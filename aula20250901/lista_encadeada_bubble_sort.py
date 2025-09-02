class No:
    """Classe que representa um nó da lista encadeada."""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
class ListaEncadeada:
    """Classe que representa a lista encadeada."""
    def __init__(self):
        self.inicio = None

        self.elementos = []
        
    def inserir(self, valor):
        """Insere um novo nó no final da lista"""
        novo_no = No(valor)
        
        if self.inicio is None:
            self.inicio = novo_no
            
        else:
            atual = self.inicio
            
            # Percorre até o ultimo nó
            while atual.proximo:
                atual = atual.proximo
                
            atual.proximo = novo_no
    
    def exibir(self):
        """Exibe os valores da lista encadeada."""
        atual = self.inicio
        
        
        while atual:
            
            self.elementos.append(atual.valor)
            
            atual = atual.proximo
            
        print(" -> ".join(map(str, self.elementos)))

    def selection_sort(self):

        usar lista elementos
            
            
        
# --- Exemplo de uso das classes ---
if __name__ == "__main__":
    
    lista = ListaEncadeada()
    
    lista.inserir(11)
    
    lista.inserir(4)
    
    lista.inserir(9)
    
    lista.inserir(1)
    
    print("Lista original")
    lista.exibir()

    print("Lista Ordenada com Selection Sort")
   
    lista.selection_sort()
    lista.exibir()

    