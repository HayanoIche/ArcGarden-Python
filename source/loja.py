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
# param: l Lista de pacotes
# param: n Nome do pacote
# param: pr Custo em Arc-Score
# return: Retorna True após cadastrar
def adicionar(l: list, n: str, pr: int) -> bool:
    try:
        novo_pacote = {
            "nome": n,
            "preco": pr,
            "plantas_comuns": list(),
            "plantas_raras": list(),
            "plantas_ultra_raras": list()
        }
        l.append(novo_pacote)
    except Exception as err:
        print(f"Ops, falha ao adicionar o pacote: {err}")
        return False
    else:
        return True
    finally:
        print("Registro finalizado.")

# loja.pegar()
# Função que busca um pacote na lista pelo seu nome
# param: l Lista de pacotes
# param: n Nome do pacote
# return: Retorna o dicionário do pacote ou None se não encontrar nada
def pegar(l: list, n: str) -> dict | None:
    try:
        for pac in l:
            if pac.get("nome") == n:
                return pac
    except Exception as err:
        print(f"Erro ao pesquisar o pacote: {err}")
    finally:
        print("Busca finalizada.")
    return None

# loja.remover()
# Função que deleta um pacote da loja pelo nome
# param: l Lista de pacotes
# param: n Nome do pacote a remover
# return: Retorna True se remover, False caso contrário
def remover(l: list, n: str) -> bool:
    sucesso = False
    try:
        for num, pac in enumerate(l):
            if pac.get("nome") == n:
                l.pop(num)
                sucesso = True
                break
    except Exception as err:
        print(f"Erro ao tentar remover o pacote: {err}")
        return False
    else:
        return sucesso
    finally:
        print("Remoção finalizada.")

# -------------------- GERENCIAMENTO DE CONTEÚDO DOS PACOTES --------------------

# loja.adicionar_planta()
# Procedimento que vincula um TipoPlanta a um pacote filtrando pela categoria
# param: pac Dicionário do pacote a ser modificado
# param: cat Categoria da planta (COMUM, RARO, ULTRA RARO)
# param: p_lista Lista com os tipos de plantas cadastrados
# return: Não retorna nada
def adicionar_planta(pac: dict, cat: str, p_lista: list) -> None:
    try:
        plantas_disponiveis = list()

        for item in p_lista:
            if item["categoria"] == cat:
                plantas_disponiveis.append(item)

        if len(plantas_disponiveis) == 0:
            print("NENHUM TIPO DE PLANTA DESSA CATEGORIA FOI CADASTRADO!")
            return

        print(f"PLANTAS {cat}:")
        for num, item in enumerate(plantas_disponiveis):
            print(f"{num + 1} - {item['nome']}")

        escolha = entrada.inteiro("Escolha a planta: ")
        if escolha < 1 or escolha > len(plantas_disponiveis):
            print("ERRO! OPÇÃO INVÁLIDA!")
            return

        planta_escolhida = plantas_disponiveis[escolha - 1]

        match cat:
            case "COMUM":
                alvo = pac["plantas_comuns"]
            case "RARO":
                alvo = pac["plantas_raras"]
            case "ULTRA RARO":
                alvo = pac["plantas_ultra_raras"]

        if planta_escolhida in alvo:
            print("ERRO! ESSA PLANTA JÁ ESTÁ NO PACOTE!")
            return

        alvo.append(planta_escolhida)
        print(f"PLANTA {planta_escolhida['nome']} ADICIONADA!")
    except Exception as err:
        print(f"Erro ao colocar planta no pacote: {err}")
    finally:
        print(">> Atualização de plantas finalizada.")

# loja.atualizar()
# Função que edita um atributo do pacote selecionado
# param: pac Dicionário do pacote a ser editado
# param: op Opção selecionada no menu de edição
# param: l Lista de pacotes
# param: p Lista de tipos de plantas
# return: Retorna True se for atualizado com sucesso, False em erro
def atualizar(pac: dict, op: str, l: list, p: list) -> bool:
    alterado = False
    try:
        match op:
            case "1":
                while True:
                    novo_nome = input("NOVO NOME DO PACOTE: ").strip().upper()
                    if novo_nome == "":
                        print("ERRO! O NOME DO PACOTE NÃO PODE FICAR VAZIO!")
                    elif novo_nome != pac["nome"] and pegar(l, novo_nome) is not None:
                        print("ERRO! ESSE PACOTE JÁ EXISTE!")
                    else:
                        pac["nome"] = novo_nome
                        alterado = True
                        break

            case "2":
                while True:
                    novo_preco = entrada.inteiro("NOVO PREÇO DO PACOTE: ")
                    if novo_preco < 0:
                        print("ERRO! O PREÇO NÃO PODE SER NEGATIVO!")
                    else:
                        pac["preco"] = novo_preco
                        alterado = True
                        break

            case "3":
                while True:
                    menu.desenhar("Adicionar Planta")
                    escolha = input("Escolha: ")
                    match escolha:
                        case "1":
                            adicionar_planta(pac, "COMUM", p)
                            alterado = True
                        case "2":
                            adicionar_planta(pac, "RARO", p)
                            alterado = True
                        case "3":
                            adicionar_planta(pac, "ULTRA RARO", p)
                            alterado = True
                        case "4":
                            break
                        case _:
                            print("ERRO! OPÇÃO INVÁLIDA!")
                            desenho.espera_entrada()

            case "4":
                plantas_do_pacote = (
                    pac["plantas_comuns"]
                    + pac["plantas_raras"]
                    + pac["plantas_ultra_raras"]
                )

                if len(plantas_do_pacote) == 0:
                    print("NENHUMA PLANTA FOI ADICIONADA AO PACOTE!")
                    return False

                for num, item in enumerate(plantas_do_pacote):
                    print(f"{num + 1} - {item['nome']}")

                escolha = entrada.inteiro("Escolha a planta que deseja remover: ")
                if escolha < 1 or escolha > len(plantas_do_pacote):
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

                planta_sel = plantas_do_pacote[escolha - 1]

                if planta_sel in pac["plantas_comuns"]:
                    pac["plantas_comuns"].remove(planta_sel)
                elif planta_sel in pac["plantas_raras"]:
                    pac["plantas_raras"].remove(planta_sel)
                else:
                    pac["plantas_ultra_raras"].remove(planta_sel)

                print("PLANTA REMOVIDA DO PACOTE!")
                alterado = True

            case _:
                return False
    except Exception as err:
        print(f"Erro ao editar o pacote: {err}")
        return False
    else:
        return alterado
    finally:
        print(">> Edição finalizada.")

