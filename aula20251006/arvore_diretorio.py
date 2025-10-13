import os

class No:
    def __init__(self, nome, tipo):
        """Cria um nó representando um arquivo ou diretório."""
        self.nome = nome          # nome do arquivo ou pasta
        self.tipo = tipo          # 'pasta' ou 'arquivo'
        self.filhos = []          # lista de nós filhos

    def adicionar_filho(self, filho):
        """Adiciona um nó filho — somente se este nó for uma pasta."""
        if self.tipo == "pasta":
            self.filhos.append(filho)

    def imprimir(self, nivel=0):
        """Imprime o conteúdo da árvore com indentação."""
        prefixo = "  " * nivel + ("📁 " if self.tipo == "pasta" else "📄 ")
        print(prefixo + self.nome)
        for filho in self.filhos:
            filho.imprimir(nivel + 1)


class Arvore:
    def __init__(self, raiz):
        """Inicializa a árvore com o nó raiz."""
        self.raiz = raiz

    @staticmethod
    def ler_diretorio(caminho):
        """Lê o diretório e constrói a árvore recursivamente."""
        nome = os.path.basename(caminho) or caminho
        no_raiz = No(nome, "pasta")

        try:
            for item in os.listdir(caminho):
                caminho_completo = os.path.join(caminho, item)
                if os.path.isdir(caminho_completo):
                    # cria subárvore para pastas
                    filho = Arvore.ler_diretorio(caminho_completo)
                    no_raiz.adicionar_filho(filho.raiz)
                else:
                    # adiciona arquivos diretamente
                    no_raiz.adicionar_filho(No(item, "arquivo"))
        except PermissionError:
            # ignora pastas sem permissão
            pass

        return Arvore(no_raiz)

    def imprimir(self):
        """Imprime toda a árvore."""
        self.raiz.imprimir()


if __name__ == "__main__":
    # Obtém o diretório atual
    diretorio_os = os.getcwd()
    print(f"Diretório atual: {diretorio_os}\n")

    # Lê o diretório e monta a árvore
    arvore = Arvore.ler_diretorio(diretorio_os)

    # Imprime a estrutura hierárquica
    print("Estrutura de diretórios:\n")
    arvore.imprimir()
