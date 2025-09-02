senha = input("Digite a senha: ")

print(f"Tamanho da senha: {len(senha)}")

print(f"Tem '@': {"@" in senha}")

print(f"Tem mais de 8 caracteres: {len(senha) > 8}")