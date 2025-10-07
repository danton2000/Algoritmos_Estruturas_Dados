import os

class No:
    def __init__(self, nome, tipo):

        self.nome = nome

        self.tipo = tipo

        self.filhos = []

    def adicionar_filho(filho):
        # adicionar um no filho
        # apenas se for pasta
        pass

    def imprimir(nivel=0):
        # imprime o conteúdo com indentação.
        pass

class Arvore:

    def __init__(self, raiz):

        self.raiz = raiz

    def ler_diretorio(caminho):
        # constrói a árvore recursivamente a partir do caminho.
        pass


    def imprimir():
        # imprime a árvore completa a partir da raiz.
        pass

if __name__ == "__main__":

    # Usando o módulo os
    diretorio_os = os.getcwd()
    print(f"Diretório atual (os): {diretorio_os}")

