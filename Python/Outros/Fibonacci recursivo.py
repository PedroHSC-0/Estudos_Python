def fibonacci(n, n1 = 0, n2 = 1):
    if(n == 0):
        print("\n")
        return 1
    else:
        aux = n1
        n1 = n2
        n2 = aux + n2
        print(n1, end = " ")
        return fibonacci(n - 1, n1 = n1, n2 = n2)



while(True):
    
    print("Selecione a opção: \n" \
    "1-) Sequência de Fibonacci de n termos\n" \
    "2-) \n" \
    "3-) \n" \
    "4-) \n" \
    "5-) Fechar programa\n")
    opcao = int(input())

    if(opcao == 1):
        n = int(input("Insira o número de termos: "))
        fibonacci(n)
        print
    
    elif(opcao == 5):
        break

