senha = str(input("Digite sua senha:"))

if len(senha) < 8:
    print("Senha menor que 8 caracteres")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_caractere_especial = False

for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True

    if caractere.islower():
        tem_minuscula = True

    if caractere.isnumeric():
        tem_numero = True

    if not caractere.replace(" ", "").isalnum():
        tem_caractere_especial = True

    
print(f"-Tem número? {tem_numero}")
print(f"-Tem letra maiúscula? {tem_maiuscula}")
print(f"-Tem letra minúscula? {tem_minuscula}")
print(f"-Tem caractere especial? {tem_caractere_especial}")

