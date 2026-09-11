# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 

# -------------------- BIBLIOTECAS --------------------
import menu, plantas, missoes, loja, jogador, jogar
from bibliotecas import desenho

# -------------------- VARÍAVEIS DO APLICATIVO --------------------

rodando = True
modo_execucao = "none"

# -------------------- FUNÇÕES DO APLICATIVO --------------------

# aplicativo.parar_programa()
# Procedimento que desliga a variável de execução para fechar o main.py
# return: Não retorna nada
def parar_programa() -> None:
    import aplicativo
    aplicativo.rodando = False

# aplicativo.mudar_modo_execucao()
# Procedimento que muda a execução atual da aplicação
# param modo: String ('none', 'jogador', 'sistema')
# return: Não retorna nada.
def mudar_modo_execucao(modo: str) -> None:
    import aplicativo
    aplicativo.modo_execucao = modo

# -------------------- ROTEAMENTO DE MENUS --------------------

# aplicativo.rodar_menu_escolha_modo_execucao()
# Procedimento do menu inicial do app
# return: Não retorna nada
def rodar_menu_escolha_modo_execucao() -> None:
    menu.desenhar("Inicial")
    escolha = input("Escolha: ").strip()
    desenho.limpar()
    
    match escolha:
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

# aplicativo.rodar_menu_jogador()
# Procedimento de controle do menu do jogador
# return: Não retorna nada.
def rodar_menu_jogador() -> None:
    jogar.cadastrar_jogador_se_necessario(jogador.atributos)

    while modo_execucao == "jogador":
        menu.desenhar("Jogador")
        escolha = input("Escolha: ").strip()

        match escolha:
            case "1":
                missoes.listar()
            case "2":
                jogar.simular_missoes(jogador.atributos, missoes.lista_de_missoes)
            case "3":
                jogar.ver_arc_score(jogador.atributos)
            case "4":
                jogar.gerenciar_jardim(jogador.atributos)
            case "5":
                jogar.abrir_pacote(jogador.atributos, loja.lista_de_pacotes)
            case "6":
                jogar.ver_ranking(jogador.atributos)
            case "7":
                mudar_modo_execucao("none")
                return
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_sistema()
# Procedimento do menu do gerenciador do sistema
# return: Não retorna nada
def rodar_menu_sistema() -> None:
    menu.desenhar("Gerenciador")
    escolha = input("Escolha: ").strip()
    
    match escolha:
        case "1":
            rodar_menu_gerenciar_missoes()
        case "2":
            rodar_menu_gerenciar_plantas()
        case "3":
            rodar_menu_gerenciar_loja()
        case "4":
            rodar_menu_resetar_jogador()                        
        case "5":
            mudar_modo_execucao("none")
        case _:
            print("ERRO! Opção inválida!")
            desenho.espera_entrada()

# -------------------- SUBMENUS DO GERENCIADOR DE SISTEMA --------------------

# aplicativo.rodar_menu_gerenciar_missoes()
# Procedimento de controle do menu de CRUD de missões
# return: Não retorna nada
def rodar_menu_gerenciar_missoes() -> None:
    while True:
        menu.desenhar("Gerenciar Missão")
        escolha = input("Escolha: ").strip()

        match escolha:
            case "1":
                missoes.criando()
            case "2":
                missoes.atualizando()
            case "3":
                missoes.excluindo()
            case "4":
                missoes.listar()
            case "5":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_gerenciar_plantas()
# Procedimento de controle do menu de CRUD de Tipos de Plantas
# return: Não retorna nada
def rodar_menu_gerenciar_plantas() -> None:
    while True:
        menu.desenhar("Gerenciar Plantas")
        escolha = input("Escolha: ").strip()
        
        match escolha:
            case "1":
                plantas.criando()
            case "2":
                plantas.atualizando()
            case "3":
                plantas.excluindo()
            case "4":
                plantas.listar()
            case "5":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_gerenciar_loja()
# Procedimento de controle do menu de CRUD de pacotes da loja
# return: Não retorna nada
def rodar_menu_gerenciar_loja() -> None:
    while True:
        menu.desenhar("Gerenciar Loja")
        escolha = input("Escolha: ").strip()

        match escolha:
            case "1":
                loja.criando()
            case "2":
                loja.atualizando()
            case "3":
                loja.excluindo()
            case "4":
                loja.listar()
            case "5":
                break
            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_resetar_jogador()
# Procedimento de confirmação para limpar o progresso e perfil do jogador
# return: Não retorna nada
def rodar_menu_resetar_jogador() -> None:
    while True:
        menu.desenhar("Gerenciar Resetar Jogador")
        escolha = input("Escolha: ").strip()
        
        match escolha:
            case "1":
                if jogador.atributos["inicializado"]:
                    username = jogador.atributos["username"]
                    jogador.atributos = jogador.zerar_jogador()
                    print(f"\n\nJOGADOR {username} RESETADO!\n\n")
                    desenho.espera_entrada()
                else:
                    print("\n\nERRO! O JOGADOR AINDA NÃO FOI INICIALIZADO PARA SER RESETADO\n\n")
                    desenho.espera_entrada()
                break
            case "2":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()