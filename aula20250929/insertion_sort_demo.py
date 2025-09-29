"""
Demonstração passo a passo do Insertion Sort em uma lista duplamente encadeada.
Uso: python aula20250908/insertion_sort_demo.py

O script mostra o estado da lista antes de processar cada elemento, as
comparações/movimentos feitos e o estado após inserir a chave.
"""

from typing import Optional


class Node:
    def __init__(self, valor: int):
        self.valor = valor
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

    def __repr__(self):
        return str(self.valor)


class ListaDupla:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add_valor(self, valor: int):
        novo = Node(valor)
        if self.head is None:
            self.head = novo
            self.tail = novo
        else:
            self.tail.next = novo
            novo.prev = self.tail
            self.tail = novo

    def to_list(self):
        """Retorna os valores em uma lista Python (para imprimir facilmente)."""
        res = []
        cur = self.head
        while cur:
            res.append(cur.valor)
            cur = cur.next
        return res

    def imprime(self):
        print(" -> ".join(map(str, self.to_list())))

    def insertion_sort_step_by_step(self, pause=False):
        """
        Executa insertion sort mostrando cada passo:
        - antes de processar cada chave, imprime a lista e a chave atual
        - mostra movimentos (quando copia valores para a frente)
        - mostra a lista após inserir a chave
        """
        if self.head is None or self.head.next is None:
            print("Lista muito pequena para ordenar.")
            return

        atual = self.head.next
        pos = 1
        while atual is not None:
            chave = atual.valor
            mover = atual.prev

            print(f"\nPasso {pos}: processando chave = {chave}")
            print("Antes:", end=" ")
            self.imprime()

            # desloca valores maiores para a direita
            movimentos = 0
            while mover is not None and mover.valor > chave:
                print(f"  mover {mover.valor} para a frente (posição de {mover.next.valor})")
                mover.next.valor = mover.valor
                mover = mover.prev
                movimentos += 1

            if mover is None:
                print(f"  inserir {chave} no inicio")
                self.head.valor = chave
            else:
                print(f"  inserir {chave} após {mover.valor}")
                mover.next.valor = chave

            print("Depois:", end=" ")
            self.imprime()

            if pause:
                input("Pressione Enter para continuar...")

            atual = atual.next
            pos += 1


if __name__ == '__main__':
    exemplo = [8, 3, 5, 9]
    lista = ListaDupla()
    for v in exemplo:
        lista.add_valor(v)

    print("Lista inicial:")
    lista.imprime()

    lista.insertion_sort_step_by_step(pause=False)

    print("\nLista final ordenada:")
    lista.imprime()