# -------------------- TELAS E PROCEDIMENTOS DE GERENCIAMENTO --------------------

# loja.criando()
# Procedimento de interface para criação interativa de pacotes na loja
# param: l Lista de pacotes
# param: p Lista de tipos de plantas
# return: Não retorna nada
def criando(l: list, p: list) -> None:
    while True:
        desenho.limpar()
        nome = input("NOME DO PACOTE: ").strip().upper()

        if nome == "":
            print("ERRO! O NOME DO PACOTE NÃO PODE FICAR VAZIO!")
        elif pegar(l, nome) is not None:
            print("ERRO! ESSE PACOTE JÁ EXISTE!")
        else:
            break

    while True:
        preco = entrada.inteiro("PREÇO DO PACOTE: ")
        if preco < 0:
            print("ERRO! O PREÇO NÃO PODE SER NEGATIVO!")
        else:
            break

    if adicionar(l, nome, preco):
        pacote = pegar(l, nome)

        while True:
            print()
            menu.desenhar("Adicionar Planta")
            escolha = input("Escolha: ")

            match escolha:
                case "1":
                    adicionar_planta(pacote, "COMUM", p)
                case "2":
                    adicionar_planta(pacote, "RARO", p)
                case "3":
                    adicionar_planta(pacote, "ULTRA RARO", p)
                case "4":
                    break
                case _:
                    print("ERRO! OPÇÃO INVÁLIDA!")

        print(f"PACOTE {nome} CRIADO!")

# loja.listar()
# Procedimento que lista na tela todos os pacotes e suas respectivas plantas
# param: l Lista de pacotes
# return: Não retorna nada
def listar(l: list) -> None:
    print()
    desenho.linha()
    desenho.titulo("PACOTES DA LOJA")
    desenho.linha()
    print()

    if len(l) == 0:
        print("NENHUM PACOTE FOI CRIADO!")
    else:
        for num, pacote in enumerate(l):
            print(f"PACOTE {num + 1}")
            print(f"NOME........: {pacote['nome']}")
            print(f"PREÇO.......: {pacote['preco']}")

            print("PLANTAS COMUNS:")
            for item in pacote["plantas_comuns"]:
                print(f"- {item['nome']}")

            print("PLANTAS RARAS:")
            for item in pacote["plantas_raras"]:
                print(f"- {item['nome']}")

            print("PLANTAS ULTRA RARAS:")
            for item in pacote["plantas_ultra_raras"]:
                print(f"- {item['nome']}")

            desenho.linha()
            
    desenho.espera_entrada()

# loja.excluindo()
# Procedimento de interface para exclusão de um pacote da loja
# param: l Lista de pacotes
# return: Não retorna nada
def excluindo(l: list) -> None:
    if len(l) == 0:
        print("NENHUM PACOTE FOI CRIADO!")
        return

    desenho.linha()
    desenho.titulo("EXCLUIR PACOTE")
    desenho.linha()

    for num, pacote in enumerate(l):
        print(f"{num + 1} - {pacote['nome']}")

    escolha = entrada.inteiro("Escolha o pacote: ")
    if escolha < 1 or escolha > len(l):
        print("ERRO! OPÇÃO INVÁLIDA!")
        return

    pacote = l[escolha - 1]
    confirmacao = input(f"DESEJA REALMENTE EXCLUIR O PACOTE {pacote['nome']}? (S/N): ").upper().strip()

    if confirmacao == "S":
        if remover(l, pacote["nome"]):
            print("PACOTE EXCLUÍDO COM SUCESSO!")
    elif confirmacao == "N":
        print("EXCLUSÃO CANCELADA!")
    else:
        print("ERRO! OPÇÃO INVÁLIDA!")

    desenho.espera_entrada()

# loja.atualizando()
# Procedimento de interface para alteração de pacotes
# param: l Lista de pacotes
# param: p Lista de tipos de plantas
# return: Não retorna nada
def atualizando(l: list, p: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("Atualizar Pacote")
    print()

    if len(l) == 0:
        print("NENHUM PACOTE FOI CRIADO!")
        desenho.linha()
        desenho.espera_entrada()
        return

    desenho.linha()
    for num, pacote in enumerate(l):
        print(f"{num + 1} - {pacote['nome']}")

    print()
    escolha = entrada.inteiro("Escolha o pacote: ")

    if escolha < 1 or escolha > len(l):
        print("ERRO! OPÇÃO INVÁLIDA!")
        desenho.espera_entrada()
        return

    pacote = l[escolha - 1]

    while True:
        desenho.limpar()
        menu.desenhar("Editando pacote")
        escolha = input("Escolha: ")

        if escolha == "5":
            break

        resultado = atualizar(pacote, escolha, l, p)
        if resultado:
            print("PACOTE ATUALIZADO!")

        desenho.espera_entrada()