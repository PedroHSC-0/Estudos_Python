from random import randint

lista = []

for i in range(20):
    lista.append(randint(1,80))

print(f"Lista: {lista}")
print(f"O menor número: {max(lista)}")
print(f"O menor número: {min(lista)}")
print(f"Amplitude da lista: {max(lista) - min(lista)}")
print(f"Soma dos números: {sum(lista)}")
print(f"A média simples: {sum(lista)/20}")
print(f"A média dos 10 primeiros números: {sum(lista[:10])/10}")
print(f"O máximo dos 10 últimos elementos: {max(lista[11:])}")
print(f"O mínimo dos 10 últimos elementos: {min(lista[11:])}")