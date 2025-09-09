import time

class Node:
    def __init__(self, numero):
        self.valor = numero
        self.next = None
        self.prev = None

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no #inicio da lista?
            self.tail = novo_no #fim da lista?
            print(f"inicio da lista: {self.head.valor}, fim da lista: {self.tail.valor}")
            
        else:
            self.tail.next = novo_no # colocando o como proximo valor, no fim da lista
            novo_no.prev = self.tail # colocando como anterior o valor do fim da lista
            print(f"proximo valor: {self.tail.next.valor}, valor anterior:{novo_no.prev.valor}")

            self.tail = novo_no # fim da lista vai ser o valor(nó) atual
            print(f"fim da lista: {self.tail.valor}")
            #exit()

    def imprime_lista(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(f"Valor: {atual.valor}")
                atual = atual.next

    def ordena_insertion(self):
        """
        Constrói a lista ordenada uma entrada por vez. 
        Ele pega cada elemento e o insere na posição correta em uma lista já ordenada.
        """

        # Verifica se tem elementos para a ordenação
        if self.head is None or self.head.next is None:

            return

        # Proximo elemento do inicio da lista 
        atual = self.head.next

        # Enquanto proximo elemento da lista não for Vazio, ele vai percorrendo
        while atual is not None:
            chave = atual.valor # 'proximo' valor
            mover = atual.prev # valor 'anterior' 

            print(f"proximo valor: {chave}", f"valor anterior: {mover.valor}")

            # Enquanto valor anteriror não for vazio e valor anteriror for maior que o proximo valor
            while mover is not None and mover.valor > chave:
                
                print(f"proximo valor antes: {mover.next.valor}")
                mover.next.valor = mover.valor
                print(f"proximo valor depois: {mover.next.valor}")

                print(f"valor anterior antes: {mover.valor}")
                mover = mover.prev
                # pq fica vazio?
                if mover is None:
                    print("Esta vazio essa merda")
                    exit()
                
            if mover is None:
                print(f"Inicio da lista antes: {self.head.valor}")

                self.head.valor = chave #trocando o inicio da lista pelo proximo valor

                print(f"Inicio da lista depois: {self.head.valor}")
            else:
                
                mover.next.valor = chave

            atual = atual.next

        print(f"Fim do while: {atual}") # Ele sai do while se o atual for None

lista_desordenada = [8, 3, 5]
lista = Lista()
for numero in lista_desordenada:
    lista.add_valor(numero)

print("Lista Desordenada:")
lista.imprime_lista()

print("Lista Ordenada com Insertion Sort:")
lista.ordena_insertion()
lista.imprime_lista()