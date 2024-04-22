from Desktop import Desktop
from Notebook import Notebook

desktop1 = Desktop()

desktop1.cadastrar("Dell", "Cinza-escuro", 3000.0, "450w")

print(desktop1.getInformacoes())

print("---")

notebook1 = Notebook()

notebook1.cadastrar("Acer", "branco-claro", 4000.0, "8 Horas")

print(notebook1.getInformacoes())