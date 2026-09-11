# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 

# jogador.zerar_jogador()
# Função para resetar o jogador
# return: Retorna um dicionário com os atributos zerados do jogador
def zerar_jogador() -> dict:
    return {
        "inicializado": False,    
        "username": "",            
        "nome_jardim": "",         
        "arc_score": 0,            
        "arc_score_total": 0,      
        "plantas": list(),        
        "missoes_feitas": dict()   
    }

atributos = zerar_jogador()