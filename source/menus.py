# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# |  Biblioteca para desenhos formatados
# |  no terminal, desenvolvida por Matheus
# |  Vidal e Igor Hayano

# -------------------- IMPORTS --------------------

# Biblioteca de Desenhos no terminal
import desenho as desenho

# -------------------- DESENHOS NO GERAL --------------------

def desenhar_logo() -> None:
    print("""     _-|                                                
    |_-|                 ____               _           
    / \   _ __ ___     / ___| __ _ _ __ __| | ___ _ __  
   / _ \ | '__/ __|   | |  _ / _` | '__/ _` |/ _ \ '_ \ 
  / ___ \| | | (__    | |_| | (_| | | | (_| |  __/ | | |
 /_/   \_\_|  \___|    \____|\__,_|_|  \__,_|\___|_| |_|
 ------------------   ---------------------------------- 
                                                - ARCEUS""")

def desenhar_creditos() -> None:
    print("""
    Conheça o time ARCEUS:
    
    IGOR MATEUS DA SILVA
    
      - Github: https://github.com/HayanoIche
      - Linkedin: https://www.linkedin.com/in/igor-mateus-da-silva-4b05013ba/
    
    MARCELA BATISTA TEIXEIRA
    
      - Github: https://github.com/wonbindasilva
      - Linkedin: https://www.linkedin.com/in/marcelabteixeira/
    
    MATHEUS PEREIRA VIDAL
    
      - Github: https://github.com/pereirinh44
      - Linkedin: https://linkedin.com/in/matheus-pereira-8700893b3
    
    FRANCO JARED MARQUINA
    
      - Github: https://github.com/Fmarquina
      - Linkedin: https://www.linkedin.com/in/franco-jared-marquina-blas-b67851303/
    """)

# -------------------- DESENHOS DOS MENUS --------------------

def desenhar_menu_inicial() -> None:
    # ----- DESENHANDO AS OPÇÕES -----
    desenho.limpar()
    desenho.linha()
    desenhar_logo()
    desenho.linha()
    desenho.menu(
        ["Jogar","Gerenciar Sistema", "Créditos"],
        descricao="Escolha o que deseja fazer:",
        sair=True
    )
    desenho.linha()
    print()

def desenhar_menu_gerenciador() -> None:
    desenho.limpar()
    desenho.linha()
    desenhar_logo()
    desenho.linha()
    print()
    desenho.titulo("SISTEMA")
    desenho.menu(
        [
            "Gerenciar Missões",
            "Gerenciar Plantas",
            "Gerenciar Loja",
            "Resetar Jogador",
            "Voltar"
        ],
        descricao="Escolha o que deseja fazer:",
        sair=False
    )
    desenho.linha()
    print()

def desenhar_menu_gerenciador_missoes() -> None:
    desenho.limpar()
    desenho.linha()
    desenhar_logo()
    desenho.linha()
    print()
    desenho.titulo("SISTEMA")
    desenho.menu(
        [
            "Criar Missão",
            "Atualizar Missão",
            "Excluir Missão",
            "Voltar"
        ],
        descricao="Escolha o que deseja fazer:",
        sair=False
    )
    desenho.linha()
    print()


def desenhar_menu_gerenciador_plantas() -> None:
    desenho.limpar()
    desenho.linha()
    desenhar_logo()
    desenho.linha()
    print()
    desenho.titulo("SISTEMA")
    desenho.menu(
        [
            "Criar Planta",
            "Atualizar Planta",
            "Excluir Planta",
            "Voltar"
        ],
        descricao="Escolha o que deseja fazer:",
        sair=False
    )
    desenho.linha()
    print()

def desenhar_menu_gerenciador_excluir_jogador() -> None:
    desenho.limpar()
    desenho.linha()
    desenhar_logo()
    desenho.linha()
    print()
    desenho.titulo("SISTEMA")
    desenho.menu(
        [
            "Sim",
            "Não",
        ],
        descricao="Deseja mesmo resetar o jogador local da maquina?",
        sair=False
    )
    desenho.linha()
    print()