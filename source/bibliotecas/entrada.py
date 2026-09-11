# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# |  Biblioteca para inputs com segurança
# |  no terminal, desenvolvida por Matheus
# |  Vidal e Igor Hayano

import sys

# entrada.real()
# Função que pega um input do tipo float do usuário de forma segura
def real(msg: str) -> float:
    while True:
        try:
            print(msg, end="")
            valor = float(input())
            return valor
        except ValueError:
            print("Erro! Valor digitado não é um número válido.")
        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            print("Erro não identificado!")

# entrada.inteiro()
# Função que pega um input do tipo integer do usuário de forma segura
def inteiro(msg: str) -> int:
    while True:
        try:
            print(msg, end="")
            valor = int(input())
            return valor
        except ValueError:
            print("Erro! Valor digitado não é um número válido.")
        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            print("Erro não identificado!")