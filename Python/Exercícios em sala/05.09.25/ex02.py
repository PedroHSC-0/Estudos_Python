peso = float(input("Digite seu peso (em Kg):"))
altura = float(input("Digite sua altura (em metros):"))

imc = peso / altura**2

print(f"{imc:.2f}\n\n")

if(imc < 18.5):
    print("Abaixo do peso")

elif(imc >= 18.5 and imc < 24.9):
    print("Peso normal")

elif(imc >= 24.9 and imc < 29.9):
    print("Sobrepeso")

elif(imc > 30):
    print("Obesidade")