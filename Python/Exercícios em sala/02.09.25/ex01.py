nome = input("Digite o nome completo: ")

#Nome completo em letras minúsculas
print(nome.lower())
#Nome completo em letras maiúsculas
print(nome.upper())
#Número de letras (sem considerar espaços)
print(len(nome.replace(" ", "")))
#Número de letras do primeiro nome
print(len(nome.partition(" ")[0]))