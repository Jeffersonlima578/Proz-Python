


def manipular_estoqueCarros(arr):

    fechar = False

    while (fechar == False):

        print("O que deseja fazer ? Digite o Number: " )

        print("1. Ver carros em estoque")

        print("2. Alterar carros")

        print("3. Adicionar carros")

        print("4. Fechar o sistema de carros")

        acao = input()

 

        if (acao == "1"):

            print("Carros em estoque: ")

            for i in range(len(arr)):

                print(str(i) + " - " + arr[i])

 

        elif (acao == "2"):

            print("Qual é o índice de Carros que deseja alterar?")

            indice = int(input())

            print("Qual é o novo modelo de Carros?")

            novo_carro = input()

            arr[indice] = novo_carro

            print("Carros '" + novo_carro + "' adicionado com sucesso")

 

        elif (acao == "3"):

            print("Qual Carros deseja adicionar?")

            novo_carro = input()

            arr.append(novo_carro)

            print("Carros '" + novo_carro + "' adicionado com sucesso")

 

        elif (acao == "4"):

            print("Fechando sistema de carros...")

            fechar = True

 

        else:

            print("Por favor informe um carro válido")

 

 

carros = ["gol", "vectra", "uno", "opala"]

manipular_estoqueCarros(carros)

 