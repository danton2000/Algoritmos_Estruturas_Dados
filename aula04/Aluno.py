class Aluno:

    def __init__(self, codigo, nome, matricula ):

        self.codigo = codigo

        self.nome = nome

        self.matricula = matricula

    def imprimir(self):

        texto = f"Codigo: {self.codigo}, Nome: {self.nome}, Matricula: {self.matricula}"

        return texto