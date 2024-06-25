class Torre:

    #atributo de classe
    id_torre = 1

    lista_torres = []

    def __init__(self):
        
        self.id_torre = None
        self.nome_torre = None
        self.endereco_torre = None

    def cadastrarTorre(self, nome_torre, endereco_torre):

        self.id_torre = Torre.id_torre

        self.nome_torre = nome_torre

        self.endereco_torre = endereco_torre

        Torre.id_torre += 1

        Torre.lista_torres.append(self)

        print("Torre cadastrada.")

    def listarTorres(self):

        contador = 0

        # Interando pela lista_torres que é uma lista de objetos Torre
        for torre in Torre.lista_torres:

            print(f"{contador} - Id Torre: {torre.id_torre} - Nome da Torre: {torre.nome_torre} - Endereço: {torre.endereco_torre}")

            contador += 1
