"""
Exemplo com Selection Sort em lista encadeada simples.

Explicação leiga:
- Selection Sort procura o menor elemento a cada iteração e coloca ele
  na posição correta (começando da esquerda). Repetindo esse processo, a
  lista fica ordenada.
"""

import time


class Node:
    def __init__(self, numero):
        self.valor = numero
        self.next = None


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        """Adiciona um nó ao final."""
        novo_no = Node(valor)

        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no


    def imprime_lista(self):
        """Imprime todos os valores da lista do início ao fim."""
        if self.head is None:
            print("A lista está vazia.")
        else:
            no_atual = self.head
            while no_atual is not None:
                print(f"Valor: {no_atual.valor}")
                no_atual = no_atual.next

    def ordena_bubble(self):
        """Mantive a versão de bubble para referência, com comentário."""
        if self.head is None or self.head.next is None:
            return

        fim = None

        while fim != self.head:
            atual = self.head
            trocou = False

            while atual.next != fim:
                proximo = atual.next
                if atual.valor > proximo.valor:
                    atual.valor, proximo.valor = proximo.valor, atual.valor
                    trocou = True
                atual = atual.next

            fim = atual

            if not trocou:
                break

    def ordena_selection(self):
        """Selection Sort que troca apenas os valores dos nós (simples)."""
        atual = self.head
        while atual is not None:
            # encontra o menor valor a partir de 'atual'
            menor = atual
            proximo = atual.next
            while proximo is not None:
                if proximo.valor < menor.valor:
                    menor = proximo
                proximo = proximo.next
            # troca valores se necessário
            if menor != atual:
                atual.valor, menor.valor = menor.valor, atual.valor
            atual = atual.next


if __name__ == "__main__":
    lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
    lista = Lista()
    for numero in lista_desordenada:
        lista.add_valor(numero)

    print("Lista Desordenada.")
    lista.imprime_lista()

    lista.ordena_selection()
    print("Lista Ordenada.")
    lista.imprime_lista()


