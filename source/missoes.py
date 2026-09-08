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
import menu
from bibliotecas import desenho
# -------------------- VARIÁVEIS DAS MISSÕES --------------------

lista_de_missoes = list()

def adicionar(missao_nome: str, missao_dificuldade: str, missao_pts: int, missao_tempo_qtd: int, missao_tempo: str) -> bool:

    lista_de_missoes.append(
        {
            "nome": missao_nome,
            "dificuldade": missao_dificuldade,
            "pts": missao_pts,
            "tempo_qtd": missao_tempo_qtd,
            "tempo": missao_tempo
        }
    )

    return True

def pegar(missao_nome: str) -> dict | None:
    for missao in lista_de_missoes:
        if missao.get("nome") == missao_nome:
            return missao

    return None

def remover(missao_nome: str) -> bool:
    for num, missao in enumerate(lista_de_missoes):
        if missao.get("nome") == missao_nome:
            lista_de_missoes.pop(num)
            return True

    return False

def atualizar(missao: dict, opcao: str) -> bool:
    match opcao:
        case "1":
            novo_nome = input("NOVO NOME DA MISSÃO: ")
            if novo_nome == "":
                print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
            
            if pegar(novo_nome) != None:
                print("ERRO! ESSA MISSÃO JÁ EXISTE!")
                return False

            missao["nome"] = novo_nome

        case "2":
            menu.desenhar("Dificuldade da missão")

            escolha = input("Escolha: ")

            match escolha:
                case "1":
                    missao["dificuldade"] = "FÁCIL"
                case "2":
                    missao["dificuldade"] = "MÉDIO"
                case "3":
                    missao["dificuldade"] = "DIFÍCIL"
                case "4":
                    missao["dificuldade"] = "ESPECIAL"
                case _:
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

        case "3":
            while True:
                try:
                    pts = int(input("NOVOS PONTOS: "))

                    if pts < 0:
                        print("ERRO! OS PONTOS NÃO PODEM SER NEGATIVOS!")
                    else:
                        missao["pts"] = pts
                        break

                except ValueError:
                    print("ERRO! OS PONTOS DEVEM SER UM NÚMERO INTEIRO!")

        case "4":
            while True:
                try:
                    tempo_qtd = int(input("NOVA QUANTIDADE DE TEMPO: "))

                    if tempo_qtd <= 0:
                        print("ERRO! A QUANTIDADE DE TEMPO DEVE SER MAIOR QUE ZERO!")
                    else:
                        missao["tempo_qtd"] = tempo_qtd
                        break

                except ValueError:
                    print("ERRO! A QUANTIDADE DE TEMPO DEVE SER UM NÚMERO INTEIRO!")

        case "5":
            menu.desenhar("Tipo de tempo")

            escolha = input("Escolha: ")

            match escolha:
                case "1":
                    missao["tempo"] = "DIA"
                case "2":
                    missao["tempo"] = "SEMANA"
                case "3":
                    missao["tempo"] = "MÊS"
                case _:
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

        case _:
            return False

    return True

def criando() -> None:

    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("CRIANDO MISSÃO")

    while True:
        nome = input("NOME DA MISSÃO: ")
        if nome == "":
            print("ERRO! O NOME NÃO PODE FICAR VAZIO!")

        if pegar(nome) != None:
            print("ERRO! ESSA MISSÃO JÁ EXISTE!")

        else:
            break

    while True:
        menu.desenhar("Dificuldade da missao")
        escolha = input("Escolha: ")

        match escolha:
            case "1":
                dificuldade = "FÁCIL"
                break

            case "2":
                dificuldade = "MÉDIO"
                break

            case "3":
                dificuldade = "DIFÍCIL"
                break

            case "4":
                dificuldade = "ESPECIAL"
                break

            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    while True:
        try:
            pts = int(input("PONTOS DA MISSÃO: "))

            if pts < 0:
                print("ERRO! OS PONTOS NÃO PODEM SER NEGATIVOS!")
            else:
                break

        except ValueError:
            print("ERRO! OS PONTOS DEVEM SER UM NÚMERO INTEIRO!")

    while True:
        menu.desenhar("Tipo de tempo")
        escolha = input("Escolha: ")

        match escolha:
            case "1":
                tempo = "DIA"
                break

            case "2":
                tempo = "SEMANA"
                break

            case "3":
                tempo = "MÊS"
                break

            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    while True:
        try:
            tempo_qtd = int(input("QUANTIDADE DE TEMPO: "))

            if tempo_qtd <= 0:
                print("ERRO! A QUANTIDADE DE TEMPO DEVE SER MAIOR QUE ZERO!")
            else:
                break

        except ValueError:
            print("ERRO! A QUANTIDADE DE TEMPO DEVE SER UM NÚMERO INTEIRO!")


    adicionar(nome, dificuldade, pts, tempo_qtd, tempo)

    print(f"MISSÃO {nome} CRIADA!")

    desenho.espera_entrada()


