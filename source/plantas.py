# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# -------------------- BIBLIOTECAS --------------------
from bibliotecas import desenho, entrada
import menu

# -------------------- VARIÁVEIS DOS TIPOS DE PLANTAS --------------------

# Lista dos modelos/espécies pré-cadastrados no sistema (TipoPlanta)
lista_de_tipos_plantas = [
    {
        "nome": "CACTO",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "COMUM",
        "xp_atual": 0,
        "xp_maximo": 50,
        "descricao": "PLANTA RESISTENTE QUE ARMAZENA ÁGUA E SOBREVIVE EM CONDIÇÕES EXTREMAS."
    },
    {
        "nome": "SUCULENTA",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "COMUM",
        "xp_atual": 0,
        "xp_maximo": 50,
        "descricao": "PEQUENA E ADAPTÁVEL, PERFEITA PARA INICIANTES NO CULTIVO."
    },
    {
        "nome": "TULIPA",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "RARO",
        "xp_atual": 0,
        "xp_maximo": 100,
        "descricao": "FLOR ELEGANTE QUE FLORESCE EM CONDIÇÕES ESPECÍFICAS."
    },
    {
        "nome": "ÁRVORE ANTIGA",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "ULTRA RARO",
        "xp_atual": 0,
        "xp_maximo": 250,
        "descricao": "ÁRVORE PODEROSA COM CRESCIMENTO LENTO E GRANDE VALOR."
    }
]

# -------------------- FUNÇÕES DE CRUD --------------------

# plantas.adicionar()
# Procedimento que adiciona um novo modelo de TipoPlanta na lista
# param: l Lista de tipos de plantas
# param: n Nome da espécie da planta
# param: c Categoria de raridade (COMUM, RARO, ULTRA RARO)
# param: xm Quantidade máxima de XP necessária para o nível
# param: d Texto descritivo sobre a espécie
# return: Retorna True após adicionar com sucesso
def adicionar(l: list, n: str, c: str, xm: int, d: str) -> bool:
    try:
        nova_planta = {
            "nome": n,
            "nivel_inicial": 1,
            "nivel_maximo": 5,
            "categoria": c,
            "xp_atual": 0,  
            "xp_maximo": xm,
            "descricao": d
        }
        l.append(nova_planta)
    except Exception as err:
        print(f"Ops, deu erro ao tentar cadastrar a planta: {err}")
        return False
    else:
        return True
    finally:
        print("Registro finalizado.")

# plantas.pegar()
# Função que busca um TipoPlanta na lista pelo seu nome
# param: l Lista de tipos de plantas
# param: n Nome da espécie a ser buscada
# return: Retorna o dicionário do TipoPlanta ou None caso não encontre
def pegar(l: list, n: str) -> dict | None:
    try:
        for p in l:
            if p.get("nome") == n:
                return p
    except Exception as err:
        print(f"Erro ao procurar a planta: {err}")
    finally:
        print("Busca finalizada.")
    return None

# plantas.remover()
# Função que remove um TipoPlanta da lista de espécies
# param: l Lista de tipos de plantas
# param: n Nome da espécie a ser removida
# return: Retorna True se for removido, False caso não encontre
def remover(l: list, n: str) -> bool:
    sucesso = False
    try:
        for num, item in enumerate(l):
            if item.get("nome") == n:
                l.pop(num)
                sucesso = True
                break
    except Exception as err:
        print(f"Não foi possível remover a planta: {err}")
        return False
    else:
        return sucesso
    finally:
        print("Remoção finalizada.")

# plantas.atualizar()
# Função que atualiza os dados de um TipoPlanta
# param: p Dicionário contendo os dados do TipoPlanta
# param: op Opção de campo selecionada no menu de edição
# param: l Lista de tipos de plantas
# return: Retorna True se a edição for realizada com sucesso, False se não
def atualizar(p: dict, op: str, l: list) -> bool:
    alterado = False
    try:
        match op:
            case "1":
                novo_nome = input("NOVO NOME DO TIPO DE PLANTA: ").strip().upper()
                if novo_nome == "":
                    print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
                    return False
                if pegar(l, novo_nome) is not None and novo_nome != p["nome"]:
                    print("ERRO! ESSE TIPO DE PLANTA JÁ EXISTE!")
                    return False
                p["nome"] = novo_nome
                alterado = True

            case "2":
                menu.desenhar("Tipo da planta")
                escolha = input("Escolha: ")
                match escolha:
                    case "1":
                        p["categoria"] = "COMUM"
                        alterado = True
                    case "2":
                        p["categoria"] = "RARO"
                        alterado = True
                    case "3":
                        p["categoria"] = "ULTRA RARO"
                        alterado = True
                    case _:
                        print("ERRO! OPÇÃO INVÁLIDA!")
                        return False

            case "3":
                while True:
                    xp_maximo = entrada.inteiro("NOVO XP MÁXIMO: ")
                    if xp_maximo <= 0:
                        print("ERRO! O XP MÁXIMO DEVE SER MAIOR QUE ZERO!")
                    else:
                        p["xp_maximo"] = xp_maximo
                        alterado = True
                        break

            case "4":
                nova_desc = input("NOVA DESCRIÇÃO: ").strip()
                if nova_desc == "":
                    print("ERRO! A DESCRIÇÃO NÃO PODE FICAR VAZIA!")
                    return False
                p["descricao"] = nova_desc
                alterado = True

            case _:
                return False
    except Exception as err:
        print(f"Erro ao salvar alterações da planta: {err}")
        return False
    else:
        return alterado
    finally:
        print("Edição finalizada.")

