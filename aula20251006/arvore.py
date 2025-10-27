"""arvore.py

Implementação simples e comentada de uma árvore genérica (cada nó pode
ter vários filhos). O arquivo substitui versões anteriores confusas e
coloca comentários práticos e objetivos em português.

Funcionalidade fornecida:
- criar nós
- adicionar nós (sob um pai indicado)
- buscar nó por valor
- imprimir a árvore em forma hierárquica
- modo interativo simples e modo demo não interativo

Não usa bibliotecas externas.
"""

import os
from typing import Optional


class No:
    """Nó da árvore: guarda um valor e uma lista de filhos."""

    def __init__(self, valor):
        # valor armazenado no nó (string ou número)
        self.valor = valor
        # lista de filhos (inicialmente vazia)
        self.filhos = []

    def adicionar_filho(self, filho: 'No'):
        """Adiciona um nó filho ao final da lista de filhos."""
        self.filhos.append(filho)


class Arvore:
    """Árvore genérica com operações básicas.

    Métodos principais:
    - vazia(): verifica se há raiz
    - buscar(valor): encontra nó com o valor
    - adicionar_no(valor, pai_valor): adiciona nó sob pai
    - imprimir(): mostra árvore indentada
    """

    def __init__(self, raiz: Optional[No] = None):
        self.raiz = raiz

    def vazia(self) -> bool:
        """Retorna True se a árvore não tem raiz."""
        return self.raiz is None

    def buscar(self, valor) -> Optional[No]:
        """Busca um nó pelo valor (pré-ordem). Retorna o nó ou None."""

        def _buscar(no: Optional[No]) -> Optional[No]:
            if no is None:
                return None
            if no.valor == valor:
                return no
            # procura recursivamente em cada filho
            for f in no.filhos:
                res = _buscar(f)
                if res is not None:
                    return res
            return None

        return _buscar(self.raiz)

    def adicionar_no(self, valor, pai_valor: Optional[str] = None) -> No:
        """Adiciona um novo nó.

        Regras simples:
        - se a árvore estiver vazia e pai_valor for None -> novo nó vira raiz
        - se pai_valor for None e árvore não vazia -> anexa ao raiz
        - se pai_valor informado -> busca o pai e anexa como filho
        - se pai não existir -> ValueError
        """
        novo = No(valor)

        if self.vazia():
            if pai_valor is not None:
                # não faz sentido informar pai quando não há raiz
                raise ValueError('Árvore vazia: não pode informar pai.')
            self.raiz = novo
            return novo

        # se não informou pai, anexa ao raiz
        if pai_valor is None:
            self.raiz.adicionar_filho(novo)
            return novo

        pai = self.buscar(pai_valor)
        if pai is None:
            raise ValueError(f"Pai '{pai_valor}' não encontrado.")
        pai.adicionar_filho(novo)
        return novo

    def imprimir(self) -> None:
        """Mostra a árvore em modo hierárquico (cada nível com indentação)."""

        def _imprimir(no: Optional[No], nivel: int) -> None:
            if no is None:
                return
            print('  ' * nivel + f'- {no.valor}')
            for f in no.filhos:
                _imprimir(f, nivel + 1)

        if self.vazia():
            print('(árvore vazia)')
            return
        _imprimir(self.raiz, 0)


def adicionar_ramo(arvore: Arvore) -> None:
    """Modo interativo para inserir nós via terminal.

    Uso: chama-se passando um objeto Arvore. Digite ENTER em valor vazio para
    encerrar. Se a árvore já tiver raiz, você pode informar o valor do pai.
    """
    while True:
        print('\nÁrvore atual:')
        arvore.imprimir()
        print('\nEntre com os dados ou ENTER para encerrar.')
        valor = input('Digite o valor/dado a ser inserido: ').strip()
        if not valor:
            break

        pai = None
        if not arvore.vazia():
            pai = input('Digite o valor do pai (ENTER para anexar à raiz): ').strip() or None

        try:
            arvore.adicionar_no(valor, pai)
        except ValueError as e:
            print('Erro:', e)


def demo() -> None:
    """Demonstração não interativa usada para validar rapidamente."""
    a = Arvore()
    a.adicionar_no('raiz')
    a.adicionar_no('filho1', 'raiz')
    a.adicionar_no('filho2', 'raiz')
    a.adicionar_no('filho1.1', 'filho1')
    a.adicionar_no('filho2.1', 'filho2')
    print('Árvore de demonstração:')
    a.imprimir()


if __name__ == '__main__':
    # Se DEMO=1 no ambiente, roda demo não interativa (útil para validação)
    if os.environ.get('DEMO') == '1':
        demo()
    else:
        arv = Arvore()
        print('Modo interativo: insira nós. Deixe em branco para sair.')
        adicionar_ramo(arv)
