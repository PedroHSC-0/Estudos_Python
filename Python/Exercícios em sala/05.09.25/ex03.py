n = int(input("Digite um número inteiro: "))

if(n % 2 == 0):
    print("Par e", end= " ")

elif(n % 2 != 0):
    print("Ímpar e", end=" ")

if(n > 0):
    print("Positivo")

elif(n < 0):
    print("Negativo")

else:
    print("Nulo")