# -------------------- TELAS E PROCEDIMENTOS DE GERENCIAMENTO --------------------

# plantas.criando()
# Procedimento de interface interativa para cadastro de novo TipoPlanta
# param: l Lista de tipos de plantas
# return: Não retorna nada
def criando(l: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("CRIANDO TIPO DE PLANTA")

    while True:
        nome = input("NOME DO TIPO DE PLANTA: ").strip().upper()
        if nome == "":
            print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
        elif pegar(l, nome) is not None:
            print("ERRO! ESSE TIPO DE PLANTA JÁ EXISTE!")
        else:
            break

    while True:
        menu.desenhar("Tipo da planta")
        escolha = input("Escolha a categoria: ")
        match escolha:
            case "1":
                categoria = "COMUM"
                break
            case "2":
                categoria = "RARO"
                break
            case "3":
                categoria = "ULTRA RARO"
                break
            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    while True:
        xp_maximo = entrada.inteiro("XP MÁXIMO: ")
        if xp_maximo <= 0:
            print("ERRO! O XP MÁXIMO DEVE SER MAIOR QUE ZERO!")
        else:
            break

    descricao = input("DESCRIÇÃO: ").strip()
    if adicionar(l, nome, categoria, xp_maximo, descricao):
        print(f"\nTIPO DE PLANTA '{nome}' CRIADO COM SUCESSO!")
    desenho.espera_entrada()

# plantas.atualizando()
# Procedimento de interface para alteração de Tipos de Plantas existentes
# param: l Lista de tipos de plantas
# return: Não retorna nada
def atualizando(l: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EDITANDO TIPOS DE PLANTAS")
    print()

    if len(l) == 0:
        print("NENHUM TIPO DE PLANTA FOI CRIADO!")
        desenho.espera_entrada()
        return

    for num, p in enumerate(l):
        print(f"  {num + 1}. {p['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL DESEJA EDITAR: ")
        if 1 <= escolha <= len(l):
            planta = l[escolha - 1]
            break
        print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

    while True:
        desenho.limpar()
        desenho.linha()
        print()
        desenho.titulo(f"EDITANDO: {planta['nome']}")
        print()

        menu.desenhar("Editando planta")
        escolha = input("ESCOLHA: ").strip()

        if escolha == "5":
            break

        resultado = atualizar(planta, escolha, l)
        if resultado:
            print("TIPO DE PLANTA ATUALIZADO!")
        desenho.espera_entrada()

# plantas.listar()
# Procedimento que exibe na tela todos os Tipos de Plantas e suas propriedades
# param: l Lista de tipos de plantas
# return: Não retorna nada
def listar(l: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("TIPOS DE PLANTAS CADASTRADOS")
    print()

    if len(l) == 0:
        print("NENHUM TIPO DE PLANTA CADASTRADO!")
    else:
        for num, p in enumerate(l):
            print(f"NOME.............: {p['nome']}")
            print(f"NÍVEL INICIAL....: {p['nivel_inicial']}")
            print(f"NÍVEL MÁXIMO.....: {p['nivel_maximo']}")
            print(f"CATEGORIA........: {p['categoria']}")
            print(f"XP INICIAL.......: {p['xp_atual']}")
            print(f"XP MÁXIMO........: {p['xp_maximo']}")
            print(f"DESCRIÇÃO........: {p['descricao']}")
            print()
            desenho.linha()

    desenho.espera_entrada()

# plantas.excluindo()
# Procedimento de interface para exclusão de um TipoPlanta
# param: l Lista de tipos de plantas
# return: Não retorna nada
def excluindo(l: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EXCLUINDO TIPO DE PLANTA")

    if len(l) == 0:
        print("\nNENHUM TIPO DE PLANTA CADASTRADO!")
        desenho.espera_entrada()
        return

    print()
    for num, p in enumerate(l):
        print(f"  {num + 1}. {p['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL DESEJA EXCLUIR: ")
        if 1 <= escolha <= len(l):
            planta = l[escolha - 1]

            print(f"\nTIPO SELECIONADO: {planta['nome']}")
            confirmar = input("DESEJA REALMENTE EXCLUIR? (S/N): ").upper().strip()

            if confirmar == "S":
                if remover(l, planta["nome"]):
                    print(f"TIPO DE PLANTA {planta['nome']} EXCLUÍDO!")
                break
            elif confirmar == "N":
                print("EXCLUSÃO CANCELADA!")
                break
            else:
                print("ERRO! DIGITE S OU N!")
        else:
            print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

    desenho.espera_entrada()