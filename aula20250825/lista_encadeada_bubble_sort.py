class No:
    """Classe que representa um nó da lista encadeada."""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
class ListaEncadeada:
    """Classe que representa a lista encadeada."""
    def __init__(self):
        self.inicio = None
        
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
        
        elementos = []
        
        while atual:
            
            elementos.append(atual.valor)
            
            atual = atual.proximo
            
        print(" -> ".join(map(str, elementos)))
        
    def bubble_sort(self):
        """Ordena a lista encadeada usando Bubble Sort(ordem crescente)."""
        
        if self.inicio is None:
            return
        
        trocou = True
        
        while trocou:
            
            trocou = False
            
            atual = self.inicio
            
            while atual.proximo:
                
                if atual.valor > atual.proximo.valor:
                    # Troca os valores
                    atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
                    
                    trocou = True
                    
                atual = atual.proximo

# --- Exemplo de uso das classes ---
if __name__ == "__main__":
    
    lista = ListaEncadeada()
    
    lista.inserir(11)
    
    lista.inserir(5)
    
    lista.inserir(9)
    
    lista.inserir(8)
    
    print("Lista original")
    lista.exibir()
    
    print("Lista ordenando com o Bubble Sort")
    lista.bubble_sort()
    
    lista.exibir()