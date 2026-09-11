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
                    "Ver Missões",
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
                    "Ver Plantas",
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


        # Menu para mostrar os possiveis tipos de planta
        case "Tipo da planta":
            desenho.menu(
                [
                    "COMUM",
                    "RARO",
                    "ULTRA RARO"
                ],
                descricao="Escolhao tipo da planta: ",
                sair=False
            )

        # Menu para mostrar as opções de edição das plantas
        case "Editando planta":  
            desenho.menu(
                [
                    "NOME",
                    "CATEGORIA",
                    "XP MÁXIMO",
                    "DESCRIÇÃO",
                    "VOLTAR"
                ],
                descricao="O QUE DESEJA ALTERAR: ",
                sair=False
            )
        # Menu para mostrar as dificuldades possiveis das missões 
        case "Dificuldade da missao":
            desenho.menu(
                [
                    "FÁCIL",
                    "MÉDIO",
                    "DIFÍCIL",
                    "ESPECIAL"
                ],
                descricao="Escolha a dificuldade da missão: ",
                sair=False
            )

        # Menu para mostrar os possiveis tempos para concluir uma missão
        case "Tipo de tempo":
            desenho.menu(
                [
                    "DIA",
                    "SEMANA",
                    "MÊS"
                ],
                descricao="Escolha o tipo de tempo: ",
                sair=False
            )

        case "Editando missão":
            desenho.menu(
                [
                    "NOME",
                    "DIFICULDADE",
                    "PONTOS",
                    "QUANTIDADE DE TEMPO",
                    "TIPO DE TEMPO",
                    "VOLTAR"
                ],
                descricao="Escolha o que deseja editar: ",
                sair=False
            )

        case "Gerenciar Loja":
            desenho.limpar()
            desenho.linha()
            desenhar_logo()
            desenho.linha()
            desenho.titulo("Gerenciar Pacotes")
            desenho.menu(
                [
                    "Criar Pacote",
                    "Atualizar Pacote",
                    "Excluir Pacote",
                    "Mostrar Pacotes",
                    "Voltar"
                ],
                descricao="Escolha uma opção: ",
                sair=False
            )

        case "Editando pacote":
            desenho.menu(
                [
                    "NOME",
                    "PREÇO",
                    "ADICIONAR PLANTA",
                    "REMOVER PLANTA",
                    "VOLTAR"
                ],
                descricao="Escolha o que deseja editar: ",
                sair=False
            )

        case "Adicionar Planta":
            desenho.menu(
        [
            "PLANTA COMUM",
            "PLANTA RARA",
            "PLANTA ULTRA RARA",
            "VOLTAR"
        ],
        descricao="Coloque plantas no pacote: ",
        sair=False
    )

        case "Jogador":
            desenho.limpar()
            desenho.linha()
            desenhar_logo()
            desenho.linha()
            print()
            desenho.titulo("MODO JOGO")
            desenho.menu(
                [
                    "Ver Missões",
                    "Simular Missões",
                    "Ver Arc-Score",
                    "Gerenciar Jardim",
                    "Abrir Pacote",
                    "Ver Ranking",
                    "Voltar"
                ],
                descricao="Escolha uma opção:",
                sair=False
            )
            desenho.linha()
            print()