verificacao_nome = False
verificacao_idade = False
verificacao_senha = False

nome = str(input("Digite seu nome completo: ")) 

# Verificação do nome -> Se não é nulo, e se a primeira letra é vogal
if(not nome == None):
    if(nome.lower()[0] in "aeiou"):
        verificacao_nome = True
        print("Verificado")

idade = str(input("Digite sua idade: "))

# Verificação da idade -> Se não é nulo (Bool), se idade é maior ou igual à 18
if(bool(idade) and idade.isnumeric() and int(idade) >= 18):
    verificacao_idade = True
    print("Verificado")
        
        
senha = str(input("Insira sua senha: ")) 

# Verificação da senha -> Se não inicia com "1234", se não inicia com "admin"
if(senha != "1234" and senha.lower().startswith("admin")):
    if(senha.isnumeric()):
        senha = int(senha) + 10
        
    print("Verificado")


# Verificação Final -> se as 3 verificações forem verdadeiras
if(verificacao_nome and verificacao_idade and verificacao_senha):
    print("Acesso Permitido.")

else: 
    print("Acesso Negado.")

