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
# Biblioteca dos Desenhos dos menus
import menus

# -------------------- PROGRAMA PRINCIPAL --------------------

# ----- VARIÁVEIS DO PROGRAMA -----

rodando = True              # Se o programa ainda está rodando
navegacao_atual = "inicio"  # Em qual etapa do programa estamos

# ----- VARIÁVEIS DO JOGO -----

plantas = list()    # Lista de todas as plantas
missoes = list()    # Lista de todas as missões

jogador = {
    "username": "",
    "nome jardim": "",
    "arc score": 0,
    "plantas": list()
}

while (rodando == True):
    # ----- INICIO DO PROGRAMA -----
    if (navegacao_atual == "inicio"):
        menus.desenhar_menu_inicial()
        
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

            case "3":
                desenho.limpar()
                desenho.titulo("CRÉDITOS", separado=True)
                menus.desenhar_creditos()
                desenho.espera_entrada()
            
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

    # ----- JOGANDO O ARC GARDEN -----
    elif (navegacao_atual == "jogando"):
        desenho.limpar()
        desenho.espera_entrada()
        
    # ----- GERENCIANDO O SISTEMA -----
    elif (navegacao_atual == "gerenciando sistema"):
        menus.desenhar_menu_gerenciador()

        escolha = input("Escolha: ")

        match(escolha):
            case "1":
                while(True):
                    menus.desenhar_menu_gerenciador_missoes()
                    escolha = input("Escolha: ")

                    match(escolha):
                        case "4":
                            break
                        case _:
                            print("ERRO! Opção inválida!")
                            desenho.espera_entrada()
                            
            case "5":
                navegacao_atual = "inicio"
                continue
            
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

