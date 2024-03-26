from AlunoEnsinoMedio import AlunoEnsinoMedio

from AlunoGraduacao import AlunoGraduacao

aluno1 = AlunoEnsinoMedio(
    codigo = 123, 
    nome = "Danton", 
    matricula = 181810032, 
    ano = 2024
)

print(aluno1.imprimir())

aluno2 = AlunoGraduacao(
    codigo = 123, 
    nome = "Danton", 
    matricula = 181810032, 
    semestre = 3
)

print(aluno2.imprimir())