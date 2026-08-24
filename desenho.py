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

import os
import time

# -------------------- DESENHOS --------------------

# desenho.linha()
# Procedimento que desenha uma linha no terminal
# :param tam: Define o tamanho que a linha vai ser, por padrão 80 chars.
# :return: Não retorna nada.
def linha(tam: int = 40) -> None:
    print("-" * tam)

# desenho.titulo()
# Procedimento que desenha um titulo formatado
# :param titulo: É basicamente o texto que fica no título.
# :param tam: Define o tamanho que o titulo vai ser, por padrão 80 chars.
# :return: Não retorna nada.
def titulo(titulo: str, separado: bool = False,  tam: int = 40) -> None:
    linha(tam)
    
    if (separado == True):
        print(f"{separar(titulo).upper():^{tam}}")
    else:
        print(f"{titulo.upper():^{tam}}")
        
    linha(tam)

# -------------------- OUTROS --------------------

# desenho.limpar()
# Procedimento que limpa o texto do terminal
# :return: Não retorna nada.
def limpar() -> None:
    if (os.name == "nt"): # se for o windows
        os.system("cls")
    else:
        os.system("clear")

# desenho.espera_entrada()
# Procedimento que faz o terminal esperar uma entrada
# :return: Não retorna nada.
def espera_entrada() -> None:
    print("")
    input("PRESSIONE [ENTER] PARA CONTINUAR. . .")

# desenho.separar()
# Procedimento que pega um texto e retorna ele só que separado por cada caractere com " ".
# :param texto: É o texto a ser separado
# :return: Retorna o texto separado por espaços.
def separar(texto: str) -> str:
    texto_formatado = ""
    
    for caractere in list(texto):
        texto_formatado += caractere + " "
    
    return texto_formatado
