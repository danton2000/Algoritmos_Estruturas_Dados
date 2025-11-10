# Implementação simples de Árvore AVL (auto-balanceada)
# - Não usa libs externas
# - Método de inserção com balanceamento (rotações)
# - Método de impressão (in-order) para testar

class No:
    """Nó da árvore: guarda valor, ponteiros e altura."""
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1  # altura de nó folha = 1

class AVL:
    """Árvore AVL simples com inserção balanceada."""
    def __init__(self):
        self.raiz = None

    def vazia(self):
        return self.raiz is None

    def adicionar_no(self, valor):
        """Inserção pública: atualiza a raiz com a árvore resultante."""
        if self.vazia():
            self.raiz = No(valor)
        else:
            self.raiz = self._adicionar_no_folha(self.raiz, valor)

    def _adicionar_no_folha(self, no_atual, valor):
        """Inserção recursiva como em BST, atualiza alturas e re-balanceia."""
        if not no_atual:
            return No(valor)
        if valor < no_atual.valor:
            no_atual.esquerda = self._adicionar_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._adicionar_no_folha(no_atual.direita, valor)

        # atualiza altura do nó atual
        no_atual.altura = 1 + max(self._altura(no_atual.esquerda),
                                 self._altura(no_atual.direita))

        # calcula fator de balanceamento (altura(esq) - altura(dir))
        balanceamento = self._balanceamento(no_atual)

        # Caso Left Left
        if balanceamento > 1 and valor < no_atual.esquerda.valor:
            return self._rotacao_direita(no_atual)

        # Caso Right Right
        if balanceamento < -1 and valor > no_atual.direita.valor:
            return self._rotacao_esquerda(no_atual)

        # Caso Left Right
        if balanceamento > 1 and valor > no_atual.esquerda.valor:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Caso Right Left
        if balanceamento < -1 and valor < no_atual.direita.valor:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def _altura(self, no):
        """Retorna altura do nó (0 se None)."""
        if not no:
            return 0
        return no.altura

    def _balanceamento(self, no):
        """Fator = altura(esquerda) - altura(direita)."""
        if not no:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    def _rotacao_direita(self, y):
        """Rotação à direita (y é raiz do subtree desbalanceado)."""
        x = y.esquerda
        T2 = x.direita

        # realizar rotação
        x.direita = y
        y.esquerda = T2

        # atualizar alturas
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))

        # nova raiz do subtree
        return x

    def _rotacao_esquerda(self, x):
        """Rotação à esquerda (x é raiz do subtree desbalanceado)."""
        y = x.direita
        T2 = y.esquerda

        # realizar rotação
        y.esquerda = x
        x.direita = T2

        # atualizar alturas
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))

        # nova raiz do subtree
        return y

    def imprimir_in_order(self):
        """Imprime os valores em ordem (uso para teste)."""
        def _inorder(no):
            return _inorder(no.esquerda) + [no.valor] + _inorder(no.direita) if no else []
        valores = _inorder(self.raiz)
        print(valores)

if __name__ == "__main__":
    # teste simples
    arv = AVL()
    for v in [10, 20, 30, 40, 50, 25]:
        arv.adicionar_no(v)
    print("In-order (deve ficar ordenado):")
    arv.imprimir_in_order()