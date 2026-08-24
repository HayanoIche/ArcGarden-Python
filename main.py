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

# -------------------- FUNÇÕES DO PROGRAMA --------------------

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
                desenhar_creditos()
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

        escolha = input("Escolha: ")

        match(escolha):
            case "1":
                while(True):
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
                    desenho.espera_entrada()
                    break
            case _:
                print("ERRO! Opção inválida!")
                desenho.espera_entrada()
