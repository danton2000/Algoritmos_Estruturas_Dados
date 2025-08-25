class NoAluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        self.proximo = None


class TurmaEncadeada:
    def __init__(self):
        self.inicio = None
        self.final = None

    def inserir_aluno(self, nome, matricula, nota):
        """
        Insere um novo aluno ao final da lista encadeada.

        Esta implementação mantém referências para o início e o final da
        lista para permitir inserções O(1) no final.

        Args:
            nome (str): nome do aluno.
            matricula (int): matrícula do aluno.
            nota (float): nota do aluno.
        """
        novo = NoAluno(nome, matricula, nota)
        # Se a lista estiver vazia, novo nó é início e final
        if not self.inicio:
            self.inicio = novo
            self.final = novo
        else:
            # Anexa ao final atual e atualiza a referência de final
            self.final.proximo = novo
            self.final = novo
        print(f"Aluno {nome} inserido com sucesso!\n")

    def busca_sequencial_nome(self, nome_busca):
        atual = self.inicio
        encontrados = []
        comparacoes = 0

        while atual:
            comparacoes += 1
            if atual.nome.lower() == nome_busca.lower():
                encontrados.append(atual)
            atual = atual.proximo

        return encontrados, comparacoes

    def busca_sequencial_matricula(self, matricula_busca):
        """
        Procura um aluno pela matrícula usando busca sequencial na lista encadeada.

        Retorna uma tupla (NoAluno | None, comparacoes) onde comparacoes é o
        número de nós verificados até encontrar o aluno (ou até terminar a lista).
        """
        atual = self.inicio
        comparacoes = 0

        while atual:
            comparacoes += 1
            if atual.matricula == matricula_busca:
                return atual, comparacoes
            atual = atual.proximo

        return None, comparacoes

    def ordenar_por_nota(self):
        """
        Ordena os alunos por nota (maior para menor).

        Estratégia simples:
        - Coletar referências de todos os nós em uma lista Python.
        - Ordenar essa lista por atributo `nota` (reverse=True).
        - Reconstruir a lista encadeada ligando os nós na nova ordem
          e atualizando `inicio` e `final`.

        Complexidade: O(n log n) pelo sort.
        """
        # Coletar nós
        atual = self.inicio
        nos = []
        while atual:
            nos.append(atual)
            atual = atual.proximo

        # Se lista vazia ou com 1 elemento, nada a fazer
        if len(nos) <= 1:
            return

        # Ordenar por nota (maior para menor)
        nos.sort(key=lambda no: no.nota, reverse=True)

        # Reconstruir ligações
        self.inicio = nos[0]
        atual = self.inicio
        for no in nos[1:]:
            atual.proximo = no
            atual = no
        # finalizar a lista
        atual.proximo = None
        self.final = atual


def status_aluno(nota):
    return "Aprovado" if nota >= 6 else "Reprovado"


def exibir_resultado(aluno, comparacoes):
    if aluno:
        print(f"\nAluno encontrado após {comparacoes} comparações:")
        print(f"Nome: {aluno.nome}")
        print(f"Matrícula: {aluno.matricula}")
        print(f"Nota: {aluno.nota}")
        print(f"Status: {status_aluno(aluno.nota)}")
    else:
        print(f"\nAluno não encontrado após {comparacoes} comparações.")


def exibir_resultado_nome(encontrados, comparacoes):
    if encontrados:
        print(f"\n{len(encontrados)} aluno(s) encontrado(s) após {comparacoes} comparações:")
        for aluno in encontrados:
            print(f"Nome: {aluno.nome}")
            print(f"Matrícula: {aluno.matricula}")
            print(f"Nota: {aluno.nota}")
            print(f"Status: {status_aluno(aluno.nota)}")
            print("---")
    else:
        print(f"\nNenhum aluno encontrado após {comparacoes} comparações.")


def main():
    turma = TurmaEncadeada()

    # Alunos iniciais
    turma.inserir_aluno("Ana", 1001, 8.5)
    turma.inserir_aluno("Bruna", 1002, 5.0)
    turma.inserir_aluno("Carla", 1003, 6.7)
    turma.inserir_aluno("Daniel", 1004, 9.2)
    turma.inserir_aluno("Eduarda", 1005, 4.8)

    while True:
        print("\n--- MENU ---")
        print("1. Buscar aluno por matrícula")
        print("2. Inserir novo aluno")
        print("3. Ordenar alunos por nota")
        print("4. Buscar aluno por nome")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            matricula_busca = int(input("Digite a matrícula: "))
            aluno, comparacoes = turma.busca_sequencial_matricula(matricula_busca)
            exibir_resultado(aluno, comparacoes)

        elif opcao == "2":
            nome = input("Nome do aluno: ")
            matricula = int(input("Matrícula: "))
            nota = float(input("Nota: "))
            turma.inserir_aluno(nome, matricula, nota)

        elif opcao == "3":
            turma.ordenar_por_nota()
            print("\nAlunos ordenados por nota (maior para menor):")
            atual = turma.inicio
            while atual:
                print(f"{atual.nome} - Nota: {atual.nota}")
                atual = atual.proximo

        elif opcao == "4":
            nome_busca = input("Digite o nome do aluno: ")
            encontrados, comparacoes = turma.busca_sequencial_nome(nome_busca)
            exibir_resultado_nome(encontrados, comparacoes)

        elif opcao == "5":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
