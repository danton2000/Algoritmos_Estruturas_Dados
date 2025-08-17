import random
def gerador_de_lista_inteiros(tamanho_lista:int = 10, intervalo_maximo:int = 10) -> list:
# lista_de_inteiros = [random.randint(0, intervalo_maximo) for _ in range(tamanho_lista)]
    lista_de_inteiros = random.sample(range(0, intervalo_maximo), tamanho_lista)
    return lista_de_inteiros