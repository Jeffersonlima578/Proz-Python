
#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

#1: Soma
2#: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 



def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtracao")
        print("3: Multiplicacao")
        print("4: Divisao")
        print("0: Sair")
        
        opcao = input("Digite o numero para a operacao correspondente: ")
        
        if opcao == "0":
            break
        elif opcao in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            
            if opcao == "1":
                resultado = num1 + num2
                print("Resultado: ", resultado)
            elif opcao == "2":
                resultado = num1 - num2
                print("Resultado: ", resultado)
            elif opcao == "3":
                resultado = num1 * num2
                print("Resultado: ", resultado)
            elif opcao == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    print("Resultado: ", resultado)
                else:
                    print("Não é possível dividir por zero")
        else:
            print("Essa opção não existe")
        print() # Linha em branco para separar as repetições do loop
    
calculadora()