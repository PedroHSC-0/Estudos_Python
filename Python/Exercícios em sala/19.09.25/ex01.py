lista = [i for i in range(1, 101)]
lista_primos = []

for n in lista:
    for i in range(1, n):
        if 1 < i:
            if n % i == 0:
                break
    else:
        lista_primos.append(n)

        
            

print(lista_primos)
