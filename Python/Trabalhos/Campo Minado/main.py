from funcoes import aviso, perdeu, venceu, input_dados, gerar_campo, iniciar_jogo

tamanho, n_minas = input_dados()

campo, coodenadas_minas = gerar_campo(tamanho, n_minas)

while(True):
    resultado = iniciar_jogo(campo, coodenadas_minas)

    if resultado:
        venceu()
    else:
        perdeu()  

    try:
        opcao = int(input("Deseja jogar novamente? (0 -> Não | 1 -> Sim)"))

    except:
        opcao = 0
    
    if opcao:
        continue
    else:
        break

aviso("Finalizando programa", 1)
