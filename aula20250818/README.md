## TurmaEncadeada — explicação prática

Este repositório contém uma implementação simples de uma lista encadeada
para gerenciar uma turma de alunos em `aula20250818/notas_listas_pesquisa_binaria.py`.

O objetivo deste README é explicar, de forma prática e direta, como o código
funciona e como você pode testá-lo rapidamente.

### Estrutura principal

- `NoAluno` — representa um nó da lista. Cada nó tem:
  - `nome` (str)
  - `matricula` (int)
  - `nota` (float)
  - `proximo` (ponteiro para o próximo nó, ou `None`)

- `TurmaEncadeada` — gerencia a lista ligada com duas referências úteis:
  - `inicio` — primeiro nó da lista
  - `final` — último nó da lista (permite inserir no fim em O(1))

### Métodos importantes

- `inserir_aluno(nome, matricula, nota)`
  - Cria um `NoAluno` e anexa ao final da lista.
  - Se a lista estiver vazia, atualiza `inicio` e `final` para o novo nó.

- `busca_sequencial_matricula(matricula_busca)`
  - Percorre a lista do `inicio` até o fim.
  - Retorna uma tupla `(no_encontrado, comparacoes)` onde `no_encontrado`
    é o objeto `NoAluno` (ou `None` se não houver correspondência) e
    `comparacoes` é o número de nós verificados.

- `busca_sequencial_nome(nome_busca)`
  - Procura por nome (ignora maiúsculas/minúsculas).
  - Retorna `(lista_de_nos_encontrados, comparacoes)`; pode haver múltiplos
    alunos com o mesmo nome.

- `ordenar_por_nota()`
  - Estratégia simples: coleta todos os nós numa lista Python, usa
    `list.sort(key=lambda no: no.nota, reverse=True)` e reconstrói a lista
    encadeada na ordem decrescente de nota.
  - Não cria novos nós — apenas rearranja os ponteiros.

### Como executar (exemplo rápido)

1. Abra um terminal na pasta raiz do projeto (`c:\senac\Algoritmos_Estruturas_Dados`).
2. Execute o arquivo:

```bash
python aula20250818/notas_listas_pesquisa_binaria.py
```

Você verá um menu com as opções:
- 1: Buscar aluno por matrícula
- 2: Inserir novo aluno
- 3: Ordenar alunos por nota (maior -> menor)
- 4: Buscar aluno por nome
- 5: Sair

Dica: No modo interativo, as matrículas usadas nos dados iniciais são 1001..1005.

### Exemplo prático

- Inserir aluno: escolha opção `2`, digite nome, matrícula e nota. A função
  `inserir_aluno` adiciona o aluno no fim da lista.
- Buscar por matrícula: opção `1` e digite `1003` — o programa retorna o aluno
  com matrícula 1003 e o número de comparações feitas.
- Ordenar por nota: opção `3` — a lista será reorganizada e exibida em ordem
  decrescente de nota.

### Complexidade (resumo)

- Inserir no fim: O(1)
- Busca sequencial (nome ou matrícula): O(n) no pior caso
- Ordenação (usando list.sort): O(n log n)

### Próximos passos sugeridos

- Adicionar funções de remoção e atualização de aluno.
- Implementar testes automáticos simples (módulo `unittest`) para validar
  inserção, busca e ordenação.

Se quiser, eu posso gerar exemplos de testes ou adicionar comentários inline no
arquivo `notas_listas_pesquisa_binaria.py` para facilitar ainda mais a leitura.
