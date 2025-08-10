from pilha import Pilha
from torre_hanoi import TorreHanoi

def exemplo_torre_hanoi_interativo():
    print("\n" + "="*50)
    print("EXEMPLO 1: Torre de Hanoi - Modo Interativo")
    print("="*50)
    
    print("Vamos criar uma Torre de Hanoi para você resolver!")
    
    while True:
        try:
            num_discos = int(input("Quantos discos você quer? (recomendado: 3-4): "))
            if 1 <= num_discos <= 8:
                break
            else:
                print("Por favor, escolha entre 1 e 8 discos.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    torre = TorreHanoi(num_discos)
    torre.resolver_interativo()

def demonstrar_conceitos_pilha():
    print("\n" + "="*50)
    print("EXEMPLO 2: Conceitos Fundamentais de Pilha")
    print("="*50)
    
    print("""
📚 CONCEITOS FUNDAMENTAIS:

1. LIFO (Last In, First Out)
   - O último elemento adicionado é o primeiro a ser removido
   

2. OPERAÇÕES PRINCIPAIS:
   - Push: Adicionar elemento no topo
   - Pop: Remover elemento do topo
   - Peek/Top: Ver o elemento do topo sem remover
   - IsEmpty: Verificar se está vazia

3. APLICAÇÕES REAIS:
   - Ctrl+Z (desfazer) nos editores
   - Navegação de páginas web (botão voltar)
   - Chamadas de funções recursivas
   - Calculadoras (notação pós-fixa)
 

4. POR QUE TORRE DE HANOI?
   - Cada haste é uma pilha
   - Só podemos mover o disco do topo (LIFO)
   - Demonstra recursão e estrutura de dados juntas
   - Problema clássico da Ciência da Computação
    """)

def menu_principal():
    while True:
        print("\n" + "="*50)
        print("EXEMPLOS DE PILHAS E TORRE DE HANOI")
        print("="*50)
        print("1. Torre de Hanoi - modo interativo")
        print("2. Conceitos importantes")
        print("0. Sair")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                print("\n👋 Até logo! Continue estudando estruturas de dados!")
                break
            elif opcao == 1:
                exemplo_torre_hanoi_interativo()
            elif opcao == 2:
                demonstrar_conceitos_pilha()
            else:
                print("❌ Opção inválida! Tente novamente.")
                
        except ValueError:
            print("❌ Por favor, digite um número válido.")
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido. Até logo!")
            break

if __name__ == "__main__":
    print("📖 Estrutura de Dados II - SENAC")
    menu_principal() 