frase = str(input("Digite uma frase: "))

lista_palavras = frase.split(" ")
lista_palavras = [palavra for palavra in lista_palavras if palavra]

lista_palavras_unicas = []
lista_palavras_unicas = [palavra for palavra in lista_palavras if palavra not in lista_palavras_unicas]

# Quantidade de palavras
print(f"-Total de palavras únicas: {len(lista_palavras_unicas)}")

# Maior de menor palavra
print(f"-Mais longa: {max(lista_palavras_unicas, key=len)}\n -Mais curta: {min(lista_palavras_unicas, key=len)}")

# Palavras que começam com vogal
lista_vogais_inicio = [palavra for palavra in lista_palavras if palavra[0].lower() in "aeiou"]
print(f"-Palavras que começam com vogal: {lista_vogais_inicio}")

# Frase invertida
lista_palavras_invertidas = [palavra[::-1] for palavra in lista_palavras]
print("-Frase invertida: ", end="")
for palavra in lista_palavras_invertidas:
    print(palavra, end=" ")
else:
    print()

# Média de caracteres
media = 0
for palavra in lista_palavras_unicas:
    media += len(palavra)

media = media/len(lista_palavras_unicas)
print(f"-Média de caracteres por palavra: {media:.2f}")


# Ordem alfabética inversa

print(f"-Palavras em ordem alfabética inversa: {sorted(lista_palavras_invertidas, reverse=True)}")

