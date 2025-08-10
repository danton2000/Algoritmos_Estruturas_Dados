"""
Validador de expressões matemáticas usando pilha.

Delimitadores válidos: (), [], {}
Cada delimitador de abertura deve ter um correspondente de fechamento correto e na ordem correta.

Exemplos de uso:
    expressao = "3 * [(5 - 2) + (4 - 2)]"
    print(validar_expressao(expressao))  # True

    expressao = "a{b(c]d}e"
    print(validar_expressao(expressao))  # False
"""

def validar_expressao(expressao):
    """
    Valida se os delimitadores em uma expressão matemática estão corretamente balanceados.

    Args:
        expressao (str): Expressão matemática a ser validada.

    Returns:
        bool: True se a expressão está correta, False caso contrário.
    """
    pilha = []
    # Mapeamento de fechamento para abertura
    pares = {')': '(', ']': '[', '}': '{'}
    aberturas = set(pares.values())

    for caractere in expressao:
        if caractere in aberturas:
            pilha.append(caractere)
        elif caractere in pares:
            if not pilha or pilha[-1] != pares[caractere]:
                # Pilha vazia ou topo não corresponde ao fechamento
                return False
            pilha.pop()
    # Se pilha está vazia, todos os delimitadores foram fechados corretamente
    return len(pilha) == 0

# Exemplos de teste
if __name__ == "__main__":
    expressoes = [
        "3 * [(5 - 2) + (4 - 2)]",
        "a{[b(c*d)+(b+c)]*[a-b(b/c)]}*5",
        "a[d]",
        "a{b[c]d}e",
        "a{b(c]d}e",
        "a[b{c}d]e}",
        "a{b(c)"
    ]
    for expr in expressoes:
        print(f"{expr}: {validar_expressao(expr)}")