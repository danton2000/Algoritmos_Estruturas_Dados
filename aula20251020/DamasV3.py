"""
Damas - versão didática com comentários práticos em português.

Este arquivo contém:
- classe Jogada: representa um movimento/captura
- classe ArvoreDeJogadas: monta uma árvore simples de sequências de jogadas
- classe TabuleiroDamas: representa o tabuleiro e aplica jogadas

Os comentários inseridos são simples e mostram o que cada parte faz e por
que (sem alterar a lógica original).
"""


class Jogada:
    """Representa uma jogada (origem -> destino) e seu tipo.

    Atributos:
    - origem: (linha, coluna)
    - destino: (linha, coluna)
    - tipo: 'movimento' ou 'captura'
    - filho_esquerdo / filho_direito: links para construir sequência na árvore
    """

    def __init__(self, origem: tuple, destino: tuple, tipo: str):
        # salva coordenadas de origem e destino
        self.origem = origem
        self.destino = destino
        # tipo de jogada (movimento simples ou captura de peça adversária)
        self.tipo = tipo  # 'movimento' ou 'captura'
        # ponteiros para montar árvore de jogadas (convenção do código)
        self.filho_esquerdo = None
        self.filho_direito = None


class ArvoreDeJogadas:
    # Inicialização / Construção
    def __init__(self):
        # Raiz da arvore(inicio/base)
        self.raiz = None

    # Metodos
    def inserir_jogada(self, nova_jogada: Jogada):
        if self.raiz is None:
            self.raiz = nova_jogada
        else:
            self._inserir(self.raiz, nova_jogada)

    def _inserir(self, atual: Jogada, nova_jogada: Jogada):
        # verifica se a nova jogada continua a sequência (destino -> origem)
        if atual.destino == nova_jogada.origem:
            # se for movimento, tenta encaixar no filho_esquerdo
            if nova_jogada.tipo == 'movimento':
                if atual.filho_esquerdo is None:
                    atual.filho_esquerdo = nova_jogada
                else:
                    # já existe um filho à esquerda: tenta inserir recursivamente
                    self._inserir(atual.filho_esquerdo, nova_jogada)
            # se for captura, usa o filho_direito
            elif nova_jogada.tipo == 'captura':
                if atual.filho_direito is None:
                    atual.filho_direito = nova_jogada
                else:
                    self._inserir(atual.filho_direito, nova_jogada)
        else:
            # se não se encaixa neste nó, tenta nas subárvores esquerda e direita
            if atual.filho_esquerdo:
                self._inserir(atual.filho_esquerdo, nova_jogada)
            if atual.filho_direito:
                self._inserir(atual.filho_direito, nova_jogada)

    def exibir_in_ordem(self):
        def _in_ordem(no):
            if no:
                _in_ordem(no.filho_esquerdo)
                # imprime tipo (MAIÚSCULO) e a movimentação
                print(f"{no.tipo.upper()}: {no.origem} → {no.destino}")
                _in_ordem(no.filho_direito)
        _in_ordem(self.raiz)

    def buscar_por_destino(self, destino: tuple) -> Jogada:
        def _buscar(no):
            if no is None:
                return None
            if no.destino == destino:
                return no
            return _buscar(no.filho_esquerdo) or _buscar(no.filho_direito)
        return _buscar(self.raiz)

    def profundidade_maxima(self) -> int:
        def _profundidade(no):
            if no is None:
                return 0
            return 1 + max(_profundidade(no.filho_esquerdo), _profundidade(no.filho_direito))
        return _profundidade(self.raiz)

    def caminho_agressivo(self):
        caminho = []
        atual = self.raiz
        while atual:
            # monta lista assumindo que o caminho agressivo é seguir à direita
            caminho.append(f"{atual.tipo.upper()}: {atual.origem} → {atual.destino}")
            atual = atual.filho_direito
        for passo in caminho:
            print(passo)


