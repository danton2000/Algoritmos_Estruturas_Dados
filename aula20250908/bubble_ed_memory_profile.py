"""
Exemplo de lista encadeada + Bubble Sort com medição de memória.

Objetivo (explicação leiga):
- Mostrar como guardar números em uma lista que é feita de "nós" ligados
    um ao outro (cada nó aponta para o próximo).
- Ordenar essa lista usando o método simples Bubble Sort.
- O decorator @profile permite analisar o uso de memória (opcional).

Observação: o algoritmo troca apenas os valores dentro dos nós (mais
simples do que rearranjar os ponteiros).
"""

from memory_profiler import profile
import time

class Node:
    def __init__(self, numero):
        # Cada nó guarda um valor (numero) e a referência para o próximo nó.
        self.valor = numero
        self.next = None

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        novo_no = Node(valor)

        # Adiciona um novo nó ao final da lista.
        # Se a lista estiver vazia, novo nó é head e tail.
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            # Caso haja elementos, liga o último ao novo e atualiza tail.
            self.tail.next = novo_no
            self.tail = novo_no


    def imprime_lista(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            no_atual = self.head
            while no_atual is not None:
                # Percorre do início ao fim imprimindo cada valor.
                print(f"Valor: {no_atual.valor}")
                no_atual = no_atual.next

    @profile
    def ordena_bubble(self):
        # Bubble Sort adaptado para lista encadeada.
        # Se a lista tem 0 ou 1 elemento, já está ordenada.
        if self.head is None or self.head.next is None:
            return

        # `fim` marca o limite direito reduzido a cada passada.
        fim = None

        # Repetir passadas até não haver trocas.
        while fim != self.head:
            atual = self.head
            trocou = False

            # Percorre cada par vizinho até o limite `fim`.
            while atual.next != fim:
                proximo = atual.next
                # Se o par estiver fora de ordem, troca os valores.
                if atual.valor > proximo.valor:
                    atual.valor, proximo.valor = proximo.valor, atual.valor
                    trocou = True
                atual = atual.next

            # Avança o limite para o último nó examinado nesta passada.
            fim = atual

            # Se em uma passada não houve troca, a lista já está ordenada.
            if not trocou:
                break


# lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
import random
lista_desordenada = list(range(1, 500))
random.shuffle(lista_desordenada)
lista = Lista()
for numero in lista_desordenada:
    lista.add_valor(numero)
# print("Lista Desordenada.")
# lista.imprime_lista()
inicio = time.time()
lista.ordena_bubble()
fim = time.time()
print("Lista Ordenada.")
# lista.imprime_lista()

print(f"Tempo de execução: {fim - inicio:.6f} segundos")