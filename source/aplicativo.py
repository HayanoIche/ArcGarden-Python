# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# |  Arquivo auxiliar com as funções do app

# -------------------- BIBLIOTECAS --------------------

import menu
from bibliotecas import desenho

# -------------------- VARÍAVEIS DO APLICATIVO --------------------

# Se o programa deve ser fechado ou não
rodando = True

# Qual o modo de execução escolhido
modo_execucao = "none"

# -------------------- FUNÇÕES DO APLICATIVO --------------------

def parar_programa():
    global rodando
    rodando = False

def mudar_modo_execucao(modo: str):
    global modo_execucao

    modo_execucao = modo

# -------------------- FUNÇÕES GERAIS DOS MENUS --------------------

# ----- INICIO DO PROGRAMA -----
def rodar_menu_escolha_modo_execucao():
    menu.desenhar("Inicial")
    
    # ----- ESCOLHA -----
    escolha = input("Escolha: ")
    desenho.limpar()
    
    match(escolha):
        case "0":
            parar_programa()
            print("\n\nArcGarden - feito por ARCEUS...")
            print("Programa fechado!\n\n")
            
        case "1":
            mudar_modo_execucao("jogador")
        
        case "2":
            mudar_modo_execucao("sistema")

        case "3":
            desenho.titulo("CRÉDITOS", separado=True)
            menu.desenhar_creditos()
            desenho.espera_entrada()
        
        case _:
            print("ERRO! Opção inválida!")
            desenho.espera_entrada()

# ----- MENU DO JOGO -----
def rodar_menu_jogador():
    desenho.limpar()
    desenho.espera_entrada()

# ----- MENU DO SISTEMA -----
def rodar_menu_sistema():
    menu.desenhar("Gerenciador")
    escolha = input("Escolha: ")
    
    match(escolha):
        case "1":
            rodar_menu_gerenciar_missoes()
            
        case "2":
            rodar_menu_gerenciar_plantas()
        
        case "4":
            rodar_menu_resetar_jogador()
                                    
        case "5":
            mudar_modo_execucao("none")
        
        case _:
            print("ERRO! Opção inválida!")
            desenho.espera_entrada()

# -------------------- FUNÇÕES DOS MENUS DO SISTEMA --------------------

# ----- MISSOES -----
def rodar_menu_gerenciar_missoes():
    while(True):
        menu.desenhar("Gerenciar Missão")
        escolha = input("Escolha: ")

        match(escolha):
            case "4":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# ----- PLANTAS -----
def rodar_menu_gerenciar_plantas():
    while(True):
        menu.desenhar("Gerenciar Plantas")
        escolha = input("Escolha: ")
        
        match(escolha):
            case "4":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# ----- JOGADOR -----
def rodar_menu_resetar_jogador():
    while(True):
        menu.desenhar("Gerenciar Resetar Jogador")
        escolha = input("Escolha: ")
        
        match(escolha):
            case "1":
                if (jogador["inicializado"] == True):
                    print(f"\n\nJOGADOR {jogador["username"]} RESETADO!\n\n")
                    #jogador = zerar_jogador()
                    desenho.espera_entrada()
                else:
                    print(f"\n\nERRO! O JOGADOR AINDA NÃO FOI INICIALIZADO PARA SER RESETADO\n\n")
                    desenho.espera_entrada()
                break
            case "2":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

