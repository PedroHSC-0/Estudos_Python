from random import randint
import os
import time
from shutil import get_terminal_size

largura_terminal = get_terminal_size().columns

# Função que gera aviso personalizado (Void)
def aviso(mensagem, atraso):
    os.system('cls')
    print(mensagem, end="")
    for i in range(3):
        time.sleep(atraso)
        print(".", end="", flush=True)

    time.sleep(atraso)
    os.system('cls')

# Função que gera mensagem de derrota (Void)
def perdeu():
    os.system('cls')
    mensagem = r"""
    |--------------------------------------|
    | |¨¨¨¨\    /¨¨¨¨\  /¨¨¨¨\  |\      /| |
    | |     )  |      ||      | | \    / | |
    | |¨¨¨¨¨)  |      ||      | |  \  /  | |
    | |____/    \____/  \____/  |   \/   | |
    |--------------------------------------|

    """
    print(mensagem.center(largura_terminal))
    print("PERDEU")
    
    for i in range(40):
        time.sleep(0.1)
        print(".", end="", flush=True)

    os.system('cls')

# Função que gera mensagem de vitória (Void)
def venceu():
    os.system('cls')
    mensagem = r"""
    |----------------------------------------| 
    |  \      /\      /    0     |\   |   |  | 
    |   \    /  \    /     |     | \  |   |  | 
    |    \  /    \  /      |     |  \ |   |  | 
    |     \/      \/       |     |   \|   0  | 
    |----------------------------------------|
    """
    print(mensagem.center(largura_terminal))
    print("VENCEU")
    
    for i in range(40):
        time.sleep(0.1)
        print(".", end="", flush=True)

    os.system('cls')

# Função de entrada de dados Tamanho do campo e número de minas
def input_dados():
    while(True):
        try:
            tamanho = int(input("Insira o tamanho do campo minado: (Max: 10) "))
            
            if(tamanho > 10):
                aviso("Insira um tamanho menor ou igual a 10", 0.5)
                continue

            while(True):
                try:
                    n_minas = int(input("Insira o número de minas contidas no campo: "))
                    break
                
                except:
                    aviso("Insira um número inteiro", 0.5)
                    continue
            break

        except:
            aviso("Insira um número inteiro", 0.5)
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
            
    return campo, coordenadas_minas

# Função para mostrar o campo atual
def mostrar_campo(campo):
    for linha in campo:

        linha_str = "".join(f"| {coordenada} " for coordenada in linha) + "|"
        print(linha_str.center(largura_terminal))

#Leitura e tratamento da entrada de dados das coordenadas
def ler_coordenadas():

    while(True):
        coordenadas_str = str(input("Insira a coordenada da casa que será aberta(x, y):"))
        if "," in coordenadas_str:
            x, y = coordenadas_str.split(",")
            x = int(x.strip())
            y = int(y.strip())
            
        else:
            aviso("Insira uma coordenada válida, Ex: 5, 6")

def verificar_redor(campo):

# Função que inicia e executa o jogo
def iniciar_jogo(campo, coordenadas_minas):
    aviso("INICIANDO CAMPO MINADO", 0,7)

    while(True):
        mostrar_campo(campo)
        coordenadas = ler_coordenadas()

        
        if(coordenadas in  coordenadas_minas):
            campo[coordenadas[0]][coordenadas[1]] = 0
            mostrar_campo(campo)
            return False
    

