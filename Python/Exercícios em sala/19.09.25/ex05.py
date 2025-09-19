from random import randint, randrange

lista1 = []
lista2 = [randrange(0, 101, 2) for i in range(10)]

while (len(lista1) < 10):
    n = randint(0, 100)
    if n % 2 == 0:
        lista1.append(n)


        
    
print(lista1[::-1])
print(lista2[::-1])