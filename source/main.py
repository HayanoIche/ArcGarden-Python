# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------

# -------------------- BIBLIOTECAS --------------------

import aplicativo as app

# -------------------- PROGRAMA PRINCIPAL --------------------

while (app.rodando):
    
    if (app.modo_execucao == "none"):
        app.rodar_menu_escolha_modo_execucao()
    
    elif (app.modo_execucao == "jogador"):
        app.rodar_menu_jogador()
    
    elif (app.modo_execucao == "sistema"):
        app.rodar_menu_sistema()

"""

# ----- VARIÁVEIS DO JOGO -----

plantas = list()    # Lista de todas as plantas
missoes = list()    # Lista de todas as missões

def zerar_jogador() -> dict:
    return {
        "inicializado": False,
        
        "username": "bunderson",
        "nome jardim": "",
        "arc score": 0,
        "plantas": list()
    }

jogador = zerar_jogador()


"""