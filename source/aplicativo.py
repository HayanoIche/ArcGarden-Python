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

# -------------------- VARIÁVEIS DO APLICATIVO --------------------

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
def mudar_modo_execucao(m: str) -> None:
    import aplicativo
    aplicativo.modo_execucao = m

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
# param j: Dicionário contendo atributos do jogador
# param m: Lista de missões
# param l: Lista de pacotes da loja
# return: Não retorna nada.
def rodar_menu_jogador(j: dict, m: list, l: list) -> None:
    jogar.cadastrar_jogador_se_necessario(j)

    while modo_execucao == "jogador":
        menu.desenhar("Jogador")
        escolha = input("Escolha: ").strip()

        match escolha:
            case "1":
                missoes.listar(m)
            case "2":
                jogar.simular_missoes(j, m)
            case "3":
                jogar.ver_arc_score(j)
            case "4":
                jogar.gerenciar_jardim(j)
            case "5":
                jogar.abrir_pacote(j, l)
            case "6":
                jogar.ver_ranking(j)
            case "7":
                mudar_modo_execucao("none")
                return
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_sistema()
# Procedimento do menu do gerenciador do sistema
# param m: Lista de missões
# param p: Lista de tipos de plantas
# param l: Lista de pacotes da loja
# param j: Dicionário contendo atributos do jogador
# return: Não retorna nada
def rodar_menu_sistema(m: list, p: list, l: list, j: dict) -> None:
    menu.desenhar("Gerenciador")
    escolha = input("Escolha: ").strip()
    
    match escolha:
        case "1":
            rodar_menu_gerenciar_missoes(m)
        case "2":
            rodar_menu_gerenciar_plantas(p)
        case "3":
            rodar_menu_gerenciar_loja(l, p)
        case "4":
            rodar_menu_resetar_jogador(j)                        
        case "5":
            mudar_modo_execucao("none")
        case _:
            print("ERRO! Opção inválida!")
            desenho.espera_entrada()

# -------------------- SUBMENUS DO GERENCIADOR DE SISTEMA --------------------

# aplicativo.rodar_menu_gerenciar_missoes()
# Procedimento de controle do menu de CRUD de missões
# param m: Lista de missões
# return: Não retorna nada
def rodar_menu_gerenciar_missoes(m: list) -> None:
    while True:
        menu.desenhar("Gerenciar Missão")
        escolha = input("Escolha: ").strip()

        match escolha:
            case "1":
                missoes.criando(m)
            case "2":
                missoes.atualizando(m)
            case "3":
                missoes.excluindo(m)
            case "4":
                missoes.listar(m)
            case "5":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_gerenciar_plantas()
# Procedimento de controle do menu de CRUD de Tipos de Plantas
# param p: Lista de tipos de plantas
# return: Não retorna nada
def rodar_menu_gerenciar_plantas(p: list) -> None:
    while True:
        menu.desenhar("Gerenciar Plantas")
        escolha = input("Escolha: ").strip()
        
        match escolha:
            case "1":
                plantas.criando(p)
            case "2":
                plantas.atualizando(p)
            case "3":
                plantas.excluindo(p)
            case "4":
                plantas.listar(p)
            case "5":
                break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_gerenciar_loja()
# Procedimento de controle do menu de CRUD de pacotes da loja
# param l: Lista de pacotes da loja
# param p: Lista de tipos de plantas
# return: Não retorna nada
def rodar_menu_gerenciar_loja(l: list, p: list) -> None:
    while True:
        menu.desenhar("Gerenciar Loja")
        escolha = input("Escolha: ").strip()

        match escolha:
            case "1":
                loja.criando(l, p)
            case "2":
                loja.atualizando(l, p)
            case "3":
                loja.excluindo(l)
            case "4":
                loja.listar(l)
            case "5":
                break
            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")
                desenho.espera_entrada()

# aplicativo.rodar_menu_resetar_jogador()
# Procedimento de confirmação para limpar o progresso e perfil do jogador
# param j: Dicionário contendo atributos do jogador
# return: Não retorna nada
def rodar_menu_resetar_jogador(j: dict) -> None:
    while True:
        menu.desenhar("Gerenciar Resetar Jogador")
        escolha = input("Escolha: ").strip()
        
        match escolha:
            case "1":
                if j["inicializado"]:
                    username = j["username"]
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