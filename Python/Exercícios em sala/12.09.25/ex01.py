lista = []
lista_removidos = []
nome = ""
mensagem = "|" + "-Olá meu querido amigo {nome}, você está convidado ao meu aniversário.".center()

while(True): 
    lista.append(str(input("Digite o nome do convidado: ")))
    opcao = int(input("Deseja adicionar mais alguém? [0]Não [1]Sim\n"))
    if(opcao == 0):
        break

print("--------------------------------------------------------------------------------------")
for nome in lista:
    print(mensagem)
print("--------------------------------------------------------------------------------------")

opcao = int(input("\nDeseja remover alguém? [0]Não [1]Sim\n"))
while(opcao == 1):
    try:
        opcao == -1
        nome = str(input("Insira o nome de quem você quer remover: (Digite 0 para parar)"))
        lista.remove(nome)
        lista_removidos.append(nome)
        print(f"{nome} foi removido da lista.")
        opcao = int(input("\nDeseja remover mais alguém? [0]Não [1]Sim\n"))
    except:
        break

print("--------------------------------------------------------------------------------------")
for nome in lista:
    print(f"Olá meu querido amigo {nome}, você está convidado ao meu aniversário.")
print("--------------------------------------------------------------------------------------")

print("\n Convidados que não vão comparecer: ")
for nome in lista_removidos:
    print(f"-{nome}")

    