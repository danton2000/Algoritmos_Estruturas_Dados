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

- `Radix_Sort.py`

  - O que faz: implementa o Radix Sort usando uma estrutura de lista encadeada. O
  script converte a lista encadeada para uma lista normal para aplicar o
  Counting Sort por dígito (unidade, dezena, centena...), reconstruindo a lista
  encadeada a cada passagem.

  - Objetivo: demonstrar um algoritmo de ordenação por distribuição (não por
  comparação) que é eficiente quando os números têm tamanho limitado (por
  exemplo, números inteiros com poucas casas). É útil para mostrar como dividir
  o problema por dígitos e usar um Counting Sort estável para ordenar por cada
  posição decimal.

  - Observação:
    - O algoritmo no script converte entre lista encadeada e lista Python para
    simplificar a implementação; isso facilita a compreensão, mas, em termos de
    desempenho prático, a conversão tem custo extra.
    - Radix Sort é eficiente quando os valores têm faixa limitada e quando o
    custo por dígito (k) é pequeno — a complexidade típica é O(n * k).
    - O script inclui um exemplo fixo (uma pequena "base de sorteios") para
    demonstrar o funcionamento e imprimir listas ordenadas por concurso.

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
## colocar mais detalhes, como nó, ultimos numeros do endereço da memoria, valores alterados

## mostrar a apresentacao mais o fluxo
