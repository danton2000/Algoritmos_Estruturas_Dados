"""Módulo simples de Árvore AVL com documentação em português.

Este arquivo contém uma implementação didática de uma Árvore AVL
com operações básicas de inserção e visualização. O código inclui
impressões e `input()` para passos de depuração/visualização usados
em sala de aula — não é otimizado para produção.
"""


class No:
    """Nó da árvore.

    Atributos:
    - `valor`: valor armazenado no nó.
    - `esquerda`: referência para o filho esquerdo (ou None).
    - `direita`: referência para o filho direito (ou None).
    - `altura`: altura do nó na árvore (1 para folha).
    """

    def __init__(self, valor):
        self.esquerda = None
        self.valor = valor
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    """Classe que representa uma Árvore AVL.

    Métodos principais:
    - `adicionar_no(valor)`: insere um novo nó mantendo balanceamento AVL.
    - `imprimir()`: percorre a árvore em ordem e imprime cada nó.

    Observação: muitos `print` e `input` são usados para mostrar estados
    intermediários durante a execução (útil para ensino).
    """

    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        """Retorna True se a árvore estiver vazia."""
        if self.raiz is None:
            return True
        return False

    def adicionar_no(self, valor):
        """Insere `valor` na árvore. Se estiver vazia, cria a raiz.

        Caso contrário, delega a inserção recursiva ao método
        `_adicionar_no_folha` que também realiza rotações quando
        necessário para manter o balanceamento AVL.
        """
        if self.vazia():
            novo_No = No(valor)  # cria primeiro nó como raiz
            # Exibição didática do nó criado
            input( f"Primeiro No: {str(novo_No)[-5:]} "
                   f"-- Valor: {str(novo_No.valor)}  Altura: {str(novo_No.altura)}  "
                   f"Esq.{str(novo_No.esquerda)[-5:]}  Dir.{str(novo_No.direita)[-5:]}\nEnter")
            self.raiz = novo_No
        else:
            print(f"----- Adicionando Nó Folha: {valor} ------")
            self.raiz = self._adicionar_no_folha(self.raiz, valor)

    def _adicionar_no_folha(self, no_atual, valor):
        # Exibição do nó atual para depuração/visualização
        input(f">>> NoAtual: {str(no_atual)}")
        # Caso base: encontrou posição para inserir o novo nó
        if not no_atual:
            novo_No = No(valor)
            print( f"    NovoNo: {str(novo_No)[-5:]} "
                   f"-- Esq.{str(novo_No.esquerda)[-5:]} Valor: {str(novo_No.valor)}  Dir.{str(novo_No.direita)[-5:]}"
                   f"   Altura {str(novo_No.altura)}")
            return novo_No

        # Percorre à esquerda ou à direita conforme o valor
        elif valor < no_atual.valor:
            no_atual.esquerda = self._adicionar_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._adicionar_no_folha(no_atual.direita, valor)

        # Atualiza altura após inserção dos filhos
        no_atual.altura = 1 + max(
            self._altura(no_atual.esquerda),
            self._altura(no_atual.direita)
        )

        input(f"    NoAtual {str(no_atual.valor)}  Altura: {no_atual.altura}")

        # Calcula fator de balanceamento (FB = altura(direita) - altura(esquerda))
        balanceamento = self._balanceamento(no_atual)
        input(f"   FB: {str(balanceamento)}")

        # Caso de rotação: FB < -1 -> subárvore esquerda pesada
        if balanceamento < -1:
            # Caso Left-Left
            if valor < no_atual.esquerda.valor:
                input("Fazer Rotação a Direita +")
                return self._rotacao_direita(no_atual)
            # Caso Left-Right
            else:
                input("Fazer Rotação a Esquerda +")
                no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
                return self._rotacao_direita(no_atual)

        # FB > 1 -> subárvore direita pesada
        if balanceamento > 1:
            # Caso Right-Right
            if valor > no_atual.direita.valor:
                input("Fazer Rotação a Direita em -")
                return self._rotacao_esquerda(no_atual)
            # Caso Right-Left
            else:
                input("Fazer Rotação a Esquerda em -")
                no_atual.direita = self._rotacao_direita(no_atual.direita)
                return self._rotacao_esquerda(no_atual)

        # Se já está balanceado, retorna o nó atualizado
        return no_atual

    def _altura(self, no):
        """Retorna a altura do nó; 0 quando o nó é None."""
        if not no:
            return 0
        return no.altura

    def _balanceamento(self, no):
        """Calcula o fator de balanceamento do nó.

        Convenção usada aqui: FB = altura(direita) - altura(esquerda).
        Valores fora do intervalo [-1, 1] indicam necessidade de rotação.
        """
        if not no:
            return 0
        fb = self._altura(no.direita) - self._altura(no.esquerda)
        return fb

    def _rotacao_esquerda(self, pai):
        filhoD = pai.direita
        neto = filhoD.esquerda

        print("Antes da Rotacao Esquerda")
        print(
            f"   : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"   : {str(filhoD)[-5:]} -- Esq.{str(filhoD.esquerda)[-5:]} Valor: {str(filhoD.valor)}  Dir.{str(filhoD.direita)[-5:]}")

        # Rotação simples à esquerda
        filhoD.esquerda = pai
        pai.direita = neto

        print("Apos da Rotacao Esquerda")
        print(
            f"   : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"   : {str(filhoD)[-5:]} -- Esq.{str(filhoD.esquerda)[-5:]} Valor: {str(filhoD.valor)}  Dir.{str(filhoD.direita)[-5:]}")

        pai.altura = 1 + max(
            self._altura(pai.esquerda),
            self._altura(pai.direita))
        filhoD.altura = 1 + max(
            self._altura(filhoD.esquerda),
            self._altura(filhoD.direita))

        input("Enter")

        return filhoD

    def _rotacao_direita(self, pai):
        filhoE = pai.esquerda
        neto = filhoE.direita

        print("Antes da Rotacao Direita")
        print(
            f"    : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"    : {str(filhoE)[-5:]} -- Esq.{str(filhoE.esquerda)[-5:]} Valor: {str(filhoE.valor)}  Dir.{str(filhoE.direita)[-5:]}")

        # Rotação simples à direita
        filhoE.direita = pai
        pai.esquerda = neto

        print("Após da Rotacao Direita")
        print(
            f"    : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"    : {str(filhoE)[-5:]} -- Esq.{str(filhoE.esquerda)[-5:]} Valor: {str(filhoE.valor)}  Dir.{str(filhoE.direita)[-5:]}")

        pai.altura = 1 + max(
            self._altura(pai.esquerda),
            self._altura(pai.direita))
        filhoE.altura = 1 + max(
            self._altura(filhoE.esquerda),
            self._altura(filhoE.direita))
        input("Enter")
        return filhoE

    def imprimir(self):
        """Imprime a árvore em ordem (esquerda, nó, direita)."""
        if self.vazia():
            print("========== Árvore vazia ==========")
            return
        print("\n=============== Árvore ================")
        self._imprimir(self.raiz)
        print("=========================================\n")

    def _imprimir(self, no_atual):
        if no_atual is not None:
            self._imprimir(no_atual.esquerda)
            print(f"Nó: {str(no_atual)[-5:]} -- Esq.{str(no_atual.esquerda)[-5:]} Valor: {str(no_atual.valor)}  Dir.{str(no_atual.direita)[-5:]} Alt.{str(no_atual.altura)}")
            self._imprimir(no_atual.direita)

#################################

def popular_arvore(arvore):
    """Função auxiliar para popular a árvore com valores de exemplo.

    A lista usada é apenas um conjunto de valores para demonstrar rotações
    e balanceamento durante as inserções.
    """
    lista_entradas = [100, 50, 20, 80, 90, 85]
    for e in lista_entradas:
        arvore.imprimir()
        arvore.adicionar_no(e)

    print("\nÁrvore completa")
    arvore.imprimir()




if __name__ == '__main__':
    # Exemplo de execução quando o módulo é executado diretamente.
    arvore = ArvoreAVL()
    popular_arvore(arvore)



