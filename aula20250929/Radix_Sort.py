#python
# -----------------------------
# Estrutura de Nó e Lista Encadeada
# -----------------------------
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        """Insere um valor no final da lista"""
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def to_list(self):
        """Converte lista encadeada em lista normal (para exibição)"""
        resultado = []
        atual = self.inicio
        while atual:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado

    def from_list(self, valores):
        """Constrói a lista encadeada a partir de uma lista normal"""
        for v in valores:
            self.inserir(v)


# -----------------------------
# Funções do Radix Sort
# -----------------------------
def counting_sort_lista(lista, exp):
    """
    Counting Sort adaptado para lista encadeada.
    """
    arr = lista.to_list()  # converte p/ lista normal (facilita o algoritmo)
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Conta ocorrências
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Soma acumulada
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Monta saída em ordem estável
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Reconstrói lista encadeada
    nova_lista = ListaEncadeada()
    nova_lista.from_list(output)
    return nova_lista


def radix_sort_lista(lista):
    """
    Radix Sort usando lista encadeada.
    """
    arr = lista.to_list()
    max_num = max(arr)
    exp = 1
    resultado = lista

    while max_num // exp > 0:
        resultado = counting_sort_lista(resultado, exp)
        exp *= 10

    return resultado


# -----------------------------
# Base de dados (exemplo fixo)
# -----------------------------
sorteios = {
    2683: [57, 47, 27, 23, 3, 1],
    2667: [4, 21, 8, 46, 1, 51],
    2700: [11, 28, 19, 1, 48, 20],
    2675: [45, 31, 42, 26, 34, 1],
    2668: [27, 30, 41, 46, 57, 1]
}

# -----------------------------
# Programa Principal
# -----------------------------
for concurso, dezenas in sorteios.items():
    lista = ListaEncadeada()
    lista.from_list(dezenas)

    ordenada = radix_sort_lista(lista)
    print(f"{ordenada.to_list()} - {concurso}")