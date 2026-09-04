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

# Biblioteca de Desenhos no terminal
from bibliotecas import desenho
from bibliotecas import arquivos

# -------------------- DESENHOS NO GERAL --------------------

def desenhar_logo() -> None:
    print(arquivos.pegar_conteudo("./textos/logo.txt"))
    print("                                                - ARCEUS")

def desenhar_creditos() -> None:
    print(arquivos.pegar_conteudo("./textos/creditos.txt"))

# -------------------- DESENHOS DOS MENUS --------------------

def desenhar(index: str) -> None:
    match index:
        # Menu de escolher se vai jogar ou gerenciar
        case "Inicial":
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

        # Menu geral do gerenciador
        case "Gerenciador":
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

        # Menu de gerenciar as missões
        case "Gerenciar Missão":
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

        # Menu de gerenciar as plantas
        case "Gerenciar Plantas":
            desenho.limpar()
            desenho.linha()
            desenhar_logo()
            desenho.linha()
            print()
            desenho.titulo("SISTEMA")
            desenho.menu(
                [
                    "Criar Planta",
                    "Atualizar Planta",
                    "Excluir Planta",
                    "Voltar"
                ],
                descricao="Escolha o que deseja fazer:",
                sair=False
            )
            desenho.linha()
            print()

        # Menu de resetar o jogador
        case "Gerenciar Resetar Jogador":
            desenho.limpar()
            desenho.linha()
            desenhar_logo()
            desenho.linha()
            print()
            desenho.titulo("SISTEMA")
            desenho.menu(
                [
                    "Sim",
                    "Não",
                ],
                descricao="Deseja mesmo resetar o jogador local da maquina?",
                sair=False
            )
            desenho.linha()
            print()
