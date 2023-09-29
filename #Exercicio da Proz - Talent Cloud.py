#Exercicio da Proz - Talent Cloud 

                    #Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
                    # Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
                    #Escreva um código que imprima todos os números exceto o número 13.
                #Escreva mais dois códigos que resolvam o mesmo problema,
                # mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
                    #Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
# Solução 1: Usando um laço de repetição while

andar = 1

while andar <= 20:
    if andar != 13:
            print(andar)
    andar += 1

                    # Solução 2: Usando um laço de repetição for

for andar in range(1, 21):
    if andar != 13:
        print(andar)

                    # Solução 3: Usando um laço de repetição do-while (não presente nativamente em Python)
                    # No exemplo abaixo, vamos simular um laço do-while com um laço while

andar = 1

while True:
    if andar != 13:
        print(andar)
    
    andar += 1
    
    if andar == 21:
        break

                        # Desafio: imprimir em ordem decrescente

                        # Solução 1: Usando um laço de repetição for

for andar in range(20, 0, -1):
    if andar != 13:
        print(andar)

                        # Solução 2: Usando um laço de repetição while

andar = 20

while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1

                        # Solução 3: Usando um laço de repetição do-while (não presente nativamente em Python)
                        # No exemplo abaixo, vamos simular um laço do-while com um laço while

andar = 20

while True:
    if andar != 13:
        print(andar)
    
    andar -= 1
    
    if andar == 0:
        break
