
"""
Fluxo estático (passo a passo) do Insertion Sort em português.

Este script mostra, de forma estática (sem animação), cada comparação
e cada movimento (deslocamento/colocação) que o algoritmo Insertion Sort
realiza sobre uma lista de exemplo. As mensagens foram simplificadas
para facilitar apresentação e cópia em slides.

Uso: execute com o interpretador Python do workspace.
"""

from typing import List


def insertion_sort_trace(arr: List[int]) -> List[str]:
    """Retorna uma lista de linhas explicando passo a passo o processo.

    A função trabalha sobre uma cópia da lista e documenta:
    - o índice e o valor 'chave' (key) sendo considerado;
    - cada comparação com elementos anteriores;
    - cada deslocamento (shift) quando um elemento maior que a chave é
      movido uma posição à frente;
    - a posição final onde a chave é colocada.
    """
    a = arr.copy()
    steps: List[str] = []
    steps.append(f"Início: {a}")

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        steps.append("")
        steps.append(f"Considerando índice {i} (chave = {key}); parte ordenada: {a[:i]}")

        # desloca elementos maiores que a chave para a direita
        while j >= 0 and a[j] > key:
            steps.append(f"Comparar chave={key} com a[{j}]={a[j]} -> maior, desloca a[{j}] para a[{j+1}]")
            a[j + 1] = a[j]
            steps.append(f"Depois do deslocamento: {a}")
            j -= 1

        destino = j + 1
        steps.append(f"Coloca chave={key} na posição {destino}")
        a[destino] = key
        steps.append(f"Estado após inserção: {a}")

    steps.append("")
    steps.append(f"Ordenado: {a}")
    return steps


def demo():
    amostra = [8, 4, 3, 7, 6, 2]
    print("Insertion Sort — fluxo estático (passo a passo)\n")
    print(f"Entrada: {amostra}\n")
    for linha in insertion_sort_trace(amostra):
        print(linha)


if __name__ == '__main__':
    demo()
