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
    print("7 - Liberar Vagas")
    print("8 - Mostrar Vagas Disponiveis")
    
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
        numero_vaga = int(input("Digite o numero da Vaga: "))

        apartamento.cadastrarApartamento(
            numero_apartamento = 103,
            vaga_garagem = numero_vaga,
            torre = torre_selecionada
        )

        # Verificar aqui se vai para a lista ou para a fila ?

    elif opcao == "4":
        apartamento.listarApartamentos()

    elif opcao == "5":
        apartamento.listarVagasApartamento()

    elif opcao == "6":
        apartamento.listarFilaEspera()

    elif opcao == "7":
        numero_vaga = int(input("Digite o numero da vaga: "))

        apartamento.liberarVaga(numero_vaga)

    elif opcao == "8":
        Apartamento.listarVagasDisponiveis()
        
    else:
        print("Opção invalida!")