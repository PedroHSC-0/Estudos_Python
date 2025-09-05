usuario_correto = "Pedro"
senha_correta = "1994"

usuario = str(input("Digite o usuário: "))
senha = input("Digite a senha: ")

if(usuario == usuario_correto and senha == senha_correta):
    print("Autenticação bem sucedida!")

else:
    print("Usuário ou senha incorretos")

