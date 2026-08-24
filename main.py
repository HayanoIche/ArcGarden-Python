# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------

# -------------------- BIBLIOTECAS --------------------

# Biblioteca do Sistema
import os
# Biblioteca de Tempo
import time
# Biblioteca de Desenhos no terminal
import desenho

# -------------------- PROGRAMA PRINCIPAL --------------------

rodando = True
navegacao_atual = "inicio"

while (rodando == True):
    # ----- INICIO DO PROGRAMA -----
    if (navegacao_atual == "inicio"):
        # ----- DESENHANDO AS OPÇÕES -----
        desenho.limpar()
        desenho.titulo("ARC GARDEN", separado=True)
        desenho.menu(
            ["Jogar","Gerenciar Sistema"],
            descricao="Escolha o que deseja fazer:",
            sair=True
        )
        desenho.linha()
        print()
        
        # ----- ESCOLHENDO -----
        escolha = input("Escolha: ")
        match(escolha):
            case "0":
                desenho.limpar()
                rodando = False
                print("\n\nArcGarden - feito por ARCEUS...")
                print("Programa fechado!\n\n")

            case "1":
                navegacao_atual = "jogando"
                continue
            
            case "2":
                navegacao_atual = "gerenciando sistema"
                continue
            
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

    # ----- JOGANDO O ARC GARDEN -----
    elif (navegacao_atual == "jogando"):
        desenho.limpar()
        print("JOGAR: A SER IMPLEMENTADO!")
        desenho.espera_entrada()
        
    # ----- GERENCIANDO O SISTEMA -----
    elif (navegacao_atual == "gerenciando sistema"):
        desenho.limpar()
        print("GERENCIAR: A SER IMPLEMENTADO!")
        desenho.espera_entrada()
