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
import jogador, missoes, plantas, loja

# -------------------- PROGRAMA PRINCIPAL --------------------

while app.rodando:
    
    if app.modo_execucao == "none":
        app.rodar_menu_escolha_modo_execucao()
    
    elif app.modo_execucao == "jogador":
        app.rodar_menu_jogador(
            jogador.atributos,
            missoes.lista_de_missoes,
            loja.lista_de_pacotes
        )
    
    elif app.modo_execucao == "sistema":
        app.rodar_menu_sistema(
            missoes.lista_de_missoes,
            plantas.lista_de_tipos_plantas,
            loja.lista_de_pacotes,
            jogador.atributos
        )