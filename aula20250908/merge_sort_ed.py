"""
Exemplo de Merge Sort em lista duplamente encadeada.

Explicação leiga:
- Merge Sort divide a lista em metades repetidamente até listas muito
  pequenas (1 elemento), e depois "merge" (junta) essas partes de forma ordenada.
- É eficiente (O(n log n)) e adequado para listas encadeadas.
"""

import time


class Node:
    def __init__(self, numero):
        # Nó com valor e ponteiros para próximo e anterior.
        self.valor = numero
        self.next = None
        self.prev = None


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        """Adiciona um nó no final da lista."""
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            novo_no.prev = self.tail
            self.tail = novo_no

    def imprime_lista(self):
        """Imprime os valores do início ao fim."""
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(f"Valor: {atual.valor}")
                atual = atual.next

    def ordena_merge(self):
        """Entrada para o merge sort; atualiza head e tail ao final."""
        self.head = self._merge_sort(self.head)
        # Atualiza tail e prev depois da ordenação
        atual = self.head
        prev = None
        while atual:
            atual.prev = prev
            prev = atual
            if atual.next is None:
                self.tail = atual
            atual = atual.next

    def _merge_sort(self, head):
        # Caso base: lista vazia ou 1 elemento
        if head is None or head.next is None:
            return head

        meio = self._divide(head)
        esquerda = self._merge_sort(head)
        direita = self._merge_sort(meio)

        return self._merge(esquerda, direita)

    def _divide(self, head):
        """Encontra o meio da lista usando ponteiros lento/rápido."""
        lento = head
        rapido = head

        while rapido.next and rapido.next.next:
            lento = lento.next
            rapido = rapido.next.next

        meio = lento.next
        # Separa as duas metades
        lento.next = None
        if meio:
            meio.prev = None
        return meio

    def _merge(self, esquerda, direita):
        """Junta duas listas ordenadas em uma só ordenada."""
        if esquerda is None:
            return direita
        if direita is None:
            return esquerda

        if esquerda.valor <= direita.valor:
            resultado = esquerda
            resultado.next = self._merge(esquerda.next, direita)
            if resultado.next:
                resultado.next.prev = resultado
        else:
            resultado = direita
            resultado.next = self._merge(esquerda, direita.next)
            if resultado.next:
                resultado.next.prev = resultado

        resultado.prev = None
        return resultado


if __name__ == "__main__":
    lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
    lista = Lista()
    for numero in lista_desordenada:
        lista.add_valor(numero)

    print("Lista Desordenada:")
    lista.imprime_lista()

    lista.ordena_merge()
    print("Lista Ordenada com Merge Sort:")
    lista.imprime_lista()

