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
        
    def selection_sort(self):
        """
        Ordena a lista encadeada em ordem crescente usando Selection Sort.

        Estratégia (versão simples que troca valores dentro dos nós):
        - Para cada posição da lista (nó `i`), encontra o nó com o menor
          valor entre `i` e o final.
        - Troca o valor do nó `i` com o valor do nó que contém o mínimo.

        Observações:
        - Mantemos a simplicidade trocando apenas os valores dos nós em vez
          de reencadear ponteiros.
        - Complexidade: O(n^2) no pior caso e no caso médio.
        """
        if self.inicio is None:
            return

        i = self.inicio
        # 'i' representa a posição atual que vamos preencher com o menor valor
        while i:
            # Encontrar o nó com o menor valor a partir de i
            menor = i
            j = i.proximo
            while j:
                if j.valor < menor.valor:
                    menor = j
                j = j.proximo

            # Se menor for diferente de i, troca os valores
            if menor is not i:
                i.valor, menor.valor = menor.valor, i.valor

            # Avança para a próxima posição
            i = i.proximo

# --- Exemplo de uso das classes ---
if __name__ == "__main__":
    
    lista = ListaEncadeada()
    
    lista.inserir(11)
    
    lista.inserir(5)
    
    lista.inserir(9)
    
    lista.inserir(8)
    
    print("Lista original")
    lista.exibir()

    print("Lista ordenando com o Selection Sort")
    lista.selection_sort()

    lista.exibir()