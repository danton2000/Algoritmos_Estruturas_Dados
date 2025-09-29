"""
Demo visual do Insertion Sort em lista duplamente encadeada.
Mostra barras ASCII coloridas representando os valores e anima passo a passo.

Uso:
    python aula20250908/insertion_sort_visual.py

Pressione Ctrl+C para interromper a animação a qualquer momento.
"""

import time
import os
import sys
from typing import Optional

# Códigos ANSI para cores simples
RESET = "\u001b[0m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
CYAN = "\u001b[36m"


class Node:
    def __init__(self, valor: int):
        self.valor = valor
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class ListaDupla:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add(self, valor: int):
        novo = Node(valor)
        if self.head is None:
            self.head = novo
            self.tail = novo
        else:
            self.tail.next = novo
            novo.prev = self.tail
            self.tail = novo

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.valor)
            cur = cur.next
        return out

    def length(self):
        n = 0
        cur = self.head
        while cur:
            n += 1
            cur = cur.next
        return n


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_bars(vals, highlight_idx=None, highlight2_idx=None):
    # mapa simples de valor -> largura
    maxv = max(vals) if vals else 1
    scale = max(1, 40 // maxv)

    lines = []
    for i, v in enumerate(vals):
        width = max(1, v * scale)
        bar = '█' * width
        color = RESET
        if i == highlight_idx:
            color = RED
        elif i == highlight2_idx:
            color = CYAN
        # mostra a barra seguida do valor entre parênteses para ficar claro
        # qual número ela representa
        lines.append(f"{color}{bar}{RESET}({v})")
    # junta com espaçamento
    print(' '.join(lines))


def insertion_sort_visual(lista: ListaDupla, delay=0.8):
    if lista.head is None or lista.head.next is None:
        return

    atual = lista.head.next
    idx = 1
    while atual:
        chave = atual.valor
        mover = atual.prev

        vals_before = lista.to_list()
        clear()
        print(f"Passo {idx} - chave={chave} (antes)")
        draw_bars(vals_before, highlight_idx=idx)
        time.sleep(delay)

        # deslocamento visual
        while mover is not None and mover.valor > chave:
            mover.next.valor = mover.valor
            mover = mover.prev

            vals_mid = lista.to_list()
            clear()
            print(f"Passo {idx} - deslocando")
            draw_bars(vals_mid, highlight_idx=idx, highlight2_idx=(idx-1 if idx-1>=0 else None))
            time.sleep(delay/2)

        if mover is None:
            lista.head.valor = chave
        else:
            mover.next.valor = chave

        vals_after = lista.to_list()
        clear()
        print(f"Passo {idx} - depois")
        draw_bars(vals_after)
        time.sleep(delay)

        atual = atual.next
        idx += 1


if __name__ == '__main__':
    exemplo = [8, 3, 5, 9]
    l = ListaDupla()
    for v in exemplo:
        l.add(v)

    try:
        insertion_sort_visual(l, delay=0.9)
    except KeyboardInterrupt:
        print('\nInterrompido pelo usuário')
    finally:
        print('\nResultado final:')
        print(l.to_list())
