class No:
    def __init__(self, valor):

        self.valor = valor

        self.filhos = []

    def adicionar_filhos(self, filho):

        self.filhos.append(filho)

class Arvore:

    def __init__(self, raiz = None):
        
        self.raiz = raiz

    def adicionar_no(self, valor, pai = None):

        pass
    
    # Função para adicionar nós na arvore
    def adicionar_ramo(arvore):

        while True:

            arvore.imprimir()

            print("Entre com os dados ou ENTER para encerrar.")

            valor = input("Digite o valor/dado a ser inserido.")

            if not valor:

                break

            pai = None

            if not arvore.vazia():

                pai = input("Digite o pai para esse dado.")

                if not pai:

                    break

                arvore.adicionar_no(valor, pai)


if __name__ == "__main__":

    # Criando uma arvore
    arvore = Arvore()

    # Adicionando nós na Arvore
    adicionar_ramo(arvore)