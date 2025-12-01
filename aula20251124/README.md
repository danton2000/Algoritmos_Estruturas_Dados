# AVL (avl_delete.py) - README

Este diretório contém uma implementação didática de uma Árvore AVL em Python (`avl_delete.py`).
O código foi escrito para fins educativos e contém prints e chamadas a `input()` para pausar e
mostrar o estado interno durante inserções, rotações e remoções.

**O que o módulo fornece**
- Classe `No`: representa um nó da árvore (atributos: `valor`, `esquerda`, `direita`, `altura`).
- Classe `ArvoreAVL`: implementação de uma árvore AVL com métodos principais:
  - `adicionar_no(valor)` — insere um valor mantendo o balanceamento.
  - `remover(valor)` — remove um valor e reequilibra a árvore.
  - `imprimir()` — imprime os nós em ordem (para inspeção didática).

**Pontos importantes sobre o código**
- O fator de balanceamento (FB) é calculado como: `FB = altura(direita) - altura(esquerda)`.
  - Valores `FB > 1` indicam subárvore direita pesada; `FB < -1` indica esquerda pesada.
- As rotações implementadas são: rotação simples à esquerda, rotação simples à direita,
  e combinações necessárias (Left-Right, Right-Left) aplicadas no momento adequado.
- Em remoções, quando encontramos um nó com dois filhos, substituímos seu valor pelo
  sucessor inorder (menor valor na subárvore direita) e removemos esse sucessor.

**Observação sobre `input()` e `print()`**
- O código inclui várias chamadas a `input()` para pausar a execução e permitir
  a inspeção passo-a-passo (útil em sala de aula). Para executar automaticamente
  sem pausas, remova (ou comente) as chamadas a `input()`.

**Exemplo de uso (arquivo `test_removal.py`)**
```python
from avl_delete import ArvoreAVL

arv = ArvoreAVL()
for v in [100, 50, 20, 80, 90, 85]:
    arv.adicionar_no(v)

print("Antes:")
arv.imprimir()

# Remove um nó e mostra estado
arv.remover(90)
print("Depois de remover 90:")
arv.imprimir()

arv.remover(100)
print("Depois de remover 100:")
arv.imprimir()
```

**Como executar**
No Windows (PowerShell) a partir da pasta do projeto:

```powershell
cd c:\senac\Algoritmos_Estruturas_Dados\aula20251124
python avl_delete.py
# ou para rodar o teste:
python test_removal.py
```

**Sugestões de próximas etapas**
- Remover ou condicionar as chamadas a `input()` para execução não interativa.
- Adicionar testes unitários que verifiquem a propriedade AVL (altura e balanceamento)
  após sequências de inserções e remoções.
- Implementar métodos adicionais (busca, altura total, percurso por níveis, etc.).

Se quiser, eu posso:
- Remover os `input()` automaticamente (opção para modo `verbose=True/False`).
- Gerar o arquivo `test_removal.py` e/ou testes unitários com `unittest`.
