from random import randint
import os
import time

# Função para avisar erro personalizado
def aviso_erro(mensagem, atraso):
    os.system('cls')
    time.sleep(0.5)
    print(mensagem, end="")
    for i in range(3):
        time.sleep(atraso)
        print(".", end="", flush=True)

    time.sleep(atraso)
    os.system('cls')

# Função de entrada de dados(Tamanho do campo e número de minas)
def input_dados():
    while(True):
        try:
            tamanho = int(input("Insira o tamanho do campo minado: "))
            while(True):
                try: 
                    n_minas = int(input("Insira o número de minas contidas no campo: "))
                    break
                
                except:
                    aviso_erro("Insira um número inteiro", 0.5)
                    continue
            break

        except:
            aviso_erro("Insira um número inteiro", 0.5)
            continue
    return tamanho, n_minas

# Função para gerar o campo minado aleatóriamente, com minas posicionadas aleatóriamente
def gerar_campo(tamanho, n_minas):
    campo = [["*" for i in range(tamanho)] for i in range(tamanho)]
    coordenadas_minas = []
    while(n_minas > 0):
        coordenada = (randint(0, tamanho - 1), randint(0, tamanho - 1))
        if(not (coordenada in coordenadas_minas)):
            coordenadas_minas.append(coordenada)
            n_minas -= 1
            
    print(coordenadas_minas)
    return campo

tamanho, n_minas = input_dados()

campo  = gerar_campo(tamanho, n_minas)




print(campo)