class TabuleiroDamas:
    # Inicialização / Construção
    def __init__(self):
        #criando o tabuleiro vazio com as linhas e colunas
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]

        # Preto inicia o turno
        self.turno = 'P'

        # Inicializando - Preenchendo o tabuleiro
        self.inicializar()

    def inicializar(self):
        # Pupulando os espaços com as peças(P e B)
        for linha in range(3):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self.tabuleiro[linha][coluna] = 'P'
        for linha in range(5, 8):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self.tabuleiro[linha][coluna] = 'B'

    def exibir(self):
        print("   " + " ".join(str(i) for i in range(8)))
        print("  +" + "---+" * 8)
        for i, linha in enumerate(self.tabuleiro):
            linha_str = f" {i}|"
            for casa in linha:
                # mostra a peça: P para preta, B para branca, ou espaço vazio
                if casa == 'P':
                    linha_str += " P |"
                elif casa == 'B':
                    linha_str += " B |"
                else:
                    linha_str += "   |"
            print(linha_str)
            print("  +" + "---+" * 8)

    def aplicar_jogadas_da_arvore(self, arvore):
        def aplicar_jogada(jogada):
            origem_linha, origem_coluna = jogada.origem
            destino_linha, destino_coluna = jogada.destino
            peca = self.tabuleiro[origem_linha][origem_coluna]

            if peca is None:
                # não existe peça na casa de origem
                print(f" Jogada inválida: não há peça em {jogada.origem}")
                return

            if peca != self.turno:
                # tentando mover peça do outro jogador
                print(f" Jogada inválida: é o turno de {self.turno}, mas tentou mover {peca}")
                return

            # Captura simples
            if jogada.tipo == 'captura':
                meio_linha = (origem_linha + destino_linha) // 2
                meio_coluna = (origem_coluna + destino_coluna) // 2
                adversaria = self.tabuleiro[meio_linha][meio_coluna]

                if adversaria is None or adversaria == peca:
                    # sem peça adversária no meio -> captura inválida
                    print(f" Captura inválida: sem adversário em {(meio_linha, meio_coluna)}")
                    return

                self.tabuleiro[meio_linha][meio_coluna] = None

            self.tabuleiro[origem_linha][origem_coluna] = None
            self.tabuleiro[destino_linha][destino_coluna] = peca
            print(f"Jogada aplicada: {jogada.tipo.upper()} de {jogada.origem} para {jogada.destino}")

            # Alterna o turno
            self.turno = 'B' if self.turno == 'P' else 'P'

        def percorrer_e_aplicar(no):
            if no is None:
                return
            aplicar_jogada(no)
            self.exibir()
            percorrer_e_aplicar(no.filho_esquerdo)
            percorrer_e_aplicar(no.filho_direito)

        print("\nAplicando jogadas da árvore:")
        percorrer_e_aplicar(arvore.raiz)

    def aplicar_jogada_individual(self, jogada):
        origem_linha, origem_coluna = jogada.origem
        destino_linha, destino_coluna = jogada.destino
        peca = self.tabuleiro[origem_linha][origem_coluna]

        if peca is None:
            # validação: origem sem peça
            print(f"Jogada inválida: não há peça em {jogada.origem}")
            return

        if peca != self.turno:
            print(f"Jogada inválida: é o turno de {self.turno}, mas tentou mover {peca}")
            return

        if jogada.tipo == 'captura':
            meio_linha = (origem_linha + destino_linha) // 2
            meio_coluna = (origem_coluna + destino_coluna) // 2
            adversaria = self.tabuleiro[meio_linha][meio_coluna]

            if adversaria is None or adversaria == peca:
                # captura inválida sem peça adversária
                print(f"Captura inválida: sem adversário em {(meio_linha, meio_coluna)}")
                return

            self.tabuleiro[meio_linha][meio_coluna] = None

        self.tabuleiro[origem_linha][origem_coluna] = None
        self.tabuleiro[destino_linha][destino_coluna] = peca
        print(f"Jogada aplicada: {jogada.tipo.upper()} de {jogada.origem} para {jogada.destino}")
        self.turno = 'B' if self.turno == 'P' else 'P'

    def realizar_jogadas(self, arvore):
        # loop para a realização das jogadas da partida de deman
        # Solicitando:
        # origem da linha da jogada e origem da coluna da joagada(onde está a peça)
        # destino da linha da jogada e destino da coluna da jogada(onde a peça vai)
        # qual movimento será feito, movimento ou captura(capturar peça do adversário)
        while True:
            print(f"\n🎯 Turno atual: jogador {self.turno}")
            print("""Como Digitar Exemplo: ol,oc-dl,dc-mo   ou ol,oc-dl-dc-ca 
                ol - origemLinha      oc - origemColuna
                dl - destinoLinha     dc - destinoColuna
                mo - movimento   ou   ca - captura 
                """)
            digitacao = input("Entre a jogada no formato:  ")
            origem, destino, acao = digitacao.split("-")
            olinha, ocoluna = origem.split(",")
            dlinha, dcoluna = destino.split(",")
            if acao == "mo":
                acao = "movimento"
            else:
                acao = "captura"
            jogada = Jogada((int(olinha), int(ocoluna)), (int(dlinha), int(dcoluna)), acao)
            arvore.inserir_jogada(jogada)
            self.aplicar_jogada_individual(jogada)
            self.exibir()


#Instanciando class ArvoreDeJogadas
arvore = ArvoreDeJogadas()

#Instanciando class TabuleiroDamas
tabuleiro = TabuleiroDamas()

# Exibindo de forma formata da o tabuleiro em seu inicio
tabuleiro.exibir()

# Realizar jogadas, passadas pelo usuário
tabuleiro.realizar_jogadas(arvore)




"""
    0   1   2   3   4   5   6   7
  +---+---+---+---+---+---+---+---+
0 |   | P |   | P |   | P |   | P |
  +---+---+---+---+---+---+---+---+
1 | P |   | P |   | P |   | P |   |
  +---+---+---+---+---+---+---+---+
2 |   | P |   | P |   | P |   | P |
  +---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
4 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
5 | B |   | B |   | B |   | B |   |
  +---+---+---+---+---+---+---+---+
6 |   | B |   | B |   | B |   | B |
  +---+---+---+---+---+---+---+---+
7 | B |   | B |   | B |   | B |   |
  +---+---+---+---+---+---+---+---+
"""

# Entender esse código
# Entender o outro codigo(blackboard) - o mais simples