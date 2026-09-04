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
# :param msg: É a mensagem que vai ser exibida pro usuário
# :return: Retorna o valor real pego no input.
def real(msg: str) -> float:
    valor = ""

    while type(valor) != float:
        try:
            print(msg, end="")
            valor = float(input())
        except ValueError:
            print("Erro! Valor digitado não é um número válido")
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Erro não indentificado!")

# entrada.inteiro()
# Função que pega um input do tipo integer do usuário de forma segura
# :param msg: É a mensagem que vai ser exibida pro usuário
# :return: Retorna o valor inteiro pego no input.
def inteiro(msg: str) -> int:
    valor = ""
    
    while type(valor) != int:
        try:
            print(msg, end="")
            valor = int(input())
        except ValueError:
            print("Erro! Valor digitado não é um número válido")
        except KeyboardInterrupt:
                    sys.exit()
        except:
            print("Erro não indentificado!")
