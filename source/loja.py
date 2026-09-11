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
from bibliotecas import desenho, entrada

# -------------------- VARIÁVEIS DA LOJA --------------------

# Lista pré pronta com pacotes e plantas adicionadas nos pacotes
lista_de_pacotes = [
    {
        "nome": "PACOTE INICIANTE",
        "preco": 20,
        "plantas_comuns": [plantas.lista_de_tipos_plantas[0], plantas.lista_de_tipos_plantas[1]],
        "plantas_raras": [],
        "plantas_ultra_raras": []
    },
    {
        "nome": "PACOTE RARO",
        "preco": 75,
        "plantas_comuns": [],
        "plantas_raras": [plantas.lista_de_tipos_plantas[2]],
        "plantas_ultra_raras": []
    }
]

# -------------------- FUNÇÕES DE CRUD --------------------

# loja.adicionar()
# Procedimento que cadastra um novo pacote na lista de pacotes da loja
# param: pacote_nome Nome do pacote
# param: pacote_preco Custo em Arc-Score
# return: Retorna True após cadastrar
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

# loja.pegar()
# Função que busca um pacote na lista pelo seu nome
# param pacote_nome: Nome do pacote
# return: Retorna o dicionário do pacote ou None se não encontrar nada
def pegar(pacote_nome: str) -> dict | None:
    for pacote in lista_de_pacotes:
        if pacote.get("nome") == pacote_nome:
            return pacote
    return None

# loja.remover()
# Função que deleta um pacote da loja pelo nome
# param pacote_nome: Nome do pacote a remover
# return: Retorna True se remover, False caso contrário
def remover(pacote_nome: str) -> bool:
    for num, pacote in enumerate(lista_de_pacotes):
        if pacote.get("nome") == pacote_nome:
            lista_de_pacotes.pop(num)
            return True
    return False

# -------------------- GERENCIAMENTO DE CONTEÚDO DOS PACOTES --------------------

# loja.adicionar_planta()
# Procedimento que vincula um TipoPlanta a um pacote filtrando pela categoria
# param pacote: Dicionário do pacote a ser modificado
# param categoria: Categoria da planta (COMUM, RARO, ULTRA RARO)
# return: Não retorna nada
def adicionar_planta(pacote: dict, categoria: str) -> None:
    plantas_disponiveis = list()

    for p in plantas.lista_de_tipos_plantas:
        if p["categoria"] == categoria:
            plantas_disponiveis.append(p)

    if len(plantas_disponiveis) == 0:
        print("NENHUM TIPO DE PLANTA DESSA CATEGORIA FOI CADASTRADO!")
        return

    print(f"PLANTAS {categoria}:")
    for num, p in enumerate(plantas_disponiveis):
        print(f"{num + 1} - {p['nome']}")

    escolha = entrada.inteiro("Escolha a planta: ")
    if escolha < 1 or escolha > len(plantas_disponiveis):
        print("ERRO! OPÇÃO INVÁLIDA!")
        return

    planta_escolhida = plantas_disponiveis[escolha - 1]

    match categoria:
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

# -------------------- TELAS E PROCEDIMENTOS DE GERENCIAMENTO --------------------

# loja.criando()
# Procedimento de interface para criação interativa de pacotes na loja
# return: Não retorna nada
def criando() -> None:
    while True:
        desenho.limpar()
        nome = input("NOME DO PACOTE: ").strip().upper()

        if nome == "":
            print("ERRO! O NOME DO PACOTE NÃO PODE FICAR VAZIO!")
        elif pegar(nome) is not None:
            print("ERRO! ESSE PACOTE JÁ EXISTE!")
        else:
            break

    while True:
        preco = entrada.inteiro("PREÇO DO PACOTE: ")
        if preco < 0:
            print("ERRO! O PREÇO NÃO PODE SER NEGATIVO!")
        else:
            break

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

