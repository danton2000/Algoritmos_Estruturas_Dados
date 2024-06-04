# Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função para inserir elementos em ordem alfabética, uma função para imprimir os elementos da lista e uma função para imprimir os elementos na ordem inversa.

"""
class Node:
    
    # Classe que representa um nó da lista duplamente encadeada.
    
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    
    # Classe que representa a lista duplamente encadeada.
    
    def __init__(self):
        self.head = None

    def insert_in_order(self, data):
        
        # Insere um novo nó na lista em ordem alfabética.
        
        new_node = Node(data)
        
        # Se a lista está vazia
        if self.head is None:
            self.head = new_node
            return

        # Se o novo nó
        # Se o novo nó deve ser o primeiro (menor que o head)
        if self.head.data >= new_node.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        # Encontra a posição correta para o novo nó
        current = self.head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        # Insere o novo nó na posição encontrada
        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

    def print_list(self):
        
        # Imprime os elementos da lista na ordem.
        
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()  # Nova linha após a impressão

    def print_list_reverse(self):
        
        # Imprime os elementos da lista na ordem inversa.
        
        current = self.head
        if not current:
            return
        
        # Navega até o último nó
        while current.next:
            current = current.next
        
        # Imprime do último para o primeiro
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()  # Nova linha após a impressão

> Exemplo de uso:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    elementos = ["banana", "maçã", "laranja", "uva", "abacaxi"]
    
    for elemento in elementos:
        dll.insert_in_order(elemento)
    
    print("Elementos na ordem alfabética:")
    dll.print_list()
    
    print("Elementos na ordem inversa:")
    dll.print_list_reverse()
"""

# Explicação do Código
## Classe Node:

Representa um nó da lista duplamente encadeada.
Contém um valor (data), um ponteiro para o próximo nó (next) e um ponteiro para o nó anterior (prev).
Classe DoublyLinkedList:

Representa a lista duplamente encadeada.
Contém um ponteiro para o primeiro nó da lista (head).

## Métodos principais:
insert_in_order(data): Insere um novo nó em ordem alfabética.

print_list(): Imprime os elementos da lista na ordem.

print_list_reverse(): Imprime os elementos da lista na ordem inversa.

Inserção em Ordem Alfabética:

Se a lista está vazia, o novo nó se torna o head.
Se o novo nó deve ser o primeiro, ajusta o head para o novo nó.
Encontra a posição correta para inserir o novo nó percorrendo a lista e insere na posição correta, ajustando os ponteiros next e prev conforme necessário.
Impressão dos Elementos:

print_list(): Percorre a lista do head até o final e imprime os valores.

print_list_reverse(): Navega até o último nó e percorre a lista para trás, imprimindo os valores.

