class Turma:
    
    def __init__(self):
        
        self.matricula = None
        self.nome = None
        self.nota = None

        Turma.alunos = [
            {"matricula": 1001, "nome": "Ana", "nota": 8.5},
            {"matricula": 1002, "nome": "Bruno", "nota": 5.0},
            {"matricula": 1003, "nome": "Carla", "nota": 6.7},
            {"matricula": 1004, "nome": "Daniel", "nota": 9.2},
            {"matricula": 1005, "nome": "Eduarda", "nota": 4.8}
        ]
    
    def inserir_aluno():
        nome = input("Nome do aluno: ")
        matricula = int(input("Matrícula: "))
        nota = float(input("Nota: "))
        novo_aluno = {"matricula": matricula, "nome": nome, "nota": nota}
        Turma.alunos.append(novo_aluno)
        print(f"Aluno {nome} inserido com sucesso!\n")

    def busca_binaria(matricula):
        inicio = 0
        fim = len(Turma.alunos) - 1
        comparacoes = 0

        while inicio <= fim:
            meio = (inicio + fim) // 2
            comparacoes += 1
            if Turma.alunos[meio]["matricula"] == matricula:
                return Turma.alunos[meio], comparacoes
            elif Turma.alunos[meio]["matricula"] < matricula:
                inicio = meio + 1
            else:
                fim = meio - 1

        return None, comparacoes

    def exibir_resultado(aluno, comparacoes):
        if aluno:
            print(f"\nAluno encontrado após {comparacoes} comparações:")
            print(f"Nome: {aluno['nome']}")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nota: {aluno['nota']}")
            print(f"Status: {Turma.status_aluno(aluno['nota'])}")
        else:
            print(f"\nAluno não encontrado após {comparacoes} comparações.")

    def status_aluno(nota):
        return "Aprovado" if nota >= 6 else "Reprovado"

    def ordenar_por_nota():
        Turma.alunos.sort(key=lambda x: x["nota"], reverse=True)
        print("\nAlunos ordenados por nota (maior para menor):")
        for aluno in Turma.alunos:
            print(f"{aluno['nome']} - Nota: {aluno['nota']}")

    def buscar_por_nome(nome_busca):
        encontrados = []
        comparacoes = 0

        for aluno in Turma.alunos:
            comparacoes += 1
            if aluno["nome"].lower() == nome_busca.lower():
                encontrados.append(aluno)

        return encontrados, comparacoes

    def exibir_resultado_nome(encontrados, comparacoes):
        if encontrados:
            print(f"\n{len(encontrados)} aluno(s) encontrado(s) após {comparacoes} comparações:")
            for aluno in encontrados:
                print(f"Nome: {aluno['nome']}")
                print(f"Matrícula: {aluno['matricula']}")
                print(f"Nota: {aluno['nota']}")
                print(f"Status: {Turma.status_aluno(aluno['nota'])}")
                print("---")
        else:
            print(f"\nNenhum aluno encontrado após {comparacoes} comparações.")

def main():

    turma = Turma()

    while True:
        print("\n--- MENU ---")
        print("1. Buscar aluno por matrícula")
        print("2. Inserir novo aluno")
        print("3. Ordenar alunos por nota")
        print("4. Buscar aluno por nome")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            Turma.alunos.sort(key=lambda x: x["matricula"])
            matricula_busca = int(input("Digite a matrícula: "))
            aluno, comparacoes = Turma.busca_binaria(matricula_busca)

            Turma.exibir_resultado(aluno, comparacoes)

        elif opcao == "2":
            Turma.inserir_aluno()

        elif opcao == "3":
            Turma.ordenar_por_nota()

        elif opcao == "4":
            nome_busca = input("Digite o nome do aluno: ")
            encontrados, comparacoes = Turma.buscar_por_nome(nome_busca)
            Turma.exibir_resultado_nome(encontrados, comparacoes)

        elif opcao == "5":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()