# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# |  Arquivo auxiliar com as funções da loja

# -------------------- BIBLIOTECAS --------------------
import plantas, menu
from bibliotecas import desenho
# -------------------- VARIÁVEIS DAS LOJA --------------------
lista_de_pacotes = list()
# -------------------- FUNÇÕES --------------------

def adicionar(pacote_nome: str, pacote_preco: int) -> bool:

    lista_de_pacotes.append(
        {
            "nome": pacote_nome,
            "preco": pacote_preco,
            "plantas_comuns": list(),
            "plantas_raras": list(),
            "plantas_ultra_raras": list()
        }
    )

    return True

def pegar(pacote_nome: str) -> dict | None:
    for pacote in lista_de_pacotes:
        if pacote.get("nome") == pacote_nome:
            return pacote

    return None


def remover(pacote_nome: str) -> bool:
    for num, pacote in enumerate(lista_de_pacotes):
        if pacote.get("nome") == pacote_nome:
            lista_de_pacotes.pop(num)
            return True

    return False

def criando() -> None:
    while True:
        desenho.limpar()
        nome = input("NOME DO PACOTE: ")

        if nome == "":
            print("ERRO! O NOME DO PACOTE NÃO PODE FICAR VAZIO!")

        elif pegar(nome) != None:
            print("ERRO! ESSE PACOTE JÁ EXISTE!")

        else:
            break

    while True:
        try:
            preco = int(input("PREÇO DO PACOTE: "))

            if preco < 0:
                print("ERRO! O PREÇO NÃO PODE SER NEGATIVO!")
            else:
                break

        except ValueError:
            print("ERRO! O PREÇO DEVE SER UM NÚMERO INTEIRO!")

    adicionar(nome, preco)

    pacote = pegar(nome)

    while True:
        print()
        menu.desenhar("Adicionar Planta")

        escolha = input("Escolha: ")

        match escolha:
            case "1":
                adicionar_planta(pacote, "COMUM")

            case "2":
                adicionar_planta(pacote, "RARO")

            case "3":
                adicionar_planta(pacote, "ULTRA RARO")

            case "4":
                break

            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    print(f"PACOTE {nome} CRIADO!")

def adicionar_planta(pacote: dict, tipo: str) -> None:
    plantas_disponiveis = list()

    for planta in plantas.lista_de_plantas:
        if planta["tipo"] == tipo:
            plantas_disponiveis.append(planta)

    if len(plantas_disponiveis) == 0:
        print("NENHUMA PLANTA DESSE TIPO FOI CADASTRADA!")
        return

    print(f"PLANTAS {tipo}:")
    
    for num, planta in enumerate(plantas_disponiveis):
        print(f"{num + 1} - {planta['nome']}")

    try:
        escolha = int(input("Escolha a planta: "))

        if escolha < 1 or escolha > len(plantas_disponiveis):
            print("ERRO! OPÇÃO INVÁLIDA!")
            return

        planta_escolhida = plantas_disponiveis[escolha - 1]

        match tipo:
            case "COMUM":
                lista = pacote["plantas_comuns"]

            case "RARO":
                lista = pacote["plantas_raras"]

            case "ULTRA RARO":
                lista = pacote["plantas_ultra_raras"]

        if planta_escolhida in lista:
            print("ERRO! ESSA PLANTA JÁ ESTÁ NO PACOTE!")
            return

        lista.append(planta_escolhida)

        print(f"PLANTA {planta_escolhida['nome']} ADICIONADA!")

    except ValueError:
        print("ERRO! DIGITE UM NÚMERO!")

def listar() -> None:
    print()
    desenho.linha()
    desenho.titulo("PACOTES DA LOJA")
    desenho.linha()
    print()

    if len(lista_de_pacotes) == 0:
        print("NENHUM PACOTE FOI CRIADO!")
    else:
        for num, pacote in enumerate(lista_de_pacotes):
            print(f"PACOTE {num + 1}")
            print(f"NOME........: {pacote['nome']}")
            print(f"PREÇO.......: {pacote['preco']}")

            print("PLANTAS COMUNS:")
            for planta in pacote["plantas_comuns"]:
                print(f"- {planta['nome']}")

            print("PLANTAS RARAS:")
            for planta in pacote["plantas_raras"]:
                print(f"- {planta['nome']}")

            print("PLANTAS ULTRA RARAS:")
            for planta in pacote["plantas_ultra_raras"]:
                print(f"- {planta['nome']}")

            desenho.linha()
    desenho.espera_entrada()
    

