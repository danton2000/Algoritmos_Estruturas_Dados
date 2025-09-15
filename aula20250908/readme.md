# Guia leigo: o que fazem os scripts em `aula20250908`

Esta pasta contém vários exemplos de algoritmos de ordenação implementados
usando listas encadeadas (estruturas formadas por "nós" que apontam para
outros nós). Abaixo está uma explicação simples, para que serve cada script
e qual é o objetivo pedagógico.

Arquivos e objetivos:

- `bubble_ed_memory_profile.py`
  - O que faz: cria uma lista encadeada e ordena usando Bubble Sort.
  - Objetivo: entender o funcionamento do Bubble Sort em listas encadeadas
    e (opcionalmente) medir uso de memória com `memory_profiler`.
  - Observação: Bubble Sort é fácil de entender, mas lento para listas grandes.

- `selection_sort_ed.py`
  - O que faz: implementa Selection Sort em uma lista encadeada.
  - Objetivo: mostrar a ideia de encontrar o menor elemento e colocá-lo
    na posição correta repetidamente.

- `insertion_sort_ed.py`
  - O que faz: demonstra Insertion Sort em uma lista duplamente encadeada.
  - Objetivo: entender como inserir cada elemento na posição correta em uma
    lista já parcialmente ordenada.
  - Observação: o script contém prints didáticos para mostrar passo a passo.

- `merge_sort_ed.py`
  - O que faz: implementa Merge Sort em uma lista duplamente encadeada.
  - Objetivo: demonstrar um algoritmo eficiente (O(n log n)) que divide a
    lista e junta as partes ordenadas.

- `quick_sort_ed.py`
  - O que faz: implementa Quick Sort em uma lista duplamente encadeada.
  - Objetivo: estudar divisão (particionamento) em torno de um pivô e ordenar
    recursivamente as partes.

Como executar um script (exemplo):

```bash
python aula20250908/selection_sort_ed.py
```

Dicas rápidas (em linguagem simples):

- Lista encadeada = fila de caixas onde cada caixa sabe onde está a próxima.
- Trocar valores dentro dos nós é mais simples do que trocar os ponteiros
  (reencadear nós). Muitos exemplos aqui trocam apenas valores.
- Bubble/Selection/Insertion são algoritmos fáceis de entender, mas lentos
  para listas grandes. Merge e Quick são mais rápidos na prática.

Se quiser, eu posso:
- Adicionar exemplos passo a passo no README (como as trocas acontecem).
- Criar um menu único que executa qualquer algoritmo para comparar tempos.
- Adicionar pequenos testes automáticos para validar os scripts.
# Entender esses 5 scripts
## Explicar para o Sor