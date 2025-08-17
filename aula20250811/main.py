print("""
Você deverá implementar um algoritmo que execute a mesma função do método index() já implementado na estrutura de dados lista do python.
minha_lista.index(elemento)

Crie uma função que receba como parâmetros uma lista e a informação a ser encontrada
nesta lista.
Esta função deverá retornar a posição da lista onde a informação foi encontrada,
ou retornar None, caso a informação não seja encontrada.
""")

import random
import gerarListas as li

def busca_sequencial(lista_entrada:list, elemento_loc:int) -> int:
    for indice, elemento in enumerate(lista_entrada):
        if elemento == elemento_loc:
            return indice
    return None

print("Gerando lista...")
lista_nao_ordenada = li.gerador_de_lista_inteiros(1000000,10000000000)

elemento_proc = random.choice(lista_nao_ordenada)

print("Procurar elemento:", elemento_proc)

print(f"Elemento localizado na posição:{busca_sequencial
      (lista_nao_ordenada, elemento_proc)}")