def atualizando() -> None:

    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EDITANDO MISSÕES")
    print()

    if len(lista_de_missoes) == 0:
        print("NENHUMA MISSÃO FOI CRIADA!")
        desenho.espera_entrada()
        return

    for num, missao in enumerate(lista_de_missoes):
        print(f"  {num + 1}. {missao['nome']}")

    print()

    while True:
        try:
            escolha = int(input("QUAL MISSÃO DESEJA EDITAR: "))

            if escolha >= 1 and escolha <= len(lista_de_missoes):
                missao = lista_de_missoes[escolha - 1]
                break

            print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

        except ValueError:
            print("ERRO! DIGITE APENAS UM NÚMERO!")

    while True:

        desenho.limpar()
        desenho.linha()
        print()
        desenho.titulo(f"EDITANDO: {missao['nome']}")
        print()

        menu.desenhar("Editando missão")

        escolha = input("ESCOLHA: ")

        if escolha == "6":
            break

        resultado = atualizar(missao, escolha)

        if resultado:
            print("MISSÃO ATUALIZADA!")

        desenho.espera_entrada()

    desenho.espera_entrada()

def excluindo() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EXCLUINDO MISSÃO")

    if len(lista_de_missoes) == 0:
        print()
        print("NENHUMA MISSÃO CADASTRADA!")
        desenho.espera_entrada()
        return

    print()

    for num, missao in enumerate(lista_de_missoes):
        print(f"  {num + 1}. {missao['nome']}")

    print()

    while True:
        try:
            escolha = int(input("QUAL MISSÃO DESEJA EXCLUIR: "))

            if escolha >= 1 and escolha <= len(lista_de_missoes):
                missao = lista_de_missoes[escolha - 1]

                print()
                print(f"MISSÃO SELECIONADA: {missao['nome']}")
                confirmar = input("DESEJA REALMENTE EXCLUIR? (S/N): ").upper()

                if confirmar == "S":
                    remover(missao["nome"])
                    print(f"MISSÃO {missao['nome']} EXCLUÍDA!")
                    break

                elif confirmar == "N":
                    print("EXCLUSÃO CANCELADA!")
                    break

                else:
                    print("ERRO! DIGITE S OU N!")

            else:
                print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

        except ValueError:
            print("ERRO! DIGITE APENAS NÚMEROS!")

    desenho.espera_entrada()

def listar() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("MISSÕES CADASTRADAS")
    print()

    if len(lista_de_missoes) == 0:
        print("NENHUMA MISSÃO FOI CRIADA!")

    else:
        desenho.linha()

        for num, missao in enumerate(lista_de_missoes):
            print(f"MISSÃO {num + 1}")
            print(f"NOME.................: {missao['nome']}")
            print(f"DIFICULDADE..........: {missao['dificuldade']}")
            print(f"PONTOS...............: {missao['pts']}")
            print(f"QUANTIDADE DE TEMPO..: {missao['tempo_qtd']}")
            print(f"TIPO DE TEMPO........: {missao['tempo']}")
            print()
            desenho.linha()
            
    desenho.espera_entrada()