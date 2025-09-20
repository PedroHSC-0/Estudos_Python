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
    time.sleep(2)
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
    os.system('cls')
    while(True):
        try: 
            tamanho = int(input("Insira o tamanho do campo minado: (2 a 10) "))
        except:
            aviso("Insira um número inteiro", 0.5)
        
        
        
        # Caso o tamanho não seja válido
        if(not (2 <= tamanho <= 10)):
            aviso("Insira um tamanho entre 2 e 10", 0.7)
            continue

        while(True):
            try:
                n_minas = int(input("Insira o número de minas contidas no campo: "))
                if(n_minas > tamanho**2 or n_minas < 1):
                    aviso("Digite uma quantidade válida", 0.5)
                    continue         
            
            except:
                aviso("Insira um número inteiro", 0.5)
                continue
            break
        break

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

# Função para leitura e tratamento da entrada de dados das coordenadas
def ler_coordenadas():

    while(True):
        try:
            coordenadas_str = str(input("Insira a coordenada da casa que será aberta(linha, coluna):"))
            if "," in coordenadas_str:
                linha, coluna = coordenadas_str.split(",")
                linha = int(linha.strip())
                coluna = int(coluna.strip())
                return (linha, coluna)
                
            else:
                aviso("Insira uma coordenada válida, Ex: 5, 6")
        except:
            aviso("Insira uma coordenada válida, Ex: 5, 6")

# Função para verificar e marcar o redor da coordenada aberta pelo jogador
def atualizar_campo(campo, posicao, coordenadas_minas):
    # Limpando a posição
    linha = posicao[0]
    coluna = posicao[1]
    

    

    return campo

# Função que verifica se todas as minas estão marcadas
def verificar_posicoes_minas(campo, coordenadas_minas):
    for coordenada in coordenadas_minas:
        if campo[coordenada[0]][coordenada[1]] != "M":
            return False
    else:
        return True

# Função que inicia e executa o jogo
def jogar(campo, coordenadas_minas):
    aviso("INICIANDO CAMPO MINADO", 0.7)

    while(True):
        os.system('cls')
        mostrar_campo(campo)
        coordenada = ler_coordenadas()
        
        if(coordenada in coordenadas_minas):
            atualizar_campo(campo, coordenada)
            mostrar_campo(campo)
            return False
        else:
            campo = atualizar_campo(campo, coordenada)

