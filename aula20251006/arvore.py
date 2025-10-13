class No:
    def __init__(self, valor):
        """Cria um nó com um valor e uma lista de filhos."""
        self.valor = valor
        self.filhos = []

    def adicionar_filhos(self, filho):
        """Adiciona um nó filho a este nó."""
        self.filhos.append(filho)


class Arvore:
    def __init__(self, raiz=None):
        """Inicializa a árvore com uma raiz opcional."""
        self.raiz = raiz

    def vazia(self):
        """Retorna True se a árvore estiver vazia."""
        return self.raiz is None

    def buscar_no(self, valor):
        """Busca um nó pelo valor dentro da árvore (busca recursiva)."""
        if self.raiz is None:
            return None
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no, valor):
        """Função auxiliar para busca recursiva."""
        if no.valor == valor:
            return no
        for filho in no.filhos:
            resultado = self._buscar_recursivo(filho, valor)
            if resultado:
                return resultado
        return None

    def adicionar_no(self, valor, pai=None):
        """Adiciona um novo nó à árvore."""
        novo_no = No(valor)

        # Caso seja o primeiro nó (raiz)
        if self.raiz is None:
            self.raiz = novo_no
            print(f"Raiz '{valor}' criada com sucesso!")
            return

        # Caso haja um pai especificado
        no_pai = self.buscar_no(pai)
        if no_pai:
            no_pai.adicionar_filhos(novo_no)
            print(f"Nó '{valor}' adicionado como filho de '{pai}'.")
        else:
            print(f"Pai '{pai}' não encontrado! Nó '{valor}' não adicionado.")

    def imprimir(self, no=None, nivel=0):
        """Imprime a árvore de forma hierárquica."""
        if self.raiz is None:
            print("(Árvore vazia)")
            return

        if no is None:
            no = self.raiz

        print("  " * nivel + f"- {no.valor}")
        for filho in no.filhos:
            self.imprimir(filho, nivel + 1)


def adicionar_ramo(arvore):
    """Função interativa para adicionar nós na árvore."""
    while True:
        arvore.imprimir()
        print("\nEntre com os dados ou pressione ENTER para encerrar.")
        valor = input("Digite o valor/dado a ser inserido: ")

        if not valor:
            break

        pai = None
        if not arvore.vazia():
            pai = input("Digite o pai para esse dado (ou ENTER se for raiz): ")
            if not pai:
                pai = None

        arvore.adicionar_no(valor, pai)


if __name__ == "__main__":
    # Criando uma árvore
    arvore = Arvore()

    # Adicionando nós interativamente
    adicionar_ramo(arvore)

    print("\nÁrvore final:")
    arvore.imprimir()
