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

# -------------------- PROGRAMA PRINCIPAL --------------------

rodando = True

while (rodando == True):
    desenho.limpar()
    desenho.titulo("ARC GARDEN", separado=True)
    desenho.espera_entrada()
