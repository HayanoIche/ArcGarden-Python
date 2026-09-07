# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# |  Arquivo auxiliar com as funções das missões

# -------------------- BIBLIOTECAS --------------------

# -------------------- FUNÇÕES --------------------

def zerar_jogador() -> dict:
    return {
        "inicializado": False,
        
        "username": "",
        "nome jardim": "",
        "arc score": 0,
        "plantas": list()
    }

# -------------------- VARIÁVEIS --------------------

atributos = zerar_jogador()