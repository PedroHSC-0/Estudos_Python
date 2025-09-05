idade = int(input("Digite sua idade: "))

if(idade < 16):
    print("Você não pode votar.")

elif(idade >= 16 and idade < 18 or idade > 70):
    print("Você pode votar. (Voto facultativo)")

elif(idade >= 18 and idade < 70):
    print("Você pode votar. (Voto obrigatório)")

