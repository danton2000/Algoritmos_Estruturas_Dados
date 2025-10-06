# Estrutura de Nó (cada nó guarda um valor e o ponteiro para o próximo)
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None  # ponteiro para o próximo nó (None se for o último)


# ListaEncadeada mínima: suporte para inserir no final e conversão para lista Python
class ListaEncadeada:
    def __init__(self):
        self.inicio = None  # referência para o primeiro nó da lista

    def inserir(self, valor):
        """Insere um valor no final da lista.

        Por que: manter uma versão encadeada dos dados facilita exercícios de
        estrutura, mesmo que o algoritmo de ordenação use a conversão para uma
        lista Python para simplificar a lógica de Radix/Counting.
        """
        novo = No(valor)
        if self.inicio is None:
            # lista vazia -> o novo nó vira o início
            self.inicio = novo
        else:
            # percorre até o fim e anexa o novo nó
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def to_list(self):
        """Converte a lista encadeada em uma lista Python.

        Por que: o Radix/Counting Sort é mais direto de implementar em listas
        indexáveis; essa conversão é feita para clareza didática.
        """
        resultado = []
        atual = self.inicio
        while atual:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado

    def from_list(self, valores):
        """Preenche a lista encadeada a partir de uma lista Python.

        Simples utilitário para construir exemplos a partir de um array.
        """
        for v in valores:
            self.inserir(v)


# -----------------------------
# Funções do Radix Sort
# -----------------------------
def counting_sort_lista(lista, exp):
    """Counting Sort por dígito (estável), aplicado sobre a lista encadeada.

    Parâmetros:
    - lista: `ListaEncadeada` com inteiros
    - exp: potência de 10 que indica o dígito atual (1=unidade, 10=dezena, ...)

    Passos:
    1) Convertemos para lista Python para aproveitar indexação simples.
    2) Contamos ocorrências do dígito atual (0-9).
    3) Computamos a soma acumulada para posicionamento estável.
    4) Preenchemos a saída andando de trás para frente (estabilidade).
    5) Reconstruímos uma `ListaEncadeada` com a ordem estável resultante.
    """
    # converte para lista normal para aplicar counting sort
    arr = lista.to_list()
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # buckets para dígitos 0..9

    # Conta quantas vezes aparece cada dígito na posição indicada por exp
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Transforma count em posições acumuladas (prefix sum)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Constroi a saída de forma estável: percorre de trás para frente
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Reconstrói a lista encadeada com os valores ordenados por este dígito
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

    # Percorre cada dígito, do menos significativo ao mais (LSD Radix)
    while max_num // exp > 0:
        # Aplica counting sort baseado no dígito atual (exp)
        resultado = counting_sort_lista(resultado, exp)
        exp *= 10  # avança para o próximo dígito (unidade -> dezena -> centena ...)

    # Retorna a lista encadeada ordenada
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

    # Executa o Radix Sort e imprime a lista ordenada com a etiqueta do concurso
    ordenada = radix_sort_lista(lista)
    print(f"{ordenada.to_list()} - {concurso}")