from Torre import Torre

from Apartamento import Apartamento

while True:
    print("--Menu--")
    print("1 - Adicionar uma Torre")
    print("2 - Listar Torres")
    print("3 - Adicionar um Apartamento")
    print("4 - Listar Apartamentos")
    print("5 - Listar Vagas")
    print("6 - Listar Fila")
    print("7 - Mostrar Vagas Disponiveis")
    
    opcao = input("Digite uma opção: ")

    # Instanciando a classe Torre
    torre = Torre()

    apartamento = Apartamento()

    if opcao == "1":

        torre.cadastrarTorre(
            nome_torre = 'Torre 1',
            endereco_torre = 'Fica logo ali'
        )

    elif opcao == "2":
        
        torre.listarTorres()
       
    elif opcao == "3":

        torre.listarTorres()

        # Pegando pela o indice a torre
        index_torre = int(input("Escolha uma Torre para vincular ao Apartamento: "))

        # Pegando a torre selecionada pelo indice na lista de torres(lista de objetos de torres)
        torre_selecionada = Torre.lista_torres[index_torre]

        #Numero da vaga
        vaga_garagem = int(input("Digite o numero da Vaga:"))

        apartamento.cadastrarApartamento(
            numero_apartamento = 103,
            vaga_garagem = vaga_garagem,
            torre = torre_selecionada
        )

        # Verificar aqui se vai para a lista ou para a fila ?

    elif opcao == "4":
        apartamento.listarApartamentos()

    elif opcao == "5":
        apartamento.listarVagas()

    elif opcao == "6":
        apartamento.listarFila()

    elif opcao == "7":
        Apartamento.mostrarVagasCondominio()
        
    else:
        print("Opção invalida!")