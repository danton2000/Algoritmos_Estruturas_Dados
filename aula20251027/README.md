# Jogo de Damas (aula20251027/jogocomtkinterV2.py)

Este README resume de forma prática e objetiva o que o script `jogocomtkinterV2.py` faz, quais estruturas de dados ele usa, como executar e quais são as limitações e possíveis melhorias.

## O que o script faz

- Implementa uma versão didática do jogo de damas com interface gráfica em Tkinter.
- Permite ao usuário selecionar origem e destino com cliques no tabuleiro, alternar entre MOVIMENTO (1 casa diagonal) e CAPTURA (2 casas diagonal), e visualizar um histórico/árvore das jogadas.
- Registra as jogadas em duas estruturas: uma lista linear (`todas_jogadas`) e uma árvore binária simples (`ArvoreDeJogadas`) onde cada nó é um objeto `Jogada`.

## Estruturas de dados principais

- Tabuleiro: lista de listas 8x8 (matriz). Cada célula contém:
  - `None` — casa vazia
  - `'P'` — peça preta
  - `'B'` — peça branca
  Acesso: `tabuleiro[linha][coluna]`.

- Jogada: objeto com campos
  - `origem` (linha, coluna)
  - `destino` (linha, coluna)
  - `tipo` (`'movimento'` ou `'captura'`)
  - `filho_esquerdo` e `filho_direito` — referências para formar a árvore de sequências

- Árvore de jogadas (`ArvoreDeJogadas`): cada nó é um `Jogada`. A inserção tenta encaixar a nova jogada em um nó existente quando `nó.destino == nova_jogada.origem`:
  - movimentos -> `filho_esquerdo`
  - capturas   -> `filho_direito`
  Essa árvore funciona como um histórico hierárquico de sequências.

- Lista de jogadas: `todas_jogadas` armazena todas as jogadas na ordem em que foram executadas (lista linear).

## Fluxo de execução (simplificado)

1. O jogo inicializa o tabuleiro com peças:
   - Linhas 0..2: peças pretas (`'P'`) em casas escuras
   - Linhas 5..7: peças brancas (`'B'`) em casas escuras
2. O usuário clica no tabuleiro para selecionar origem e depois destino.
3. O código valida a jogada (`validar_jogada`) — limites, casa preta, destino vazio, diagonal e distância (1 ou 2) e, se captura, existência de peça adversária no meio.
4. Se válida, o jogo move a peça na matriz, remove peça capturada se houver, cria um objeto `Jogada`, insere na árvore e na lista, alterna jogador e atualiza a interface.

## Como executar

Requisitos mínimos:
- Python 3.x (não usa dependências externas além do Tkinter, que normalmente já vem com Python em ambientes padrão).

Com o terminal (bash ou cmd) aberto na raiz do repositório, execute:

```bash
python aula20251027/jogocomtkinterV2.py
```

Observação: o script abre uma janela GUI — execute em um ambiente com interface gráfica.

## Como jogar (uso rápido)

- Clique em uma peça sua (P ou B) para selecionar a origem.
- Clique na casa destino.
- Antes de clicar em destino, escolha o botão `MOVIMENTO` (1 casa diagonal) ou `CAPTURA` (2 casas diagonal).
- A área lateral (`🌳 ÁRVORE DE JOGADAS`) registra a árvore visualmente; o botão `TODAS JOGADAS` mostra um log textual.

## Limitações conhecidas

- Não há coroação (promoção para dama) nem movimentos de dama.
- Não há obrigatoriedade de captura (usuário escolhe tipo manualmente).
- Não há movimentos múltiplos automáticos (capturas sequenciais devem ser feitas manualmente).
- Validação não distingue direção (peças podem mover em qualquer diagonal, sem restrição de "avançar").
- Inserção na árvore faz uma busca recursiva que no pior caso pode ser O(n).

## Melhorias simples sugeridas

- Implementar coroação (promover peça a dama quando atinge a última linha).
- Forçar captura quando houver possibilidade (regra comum em damas).
- Permitir múltiplas capturas em uma só jogada automaticamente.
- Substituir strings `'P'`/`'B'` por objetos `Peca` para facilitar extensão (e.g., propriedade `dama`).
- Otimizar inserção na árvore mantendo um dicionário que mapeie destinos para nós (reduz busca de O(n) para O(1)).

## Arquivos relacionados
- `aula20251027/jogocomtkinterV2.py` — código principal do jogo (GUI + lógica).
