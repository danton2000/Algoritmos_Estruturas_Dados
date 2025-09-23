"""
Exemplo de Insertion Sort em lista duplamente encadeada (com muitos prints
de debug para fins didáticos).

Explicação leiga:
- Insertion Sort constrói uma lista ordenada elemento a elemento. Para cada
  novo elemento, deslocamos os elementos maiores para a direita e colocamos
  o novo elemento na posição correta.
"""

import time


class Node:
    def __init__(self, numero):
        # Cada nó guarda um valor e referências para o anterior e o próximo.
        self.valor = numero
        self.next = None
        self.prev = None


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        """Adiciona valor ao final; imprime passos para estudo."""
        novo_no = Node(valor)
        if self.head is None:
            # Lista vazia: head e tail apontam para o novo nó
            self.head = novo_no
            self.tail = novo_no
            #print(f"inicio da lista: {self.head.valor}, fim da lista: {self.tail.valor}")
        else:
            # Anexa no final e atualiza ponteiros prev/next
            self.tail.next = novo_no
            novo_no.prev = self.tail
            #print(f"proximo valor: {self.tail.next.valor}, valor anterior:{novo_no.prev.valor}")

            self.tail = novo_no
            #print(f"fim da lista: {self.tail.valor}")

    def imprime_lista(self):
        """Percorre do inicio ao fim imprimindo os valores."""
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(f"Valor: {atual.valor}")
                atual = atual.next

    def ordena_insertion(self):
        """
        Faz Insertion Sort movendo valores.

        Observação: imagine que você pega cada elemento e o insere na
        posição correta entre os já processados, deslocando os maiores para a
        direita.
        """

        if self.head is None or self.head.next is None:
            return

        # Começa no segundo elemento (o primeiro já está "ordenado").
        atual = self.head.next
        # print(self.head.next.valor)
        # exit()

        # Para cada elemento, deslocamos valores maiores para a direita
        # e inserimos o valor chave na posição correta.
        while atual is not None:

            print(f"inicio lista")
            print(f"valor: {self.head.valor}")
            print(f"proximo: {self.head.next.valor}")
            print(f"anterior: {self.head.prev}")

            print(f"Proximo elemento da lista")
            print(f"valor: {atual.valor}")
            print(f"anterior: {atual.prev.valor}")
        
            print(f"Fim lista")
            print(f"valor: {self.tail.valor}")
            print(f"proximo: {self.tail.next}")
            print(f"anterior: {self.tail.prev.valor}")


            chave = atual.valor
            mover = atual.prev
            # Move elementos maiores uma posição à frente.
            8 é none? e 8 > 3
            while mover is not None and mover.valor > chave:
                mover.next.valor = mover.valor  # move o valor para a frente
                mover = mover.prev

            # Se chegamos ao início, atualiza o head; caso contrário, insere
            # logo após o ponteiro mover.
            if mover is None:
                self.head.valor = chave
            else:
                mover.next.valor = chave

            atual = atual.next

            print(f"inicio lista")
            print(f"valor: {self.head.valor}")
            print(f"proximo: {self.head.next.valor}")
            print(f"anterior: {self.head.prev}")

            print(f"Proximo elemento da lista")
            print(f"valor: {atual.valor}")
            print(f"anterior: {atual.prev.valor}")

            print(f"Fim lista")
            print(f"valor: {self.tail.valor}")
            print(f"proximo: {self.tail.next}")
            print(f"anterior: {self.tail.prev.valor}")
            
            exit()

            print("Lista Ordenada com Insert Sort:(tentativas)")
            lista.imprime_lista()




if __name__ == "__main__":
    lista_desordenada = [8, 3, 5, 9]
    lista = Lista()
    for numero in lista_desordenada:
        lista.add_valor(numero)

    print("Lista Desordenada:")
    lista.imprime_lista()

    print("Lista Ordenada com Insertion Sort:")
    lista.ordena_insertion()
    