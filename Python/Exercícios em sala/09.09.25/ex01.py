bandas = []

n = int(input("Digite o número de bandas que você quer inserir: "))

print("Digite os nomes das suas bandas preferidas: ")
for i in range(0, n):
    banda = input()
    bandas.append(banda)

print("\n")

for i in bandas:
    print(i, end=", ")

