lista_milhao = []

for i in range(1000000):
    lista_milhao.append(i)

for i in lista_milhao:
    print(i, end=", ")

print(sum(lista_milhao))