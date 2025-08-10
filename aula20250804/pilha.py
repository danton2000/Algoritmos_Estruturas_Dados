class Pilha:   
    def __init__(self):
        self.itens = []
    
    def push(self, item):
        self.itens.append(item)
        print(f"Adicionado {item} à pilha")
    
    def pop(self):
        if self.esta_vazia():
            raise IndexError("Pop de pilha vazia")
        
        item = self.itens.pop()
        print(f"Removido {item} da pilha")
        return item
    
    def peek(self):
        if self.esta_vazia():
            raise IndexError("Peek de pilha vazia")
        return self.itens[-1]
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def tamanho(self):
        return len(self.itens)
    
    def exibir(self):
        if self.esta_vazia():
            print("Pilha vazia: []")
        else:
            print("Pilha (base -> topo):", self.itens)
    
    def __str__(self):
        return f"Pilha: {self.itens}" 