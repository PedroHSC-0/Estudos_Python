def fibonacci(n, n1 = 0, n2 = 1):
    if(n == 0):
        return 1
    else:
        aux = n1
        n1 = n2
        n2 = aux + n2
        print(n1, end = " ")
        return fibonacci(n - 1, n1 = n1, n2 = n2)

while(True):
    
    opcao = int(input("Selecione a opção: " \
    "1-) Sequência de Fibonacci de n termos" \
    "2-) " \
    "3-)" \
    "4-)" \
    "5-) Fechar programa"))

    if(opcao == 1):
        fibonacci(n)
    
    elif(opcao == 5):
        break
    :
