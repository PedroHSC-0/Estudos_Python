impares = []
multiplos_tres = []
cubos = []

for i in range(1, 20, 2):
    impares.append(i)

for impar in impares: print(impar, end=", ")


for i in range(1, 30, 3):
    multiplos_tres.append(i)

for multiplo in  multiplos_tres: print(multiplo, end=", ")

for i in range(10):
    cubos.append(i**3)


for cubo in cubos: print(cubo, end=", ")
