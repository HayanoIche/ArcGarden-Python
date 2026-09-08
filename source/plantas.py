# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------

# |  Arquivo auxiliar com as funções das plantas

# -------------------- BIBLIOTECAS --------------------
from bibliotecas import desenho
import menu

# -------------------- VARIÁVEIS DAS PLANTAS --------------------

lista_de_plantas = list()

# -------------------- FUNÇÕES --------------------

# ----- CRUD -----
def adicionar(planta_nome: str, planta_tipo: str, planta_xp: int, planta_xp_maximo: int, planta_descricao: str) -> bool:

    lista_de_plantas.append(
        {
            "nome": planta_nome,
            "nivel_inicial": 1,
            "nivel_maximo": 5,
            "tipo": planta_tipo,
            "xp_atual": planta_xp,
            "xp_maximo": planta_xp_maximo,
            "descricao": planta_descricao
        }
    )

    return True

def atualizar(planta: dict, opcao: str) -> bool:

    match opcao:

        case "1":
            novo_nome = input("NOVO NOME DA PLANTA: ")

            if pegar(novo_nome) != None:
                print("ERRO! ESSA PLANTA JÁ EXISTE!")
                return False

            planta["nome"] = novo_nome

        case "2":
            menu.desenhar("Tipo da planta")

            escolha = input("Escolha: ")

            match escolha:
                case "1":
                    planta["tipo"] = "COMUM"

                case "2":
                    planta["tipo"] = "RARO"

                case "3":
                    planta["tipo"] = "ULTRA RARO"

                case _:
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

        case "3":
            while True:
                try:
                    xp = int(input("NOVO XP ATUAL: "))

                    if xp < 0:
                        print("ERRO! O XP NÃO PODE SER NEGATIVO!")
                    elif xp > planta["xp_maximo"]:
                        print("ERRO! O XP ATUAL NÃO PODE SER MAIOR QUE O XP MÁXIMO!")
                    else:
                        planta["xp_atual"] = xp
                        break

                except ValueError:
                    print("ERRO! O XP DEVE SER UM NÚMERO INTEIRO!")

        case "4":
            while True:
                try:
                    xp_maximo = int(input("NOVO XP MÁXIMO: "))

                    if xp_maximo < 0:
                        print("ERRO! O XP MÁXIMO NÃO PODE SER NEGATIVO!")
                    elif xp_maximo < planta["xp_atual"]:
                        print("ERRO! O XP MÁXIMO NÃO PODE SER MENOR QUE O XP ATUAL!")
                    else:
                        planta["xp_maximo"] = xp_maximo
                        break

                except ValueError:
                    print("ERRO! O XP DEVE SER UM NÚMERO INTEIRO!")

        case "5":
            planta["descricao"] = input("NOVA DESCRIÇÃO: ")

        case _:
            return False

    return True

def pegar(planta_nome: str) -> dict | None:
    for planta in lista_de_plantas:
        if planta.get("nome") == planta_nome:
            return planta

    return None

def remover(planta_nome: str):
    for num, item in enumerate(lista_de_plantas):
        if (item.get("nome") != None):
            if (item.get("nome") == planta_nome):
                lista_de_plantas.pop(num)
                return True
    
    return False

def criando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("CRIANDO PLANTA")

    while True:
        nome = input("NOME DA PLANTA: ")
        if nome == "":
            print("ERRO! O NOME NÃO PODE FICAR VAZIO!")

        if pegar(nome) != None:
            print("ERRO! ESSA PLANTA JÁ EXISTE!")

        else:
            break

    while True:
        menu.desenhar("Tipo da planta")

        escolha = input("Escolha: ")

        match escolha:
            case "1":
                tipo = "COMUM"
                break

            case "2":
                tipo = "RARO"
                break

            case "3":
                tipo = "ULTRA RARO"
                break

            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    while True:
        try:
            xp = int(input("XP INICIAL: "))

            if xp < 0:
                print("ERRO! O XP NÃO PODE SER NEGATIVO!")
            else:
                break

        except ValueError:
            print("ERRO! O XP DEVE SER UM NÚMERO INTEIRO!")

    while True:
        try:
            xp_maximo = int(input("XP MÁXIMO: "))

            if xp_maximo < 0:
                print("ERRO! O XP NÃO PODE SER NEGATIVO!")

            elif xp_maximo < xp:
                print("ERRO! O XP MÁXIMO NÃO PODE SER MENOR QUE O XP INICIAL!")

            else:
                break

        except ValueError:
            print("ERRO! O XP DEVE SER UM NÚMERO INTEIRO!")

    descricao = input("DESCRIÇÃO: ")

    adicionar(nome, tipo, xp, xp_maximo, descricao)

    print(f"PLANTA {nome} CRIADA!")

    desenho.espera_entrada()

def atualizando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EDITANDO PLANTAS")
    print()

    if len(lista_de_plantas) == 0:
        print("NENHUMA PLANTA FOI CRIADA!")
        desenho.espera_entrada()
        return

    for num, planta in enumerate(lista_de_plantas):
        print(f"  {num + 1}. {planta['nome']}")

    print()

    while True:
        try:
            escolha = int(input("QUAL PLANTA DESEJA EDITAR: "))

            if escolha >= 1 and escolha <= len(lista_de_plantas):
                planta = lista_de_plantas[escolha - 1]
                break

            print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

        except ValueError:
            print("ERRO! DIGITE APENAS UM NÚMERO!")

    while True:
        desenho.limpar()
        desenho.linha()
        print()
        desenho.titulo(f"EDITANDO: {planta['nome']}")
        print()

        menu.desenho("Editando planta")

        escolha = input("ESCOLHA: ")

        if escolha == "6":
            break

        resultado = atualizar(planta, escolha)

        if resultado:
            print("PLANTA ATUALIZADA!")
            desenho.espera_entrada()
        else:
            desenho.espera_entrada()

    desenho.espera_entrada()

def listar() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("PLANTAS CADASTRADAS")
    print()

    if len(lista_de_plantas) == 0:
        print("NENHUMA PLANTA FOI CRIADA!")

    else:
        for num, planta in enumerate(lista_de_plantas):
            print(f"PLANTA {num + 1}")
            print(f"NOME.............: {planta['nome']}")
            print(f"NÍVEL INICIAL....: {planta['nivel_inicial']}")
            print(f"NÍVEL MÁXIMO.....: {planta['nivel_maximo']}")
            print(f"TIPO.............: {planta['tipo']}")
            print(f"XP ATUAL.........: {planta['xp_atual']}")
            print(f"XP MÁXIMO........: {planta['xp_maximo']}")
            print(f"DESCRIÇÃO........: {planta['descricao']}")
            print()
            desenho.linha()

    desenho.espera_entrada()

def excluindo() -> None:

    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EXCLUINDO PLANTA")

    if len(lista_de_plantas) == 0:
        print()
        print("NENHUMA PLANTA CADASTRADA!")
        desenho.espera_entrada()
        return

    print()

    for num, planta in enumerate(lista_de_plantas):
        print(f"  {num + 1}. {planta['nome']}")

    print()

    while True:
        escolha = input("QUAL PLANTA DESEJA EXCLUIR: ")

        try:
            escolha = int(escolha)

            if escolha >= 1 and escolha <= len(lista_de_plantas):
                planta = lista_de_plantas[escolha - 1]

                print()
                print(f"PLANTA SELECIONADA: {planta['nome']}")
                confirmar = input("DESEJA REALMENTE EXCLUIR? (S/N): ").upper()

                if confirmar == "S":
                    remover(planta["nome"])
                    print(f"PLANTA {planta['nome']} EXCLUÍDA!")
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