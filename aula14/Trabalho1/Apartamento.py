# Importando a classe ListaEncadeada
from ListaEncadeada import ListaEncadeada

# Importando a classe Fila
from Fila import Fila

class Apartamento:

    #atributo de classe
    id_apartamento = 1

    #Vagas do condominio
    vagas_condominio = 1

    lista_apartamentos = []

    lista_encadeada = ListaEncadeada()

    fila = Fila()

    def __init__(self):
        
        self.id_apartamento = None
        self.numero_apartamento = None
        self.vaga_garagem = None
        self.torre = None
        self.proximo = None

    def cadastrarApartamento(self, numero_apartamento, vaga_garagem, torre):

        self.id_apartamento = Apartamento.id_apartamento

        self.numero_apartamento = numero_apartamento

        # Utilizando um metodo de classe para verifica sem tem vaga disponivel
        self.vaga_garagem = vaga_garagem

        self.torre = torre

        self.verificaVagasGaragem()

        Apartamento.id_apartamento += 1

        Apartamento.lista_apartamentos.append(self)

        print("Apartamento cadastrado.")

    def listarApartamentos(self):

        # Interando pela lista_torres que é uma lista de objetos Torre
        for apto in Apartamento.lista_apartamentos:

            print(f"Id Apto: {apto.id_apartamento} - Numero do Apto: {apto.numero_apartamento} - Vaga Garagem: {apto.vaga_garagem} - Torre: {apto.torre.nome_torre}")

    def listarVagasApartamento(self):
        # Listando os numeros de vagas
        Apartamento.lista_encadeada.imprimir()

    def listarFilaEspera(self):
        # Listando a fila
        Apartamento.fila.imprimir()

    def verificaVagasGaragem(self):

        # 3 limite de vagas
        if  Apartamento.vagas_condominio == 0:

            Apartamento.fila.adicionarNaFila(self)

            # Adicionar na fila
        else:
            # Adicionar na lista encadeada
            Apartamento.lista_encadeada.adicionar(self)

            Apartamento.vagas_condominio -= 1

    def liberarVaga(self, numero_vaga):

        #Removendo da lista encadeada(apartamentos que estão utilizando as vagas)
        Apartamento.lista_encadeada.remover(numero_vaga)
        
        # Por que eu tive que fazer esse loop?(duvida)
        #Procurando o obj do apartamento pelo numero_vaga para a dicionar na fila de espera
        for apto in Apartamento.lista_apartamentos:
            
            if apto.vaga_garagem == numero_vaga:
                
                #Capturando o apto que saiu da fila para adicionar na lista encadeada
                apto_lista_encadeada = Apartamento.fila.remover()
                
                #print("apto que vai sair da fila e ir para a lista encadeada", apto_lista_encadeada.id_apartamento)
                
                Apartamento.lista_encadeada.adicionar(apto_lista_encadeada) 
                
                Apartamento.fila.adicionarNaFila(apto)
            
    def listarVagasDisponiveis():
        
        print(Apartamento.vagas_condominio)
            