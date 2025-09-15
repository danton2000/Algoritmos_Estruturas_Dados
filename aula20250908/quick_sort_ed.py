"""
Exemplo de Quick Sort em lista duplamente encadeada.

Explicação leiga:
- Quick Sort escolhe um pivô (aqui usamos o último elemento) e rearranja
  os elementos de forma que valores menores que o pivô fiquem à esquerda
  e os maiores à direita; após isso, aplica recursivamente o mesmo processo
  nas sublistas.
"""

import time


class Node:
    def __init__(self, numero):
        self.valor = numero
        self.next = None
        self.prev = None


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        """Adiciona um nó ao final da lista."""
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            novo_no.prev = self.tail
            self.tail = novo_no

    def imprime_lista(self):
        """Imprime do início ao fim."""
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(f"Valor: {atual.valor}")
                atual = atual.next


    def ordena_quick(self):
        """Inicia o Quick Sort usando head e tail como limites."""
        self._quick_sort(self.head, self.tail)

    def _quick_sort(self, inicio, fim):
        # Condição de parada: sublista vazia ou com 1 elemento
        if inicio is not None and fim is not None and inicio != fim and inicio != fim.next:
            pivo = self._particiona(inicio, fim)
            # Ordena recursivamente as duas metades
            self._quick_sort(inicio, pivo.prev)
            self._quick_sort(pivo.next, fim)

    def _particiona(self, inicio, fim):
        """Particiona a sublista usando 'fim' como pivô (troca valores)."""
        pivo_valor = fim.valor
        i = inicio.prev
        j = inicio

        # Move pela sublista e coloca valores menores que o pivô antes
        while j != fim:
            if j.valor <= pivo_valor:
                i = i.next if i else inicio
                # troca os valores entre i e j
                i.valor, j.valor = j.valor, i.valor
            j = j.next

        # Coloca o pivô na posição correta (i+1)
        i = i.next if i else inicio
        i.valor, fim.valor = fim.valor, i.valor
        return i


if __name__ == "__main__":
    lista = Lista()
    for numero in [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]:
        lista.add_valor(numero)

    print("Lista Desordenada:")
    lista.imprime_lista()
    lista.ordena_quick()
    print("Lista Ordenada com Quick Sort:")
    lista.imprime_lista()

