n_vogais = 0
n_consoantes = 0

frase = str(input())


for letra in frase.lower().replace(" ", ""):
    if(letra.isalpha()):
        print(letra)
        if letra in "aeiou":
            n_vogais += 1
        else:
            n_consoantes += 1

print(f"-Número de vogais: {n_vogais}")
print(f"-Número de consoantes: {n_consoantes}")

if "engenharia" in frase:
    print("-engenharia está na frase")

print(f"-{frase[::-1]}")