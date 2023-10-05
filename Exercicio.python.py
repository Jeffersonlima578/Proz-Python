

def mostrarNumero():
    print("Escreva um número que seja menor ou igual a 100")
    num = int(input())

    numeroValido = False
    while(numeroValido == False):
        try:
            if(num > 100):
                print("O número precisa ser menor ou igual a 100")
            else:
                frase = "Você escolheu o número " + str(num)
                numeroValido = True
                return frase
        except:
            print("O valor digitado deve ser um número inteiro")
            

def calcularDivisao():
    print("Digite dois números para realizar a divisão")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Verifica se o segundo número é zero para evitar divisão por zero
    if num2 == 0:
        print("Não é possível realizar uma divisão por zero")
    else:
        resultado = num1 / num2
        print("O resultado da divisão é: ", resultado)