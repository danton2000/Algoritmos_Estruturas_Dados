from Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):

        texto = f"Codigo: {self.codigo}, Nome: {self.nome}, Matricula: {self.matricula}, Semestre: {self.semestre}"

        return texto