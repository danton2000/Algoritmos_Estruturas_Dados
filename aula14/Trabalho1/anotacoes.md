# Trabalho 01 - Condomínio

1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id, nome e endereço. A classe Apartamento deve conter os atributos, id, número do
apartamento, número da vaga de garagem e torre. - ok

2) Este condomínio, não possui vagas de garagem para todos os apartamentos. Isso faz com que exista uma fila de espera por vagas. Implemente uma fila de espera que contenha os métodos para adicionar
apartamentos na fila, retirar apartamentos informando o número da vaga que este apartamento receberá e um método para imprimir a fila de espera.

3) O condomínio tem apenas 10 vagas de garagem. Então, no monento que o décimo primeiro apartamento for cadastrado, este apartamento deve ir para a fila de espera. Os apartamento que tem vaga de garagem, devem ficar na lista encadeada de apartamento com vaga, ordenados pelo número da vaga. - ok

4) Construa um menu que permita ao wusuário escolher as opções de:

    a) Cadastrar apartamento -> Quando o apartamento for cadastrado, se tiver vaga de garagem disponível, ele deve ir para a lista encadeada, ordenada pelo número da vaga. Se não tiver mais vagas, o apartamento deve ir para a fila de apartamentos que estão esperando a vaga. - ok

    b) Liberar vaga -> O Usuário deve informar o número da vaga que será liberada, então o apartamento que estiver nessa vaga deve ser colocado no fim da fila e o apartamento que estiver no início da fila deve ir para a lista encadeada, assumindo a vaga de garagem que foi liberada.

    c) Imprimir a lista de apartamentos que tem vaga. - ok

    d) Imprimir a fila de apartamentos que estão esperando por vaga de garagem. - ok

> Este trabalho deverá ser apresentado.

# A lista encadeada pode atribuir o valor da vaga ou remover/alerta ou joga na fila
