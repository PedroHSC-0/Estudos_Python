opcao = int(input("1-) Ceusius para Fahrenheit\n2-) Fahrenheit para Ceusius\n"))
temp = float(input("Insira a temperatura: "))

if(opcao == 1):
    temp = temp * 9/5 + 32
    print(f"-> {temp:.2f}°F")

elif(opcao == 2):
    temp = (temp - 32) * 5/9
    print(f"-> {temp:.2f}°C")