def excluindo() -> None:
    if len(lista_de_pacotes) == 0:
        print("NENHUM PACOTE FOI CRIADO!")
        return

    desenho.linha()
    desenho.titulo("EXCLUIR PACOTE")
    desenho.linha()

    for num, pacote in enumerate(lista_de_pacotes):
        print(f"{num + 1} - {pacote['nome']}")

    try:
        escolha = int(input("Escolha o pacote: "))

        if escolha < 1 or escolha > len(lista_de_pacotes):
            print("ERRO! OPÇÃO INVÁLIDA!")
            return

        pacote = lista_de_pacotes[escolha - 1]

        confirmacao = input(f"DESEJA REALMENTE EXCLUIR O PACOTE {pacote['nome']}? (S/N): ").upper()

        if confirmacao == "S":
            remover(pacote["nome"])
            print("PACOTE EXCLUÍDO COM SUCESSO!")

        elif confirmacao == "N":
            print("EXCLUSÃO CANCELADA!")

        else:
            print("ERRO! OPÇÃO INVÁLIDA!")

    except ValueError:
        print("ERRO! DIGITE UM NÚMERO!")

    desenho.espera_entrada()

def atualizar(pacote: dict, opcao: str) -> bool:
    match opcao:
        case "1":
            while True:
                novo_nome = input("NOVO NOME DO PACOTE: ")

                if novo_nome == "":
                    print("ERRO! O NOME DO PACOTE NÃO PODE FICAR VAZIO!")
                elif novo_nome != pacote["nome"] and pegar(novo_nome) != None:
                    print("ERRO! ESSE PACOTE JÁ EXISTE!")
                else:
                    pacote["nome"] = novo_nome
                    break

        case "2":
            while True:
                try:
                    novo_preco = int(input("NOVO PREÇO DO PACOTE: "))

                    if novo_preco < 0:
                        print("ERRO! O PREÇO NÃO PODE SER NEGATIVO!")
                    else:
                        pacote["preco"] = novo_preco
                        break

                except ValueError:
                    print("ERRO! O PREÇO DEVE SER UM NÚMERO INTEIRO!")

        case "3":
            while True:
                menu.desenhar("Adicionar Planta")
                escolha = input("Escolha: ")

                match escolha:
                    case "1":
                        adicionar_planta(pacote, "COMUM")
                    case "2":
                        adicionar_planta(pacote, "RARO")
                    case "3":
                        adicionar_planta(pacote, "ULTRA RARO")
                    case "4":
                        break
                    case _:
                        print("ERRO! OPÇÃO INVÁLIDA!")
                        desenho.espera_entrada()

        case "4":
            plantas_do_pacote = (
                pacote["plantas_comuns"]
                + pacote["plantas_raras"]
                + pacote["plantas_ultra_raras"]
            )

            if len(plantas_do_pacote) == 0:
                print("NENHUMA PLANTA FOI ADICIONADA AO PACOTE!")
                return False

            for num, planta in enumerate(plantas_do_pacote):
                print(f"{num + 1} - {planta['nome']}")

            try:
                escolha = int(input("Escolha a planta que deseja remover: "))

                if escolha < 1 or escolha > len(plantas_do_pacote):
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

                planta = plantas_do_pacote[escolha - 1]

                if planta in pacote["plantas_comuns"]:
                    pacote["plantas_comuns"].remove(planta)
                elif planta in pacote["plantas_raras"]:
                    pacote["plantas_raras"].remove(planta)
                else:
                    pacote["plantas_ultra_raras"].remove(planta)

                print("PLANTA REMOVIDA DO PACOTE!")

            except ValueError:
                print("ERRO! DIGITE UM NÚMERO!")

        case _:
            return False

    return True

def atualizando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("Atualizar Pacote")
    print()

    if len(lista_de_pacotes) == 0:
        print("NENHUM PACOTE FOI CRIADO!")
        desenho.linha()
        desenho.espera_entrada()
        return

    desenho.linha()

    for num, pacote in enumerate(lista_de_pacotes):
        print(f"{num + 1} - {pacote['nome']}")

    print()

    try:
        escolha = int(input("Escolha o pacote: "))

        if escolha < 1 or escolha > len(lista_de_pacotes):
            print("ERRO! OPÇÃO INVÁLIDA!")
            desenho.espera_entrada()
            return

    except ValueError:
        print("ERRO! DIGITE UM NÚMERO!")
        desenho.espera_entrada()
        return

    pacote = lista_de_pacotes[escolha - 1]

    while True:
        desenho.limpar()
        menu.desenhar("Editando pacote")
        escolha = input("Escolha: ")

        if escolha == "5":
            break

        resultado = atualizar(pacote, escolha)

        if resultado:
            print("PACOTE ATUALIZADO!")

        desenho.espera_entrada()