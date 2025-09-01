# Lista Encadeada com Bubble Sort (aula20250825)

Este diretório contém um exemplo simples em Python que mostra como:

- construir uma lista encadeada (singly linked list),
- inserir elementos no final da lista,
- exibir a lista,
- ordenar a lista usando o algoritmo Bubble Sort.

O arquivo principal é `lista_encadeada_bubble_sort.py`.

## O que este código faz (explicação leiga)

Imagine uma fila de caixas, onde cada caixa guarda um número e um bilhete
com a indicação da próxima caixa. Essa é a "lista encadeada": cada caixa
(sinalizada por `No`) tem um valor e sabe onde está a próxima caixa (`proximo`).

O programa permite:

- Colocar números no final da fila (inserir),
- Ver todos os números na ordem atual (exibir),
- Ordenar os números em ordem crescente usando um método simples chamado
  Bubble Sort (que compara cada par de caixas vizinhas e troca quando estão na ordem errada).

## Como o código está organizado (passo a passo)

1. Classe `No` — representa uma caixa com `valor` e um link `proximo`.
2. Classe `ListaEncadeada` — representa a fila de caixas e tem:
   - `inserir(valor)`: insere um novo nó no final da lista;
   - `exibir()`: monta e imprime a sequência de valores na lista;
   - `bubble_sort()`: ordena os valores da lista em ordem crescente usando Bubble Sort.
3. Exemplo Bubble Sort:
    Exemplo passo a passo com [11, 5, 9, 8]:

    - Passada 1:
    compara 11 e 5 → 11>5 → troca → [5, 11, 9, 8]
    compara 11 e 9 → 11>9 → troca → [5, 9, 11, 8]
    compara 11 e 8 → 11>8 → troca → [5, 9, 8, 11]
    trocou = True (faz outra passada)
    - Passada 2:
    compara 5 e 9 → já ok
    compara 9 e 8 → 9>8 → troca → [5, 8, 9, 11]
    compara 9 e 11 → ok
    trocou = True (faz outra passada)
    - Passada 3:
    percorre todas as comparações, nenhuma troca → trocou = False → para
    Lista final: [5, 8, 9, 11]

Observação: o Bubble Sort aqui troca os valores dentro dos nós (não mexe nos links),
por simplicidade.

## Como executar

Abra um terminal na raiz do projeto e execute:

```bash
python aula20250825/lista_encadeada_bubble_sort.py
```

Você verá algo como:

```
Lista original
11 -> 5 -> 9 -> 8
Lista ordenando com o Bubble Sort
5 -> 8 -> 9 -> 11
```

## Notas importantes (dicas rápidas)

- A lista encadeada é útil quando você quer inserir ou remover itens com
  facilidade sem precisar mover todos os elementos, mas percorrer a lista
  para acessar posições intermediárias é mais lento do que em uma lista Python.
- O Bubble Sort é fácil de entender, mas é lento para listas grandes (O(n^2)).
- Aqui o código troca apenas os valores dos nós, uma forma simples de ordenar
  sem reencadear ponteiros.