# loja.listar()
# Procedimento que lista na tela todos os pacotes e suas respectivas plantas
# return: Não retorna nada
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
            for p in pacote["plantas_comuns"]:
                print(f"- {p['nome']}")

            print("PLANTAS RARAS:")
            for p in pacote["plantas_raras"]:
                print(f"- {p['nome']}")

            print("PLANTAS ULTRA RARAS:")
            for p in pacote["plantas_ultra_raras"]:
                print(f"- {p['nome']}")

            desenho.linha()
            
    desenho.espera_entrada()

# loja.excluindo()
# Procedimento de interface para exclusão de um pacote da loja
# return: Não retorna nada
def excluindo() -> None:
    if len(lista_de_pacotes) == 0:
        print("NENHUM PACOTE FOI CRIADO!")
        return

    desenho.linha()
    desenho.titulo("EXCLUIR PACOTE")
    desenho.linha()

    for num, pacote in enumerate(lista_de_pacotes):
        print(f"{num + 1} - {pacote['nome']}")

    escolha = entrada.inteiro("Escolha o pacote: ")
    if escolha < 1 or escolha > len(lista_de_pacotes):
        print("ERRO! OPÇÃO INVÁLIDA!")
        return

    pacote = lista_de_pacotes[escolha - 1]
    confirmacao = input(f"DESEJA REALMENTE EXCLUIR O PACOTE {pacote['nome']}? (S/N): ").upper().strip()

    if confirmacao == "S":
        remover(pacote["nome"])
        print("PACOTE EXCLUÍDO COM SUCESSO!")
    elif confirmacao == "N":
        print("EXCLUSÃO CANCELADA!")
    else:
        print("ERRO! OPÇÃO INVÁLIDA!")

    desenho.espera_entrada()

# loja.atualizar()
# Função que edita um atributo do pacote selecionado
# param pacote: Dicionário do pacote a ser editado
# param opcao: Opção selecionada no menu de edição
# return: Retorna True se for atualizado com sucesso, False em erro
def atualizar(pacote: dict, opcao: str) -> bool:
    match opcao:
        case "1":
            while True:
                novo_nome = input("NOVO NOME DO PACOTE: ").strip().upper()
                if novo_nome == "":
                    print("ERRO! O NOME DO PACOTE NÃO PODE FICAR VAZIO!")
                elif novo_nome != pacote["nome"] and pegar(novo_nome) is not None:
                    print("ERRO! ESSE PACOTE JÁ EXISTE!")
                else:
                    pacote["nome"] = novo_nome
                    break

        case "2":
            while True:
                novo_preco = entrada.inteiro("NOVO PREÇO DO PACOTE: ")
                if novo_preco < 0:
                    print("ERRO! O PREÇO NÃO PODE SER NEGATIVO!")
                else:
                    pacote["preco"] = novo_preco
                    break

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

            for num, p in enumerate(plantas_do_pacote):
                print(f"{num + 1} - {p['nome']}")

            escolha = entrada.inteiro("Escolha a planta que deseja remover: ")
            if escolha < 1 or escolha > len(plantas_do_pacote):
                print("ERRO! OPÇÃO INVÁLIDA!")
                return False

            planta_sel = plantas_do_pacote[escolha - 1]

            if planta_sel in pacote["plantas_comuns"]:
                pacote["plantas_comuns"].remove(planta_sel)
            elif planta_sel in pacote["plantas_raras"]:
                pacote["plantas_raras"].remove(planta_sel)
            else:
                pacote["plantas_ultra_raras"].remove(planta_sel)

            print("PLANTA REMOVIDA DO PACOTE!")

        case _:
            return False

    return True

# loja.atualizando()
# Procedimento de interface para alteração de pacotes
# return: Não retorna nada
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
    escolha = entrada.inteiro("Escolha o pacote: ")

    if escolha < 1 or escolha > len(lista_de_pacotes):
        print("ERRO! OPÇÃO INVÁLIDA!")
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