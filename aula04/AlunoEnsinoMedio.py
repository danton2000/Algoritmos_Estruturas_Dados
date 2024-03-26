from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):

        texto = f"Codigo: {self.codigo}, Nome: {self.nome}, Matricula: {self.matricula}, Ano: {self.ano}"

        return texto