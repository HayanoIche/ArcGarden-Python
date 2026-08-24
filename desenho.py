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
    
# desenho.menu()
# Procedimento que desenha um menu com indices (1 - tal tal tal...)
# :param opcoes: Uma lista com as opções a serem desenhadas.
# :param descricao: Uma descrição a ser desenhada em cima do menu.
# :param sair: se vai ter a opção 0 de sair no menu.
# :param espacamento: espaçamento entre as opções e o inicio da linha.
# :return: Não retorna nada.
def menu(opcoes: list,
         descricao: str = "",
         sair: bool = False,
         espacamento: int= 4) -> None:
    
    print()
    
    if (descricao != ""):
        print(f"{" "*(espacamento - 1)}{descricao}")
        print()
    
    for i, opcao in enumerate(opcoes, start=1):    
        print(f"{i:>{espacamento}} - {opcao}")
    
    if (sair == True):
        print(f"{"0":>{espacamento}} - Sair")
    
    print()

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
